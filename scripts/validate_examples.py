#!/usr/bin/env python3
"""Validate every skill's `examples/example-01.md` output against its `manifest.json`.

For each `skills/<domain>/<name>/` directory that has BOTH a `manifest.json` and
an `examples/example-01.md`:
  * the example's `## Output` section must contain a fenced ```json block
    (the LAST ```json block in the file, per the observed repo convention —
    some examples show an intermediate ```mdx/other block before the JSON)
  * that block must parse as valid JSON
  * every output declared in manifest.json `outputs[]` must be present in the
    parsed JSON, with a value of the declared `type` (string/array/number/
    object/boolean) — unless the output is `"nullable": true` and the value is
    `null`
  * skill-specific mechanical invariants from `tests/contract.md` are enforced
    where they are checkable by plain code (see CONTRACT_CHECKS below); items
    that require human/LLM judgment are intentionally not encoded

Skills with no `manifest.json` or no `examples/example-01.md` (e.g. the
`substrate` domain, which ships SKILL.md only) are skipped and counted
separately — this is expected, not a failure.

Exit code is non-zero if any validated skill fails, so this can run in CI.
Zero third-party dependencies (standard library only).
"""
from __future__ import annotations
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "skills")

# The observed convention (verified against 10 skills across cosmos, research,
# media, coding, education, brand): the output JSON lives in the LAST fenced
# ```json code block in examples/example-01.md, typically under an "## Output"
# heading. We deliberately match "the last ```json block" rather than "the
# block right after ## Output" so we still work on skills whose Output section
# additionally shows a non-JSON block (e.g. an ```mdx block) before the JSON.
JSON_FENCE_RE = re.compile(r"```json\s*\n(.*?)```", re.S)

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Lightweight JSX tag matcher — NOT a real parser. Captures (is_close, tag_name,
# is_self_closing) for capitalized component tags like <FactTable .../> or
# <AtlasHero>...</AtlasHero>. The attribute segment is matched non-greedily so
# a trailing `/` (self-closing marker) is left for the third group instead of
# being swallowed as "just another attribute character".
JSX_TAG_RE = re.compile(r"<(/?)([A-Z][A-Za-z0-9]*)[^<>]*?(/)?>")

JSON_TYPE_CHECKS = {
    "string": lambda v: isinstance(v, str),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "array": lambda v: isinstance(v, list),
    "object": lambda v: isinstance(v, dict),
}


def extract_output_json(example_text: str) -> tuple[dict | list | None, str | None]:
    """Return (parsed_json, error). Uses the LAST ```json fenced block in the file."""
    blocks = JSON_FENCE_RE.findall(example_text)
    if not blocks:
        return None, "no fenced ```json code block found in examples/example-01.md"
    raw = blocks[-1]
    try:
        return json.loads(raw), None
    except json.JSONDecodeError as e:
        return None, f"the last ```json block is not valid JSON ({e})"


def check_outputs_match_manifest(
    data: dict | list, outputs: list[dict], path: str, errors: list[str]
) -> None:
    if not isinstance(data, dict):
        errors.append(f"{path}: example output JSON is a {type(data).__name__}, expected a JSON object")
        return
    for out in outputs:
        if not isinstance(out, dict):
            errors.append(f"{path}: manifest output entry is not a JSON object")
            continue
        name = out.get("name")
        want_type = out.get("type")
        nullable = out.get("nullable", False)
        if name is None:
            continue
        if name not in data:
            errors.append(f"{path}: manifest output {name!r} is missing from the example's JSON")
            continue
        value = data[name]
        if value is None:
            if nullable:
                continue
            errors.append(f"{path}: output {name!r} is null in the example but manifest does not mark it nullable")
            continue
        checker = JSON_TYPE_CHECKS.get(want_type)
        if checker is None:
            continue  # unknown/unsupported declared type — nothing to mechanically check
        if not checker(value):
            errors.append(
                f"{path}: output {name!r} has type {type(value).__name__}, expected {want_type!r}"
            )


def _jsx_tag_balance(mdx: str) -> list[tuple[str, int, int]]:
    """Return (tag, open_count, close_count) for each capitalized JSX-like tag
    referenced in `mdx`. Self-closing tags (`<Foo ... />`) count as neither an
    open nor a close needing a match. This is a lightweight heuristic, not a
    real parser — good enough to catch a stray unmatched <Foo> in an example.
    """
    opens: dict[str, int] = {}
    closes: dict[str, int] = {}
    for is_close, name, is_self_closing in JSX_TAG_RE.findall(mdx):
        if is_self_closing:
            continue
        if is_close:
            closes[name] = closes.get(name, 0) + 1
        else:
            opens[name] = opens.get(name, 0) + 1
    tags = set(opens) | set(closes)
    return [(t, opens.get(t, 0), closes.get(t, 0)) for t in sorted(tags)]


# ---------------------------------------------------------------------------
# Mechanical contract checks, keyed by "<domain>/<name>".
#
# Each entry is a function(data: dict, path: str, errors: list[str]) -> None
# that encodes ONLY the objective, code-checkable assertions from that skill's
# tests/contract.md — judgment-call items ("hook respects the audience's
# intelligence", "no clickbait framing", "tone is appropriate", etc.) are
# intentionally left out; a human/LLM review is still required for those.
# ---------------------------------------------------------------------------


def _check_apod_to_short(data: dict, path: str, errors: list[str]) -> None:
    # rights_line is a non-empty string
    rights = data.get("rights_line")
    if isinstance(rights, str) and not rights.strip():
        errors.append(f"{path}: rights_line is empty")
    # captions: array with >=1 entry, each <=7 words
    captions = data.get("captions")
    if isinstance(captions, list):
        if len(captions) < 1:
            errors.append(f"{path}: captions must have >= 1 entry")
        for i, cap in enumerate(captions):
            if isinstance(cap, str) and len(cap.split()) > 7:
                errors.append(f"{path}: captions[{i}] has more than 7 words ({cap!r})")
    # script word count ~= duration_sec * 2.5 (+/-15%)
    script = data.get("script")
    duration = data.get("duration_sec")
    if isinstance(script, str) and isinstance(duration, (int, float)) and not isinstance(duration, bool):
        words = len(script.split())
        target = duration * 2.5
        low, high = target * 0.85, target * 1.15
        if not (low <= words <= high):
            errors.append(
                f"{path}: script word count {words} outside {low:.1f}-{high:.1f} "
                f"expected for duration_sec={duration}"
            )


def _check_nasa_image_to_atlas_page(data: dict, path: str, errors: list[str]) -> None:
    # slug is kebab-case
    slug = data.get("slug")
    if isinstance(slug, str) and not SLUG_RE.match(slug):
        errors.append(f"{path}: slug {slug!r} is not kebab-case")
    # frontmatter includes title, object, and at least one catalog_id
    frontmatter = data.get("frontmatter")
    if isinstance(frontmatter, dict):
        title = frontmatter.get("title")
        if not (isinstance(title, str) and title.strip()):
            errors.append(f"{path}: frontmatter.title is missing or empty")
        obj = frontmatter.get("object")
        if not (isinstance(obj, str) and obj.strip()):
            errors.append(f"{path}: frontmatter.object is missing or empty")
        catalog_ids = frontmatter.get("catalog_ids")
        if not (isinstance(catalog_ids, list) and len(catalog_ids) >= 1):
            errors.append(f"{path}: frontmatter.catalog_ids must include at least one catalog ID")
    # mdx has balanced JSX-like components (heuristic, not a real parser)
    mdx = data.get("mdx")
    if isinstance(mdx, str):
        for tag, opens, closes in _jsx_tag_balance(mdx):
            if opens != closes:
                errors.append(
                    f"{path}: mdx has unbalanced <{tag}> components ({opens} opening, {closes} closing)"
                )
    # every row in facts has a non-empty source
    facts = data.get("facts")
    if isinstance(facts, list):
        for i, row in enumerate(facts):
            if isinstance(row, dict):
                source = row.get("source")
                if not (isinstance(source, str) and source.strip()):
                    errors.append(f"{path}: facts[{i}] has an empty or missing 'source'")
    # rights_line non-empty
    rights = data.get("rights_line")
    if isinstance(rights, str) and not rights.strip():
        errors.append(f"{path}: rights_line is empty")


def _check_rights_check_nasa_esa(data: dict, path: str, errors: list[str]) -> None:
    valid_verdicts = {"allowed-with-attribution", "check-license", "restricted", "do-not-publish-yet"}
    verdict = data.get("verdict")
    if verdict is not None and verdict not in valid_verdicts:
        errors.append(f"{path}: verdict {verdict!r} is not one of {sorted(valid_verdicts)}")
    attribution = data.get("attribution_line")
    if isinstance(attribution, str) and not attribution.strip():
        errors.append(f"{path}: attribution_line is empty")


def _check_arxiv_paper_to_brief(data: dict, path: str, errors: list[str]) -> None:
    # metadata includes a stable identifier
    metadata = data.get("metadata")
    if isinstance(metadata, dict):
        ident = metadata.get("id")
        if not (isinstance(ident, str) and ident.strip()):
            errors.append(f"{path}: metadata.id (stable identifier) is missing or empty")
    # every result has non-empty evidence
    results = data.get("results")
    if isinstance(results, list):
        for i, r in enumerate(results):
            if isinstance(r, dict):
                evidence = r.get("evidence")
                if not (isinstance(evidence, str) and evidence.strip()):
                    errors.append(f"{path}: results[{i}] has empty or missing 'evidence'")
    # limitations contains at least one item
    limitations = data.get("limitations")
    if isinstance(limitations, list) and len(limitations) < 1:
        errors.append(f"{path}: limitations must contain at least one item")


def _check_social_repurposer(data: dict, path: str, errors: list[str]) -> None:
    # Only the requested platforms are populated; others are null.
    # We can't know the request here without re-parsing the Input block, so we
    # only enforce the mechanically-derivable half: every populated platform
    # value has the type the manifest declares (handled generically above) and
    # rights_line, if present and non-null, is non-empty.
    rights = data.get("rights_line")
    if isinstance(rights, str) and not rights.strip():
        errors.append(f"{path}: rights_line is present but empty")


def _check_cosmic_code_lab(data: dict, path: str, errors: list[str]) -> None:
    for field in ("problem_statement", "starter_code", "tests", "solution", "science_note"):
        value = data.get(field)
        if isinstance(value, str) and not value.strip():
            errors.append(f"{path}: {field} is empty")


CONTRACT_CHECKS = {
    "cosmos/apod-to-short": _check_apod_to_short,
    "cosmos/nasa-image-to-atlas-page": _check_nasa_image_to_atlas_page,
    "cosmos/rights-check-nasa-esa": _check_rights_check_nasa_esa,
    "research/arxiv-paper-to-brief": _check_arxiv_paper_to_brief,
    "media/social-repurposer": _check_social_repurposer,
    "coding/cosmic-code-lab": _check_cosmic_code_lab,
}


def validate_skill(skill_dir: str, domain: str, name: str, errors: list[str]) -> bool:
    """Validate one skill. Returns True if it passed (or had nothing to check)."""
    rel = os.path.relpath(skill_dir, os.path.join(ROOT, ".."))
    manifest_path = os.path.join(skill_dir, "manifest.json")
    example_path = os.path.join(skill_dir, "examples", "example-01.md")

    try:
        with open(manifest_path, encoding="utf-8") as f:
            manifest = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        errors.append(f"{rel}: manifest.json is not valid JSON ({e})")
        return False

    if not isinstance(manifest, dict):
        errors.append(f"{rel}: manifest.json is not a JSON object")
        return False

    outputs = manifest.get("outputs", [])
    if not isinstance(outputs, list):
        errors.append(f"{rel}: manifest.json 'outputs' is not an array")
        return False

    try:
        with open(example_path, encoding="utf-8") as f:
            example_text = f.read()
    except OSError as e:
        errors.append(f"{rel}: could not read examples/example-01.md ({e})")
        return False

    data, err = extract_output_json(example_text)
    if err is not None:
        errors.append(f"{rel}: {err}")
        return False

    before = len(errors)
    check_outputs_match_manifest(data, outputs, rel, errors)

    key = f"{domain}/{name}"
    contract_check = CONTRACT_CHECKS.get(key)
    if contract_check is not None and isinstance(data, dict):
        contract_check(data, rel, errors)

    return len(errors) == before


def main() -> int:
    errors: list[str] = []
    passed = 0
    skipped = 0

    for domain in sorted(os.listdir(ROOT)):
        domain_dir = os.path.join(ROOT, domain)
        if not os.path.isdir(domain_dir):
            continue
        for name in sorted(os.listdir(domain_dir)):
            skill_dir = os.path.join(domain_dir, name)
            if not os.path.isdir(skill_dir):
                continue
            manifest_path = os.path.join(skill_dir, "manifest.json")
            example_path = os.path.join(skill_dir, "examples", "example-01.md")
            if not (os.path.exists(manifest_path) and os.path.exists(example_path)):
                skipped += 1
                continue

            skill_errors: list[str] = []
            ok = validate_skill(skill_dir, domain, name, skill_errors)
            rel = os.path.relpath(skill_dir, os.path.join(ROOT, ".."))
            if ok:
                print(f"PASS  {rel}")
                passed += 1
            else:
                print(f"FAIL  {rel}")
                for e in skill_errors:
                    print(f"        - {e}")
            errors.extend(skill_errors)

    print()
    if errors:
        print(f"FAIL: {len(errors)} issue(s) across skill example(s).")
        print(f"OK: {passed} skill(s) validated, {skipped} skipped (no examples/manifest).")
        return 1

    print(f"OK: {passed} skill(s) validated, {skipped} skipped (no examples/manifest).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
