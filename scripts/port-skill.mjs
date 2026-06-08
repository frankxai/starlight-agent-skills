#!/usr/bin/env node
/**
 * Port a skill from this library into a consumer repo (SIS / ACOS / any).
 *
 * Usage:
 *   node scripts/port-skill.mjs <domain/skill> --target=<path> [--dest=<subdir>] [--dry-run]
 *
 * Examples:
 *   node scripts/port-skill.mjs cosmos/apod-to-short --target=/path/to/Starlight-Intelligence-System
 *   node scripts/port-skill.mjs media/social-repurposer --target=/path/to/agentic-creator-os --dest=.claude/skills
 *
 * Behavior:
 *   - Copies skills/<domain>/<name>/ into <target>/<dest>/<domain>/<name>/.
 *   - Rewrites self-referential relative links (../../<domain>/...) to the
 *     destination's layout so cross-skill references keep resolving.
 *   - Verifies the SKILL.md carries the "Built on SIP" attestation footer; refuses
 *     to port without it (silent composition is a protocol breach).
 *   - --dry-run prints the plan and the attestation check without writing.
 *
 * Default --dest is "skills" (SIS layout). ACOS uses ".claude/skills".
 */
import { readFileSync, writeFileSync, mkdirSync, readdirSync, statSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join, relative, resolve, isAbsolute, sep } from "node:path";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = join(HERE, "..");

const args = process.argv.slice(2);
const skillId = args.find((a) => !a.startsWith("--"));
const opt = (name, def) => {
  const a = args.find((x) => x.startsWith(`--${name}=`));
  return a ? a.split("=").slice(1).join("=") : def;
};
const dryRun = args.includes("--dry-run");
const target = opt("target", null);
const dest = opt("dest", "skills");

if (!skillId || !skillId.includes("/")) {
  console.error("Usage: port-skill.mjs <domain/skill> --target=<path> [--dest=<subdir>] [--dry-run]");
  process.exit(2);
}
if (!target) {
  console.error("Error: --target=<path> is required.");
  process.exit(2);
}

const parts = skillId.split("/");
const [domain, name] = parts;
const SEG_RE = /^[a-z0-9][a-z0-9-]*$/;
// Reject malformed or traversal-laden ids (e.g. "cosmos/../../etc").
if (parts.length !== 2 || !SEG_RE.test(domain) || !SEG_RE.test(name)) {
  console.error(`Error: invalid skill id ${JSON.stringify(skillId)} — expected "<domain>/<skill>" in kebab-case.`);
  process.exit(2);
}
// `dest` must be a relative subpath with no traversal segments.
if (isAbsolute(dest) || dest.split(/[\\/]/).some((s) => s === ".." )) {
  console.error(`Error: --dest must be a relative path without ".." segments (got ${JSON.stringify(dest)}).`);
  process.exit(2);
}
const src = join(REPO, "skills", domain, name);
const skillMd = join(src, "SKILL.md");
if (!existsSync(skillMd)) {
  console.error(`Error: skill not found: ${relative(REPO, skillMd)}`);
  process.exit(1);
}

// Attestation gate.
const md = readFileSync(skillMd, "utf8");
if (!md.includes("Built on SIP")) {
  console.error(`Error: ${skillId} is missing the "Built on SIP" attestation footer. Refusing to port.`);
  process.exit(1);
}

const destRoot = join(target, dest, domain, name);
// Defense in depth: confirm the resolved destination stays inside --target.
const targetBase = resolve(target);
const destResolved = resolve(destRoot);
if (destResolved !== targetBase && !destResolved.startsWith(targetBase + sep)) {
  console.error(`Error: refusing to write outside --target (${targetBase}). Computed ${destResolved}.`);
  process.exit(2);
}

function walk(dir) {
  const out = [];
  for (const e of readdirSync(dir)) {
    const p = join(dir, e);
    if (statSync(p).isDirectory()) out.push(...walk(p));
    else out.push(p);
  }
  return out;
}

const files = walk(src);
console.log(`Porting ${skillId} -> ${destRoot}`);
console.log(`Attestation: OK ("Built on SIP" present)`);
console.log(`Files: ${files.length}`);

for (const f of files) {
  const rel = relative(src, f);
  const out = join(destRoot, rel);
  let body = readFileSync(f, "utf8");
  // Rewrite cross-skill references that point up out of this skill
  // (../../<otherdomain>/...) so they resolve under the destination layout.
  // The destination keeps the same <domain>/<name> nesting, so sibling-domain
  // references remain valid; we only normalize doc links back to the library.
  // `[^)\n]*` keeps the match within a single markdown link (no cross-line
  // backtracking / ReDoS, and no swallowing past the intended link).
  body = body.replace(/\]\((\.\.\/){3,}[^)\n]*\)/g, (m) =>
    m.replace(/\((\.\.\/)+/, "(https://github.com/frankxai/starlight-agent-skills/blob/main/")
  );
  if (dryRun) {
    console.log(`  [dry-run] would write ${relative(target, out)}`);
  } else {
    mkdirSync(dirname(out), { recursive: true });
    writeFileSync(out, body);
    console.log(`  wrote ${relative(target, out)}`);
  }
}

console.log(dryRun ? "Dry run complete — nothing written." : "Done.");
