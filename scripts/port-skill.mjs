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
import { dirname, join, relative } from "node:path";

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

const [domain, name] = skillId.split("/");
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
  body = body.replace(/\]\((\.\.\/){3,}[^)]*\)/g, (m) =>
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
