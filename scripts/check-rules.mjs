#!/usr/bin/env node
/**
 * Verify every `skill` id in skill-rules.json resolves to a real skill folder
 * (skills/<domain>/<name>/SKILL.md), and that every skill folder is covered by
 * a rule. Exit non-zero on mismatch so this can run in CI.
 */
import { readFileSync, readdirSync, existsSync, statSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = join(HERE, "..");
const SKILLS = join(REPO, "skills");

// Collect skill names from the filesystem.
const found = new Map(); // name -> "domain/name"
for (const domain of readdirSync(SKILLS)) {
  const dpath = join(SKILLS, domain);
  if (!statSync(dpath).isDirectory()) continue;
  for (const name of readdirSync(dpath)) {
    const spath = join(dpath, name, "SKILL.md");
    if (existsSync(spath)) {
      // Skill `name` is the cross-domain identifier in skill-rules.json; a
      // collision across domains would silently overwrite one skill's rules.
      if (found.has(name)) {
        console.error(
          `FAIL: duplicate skill name "${name}" in both "${found.get(name)}" and "${domain}/${name}"`
        );
        process.exit(1);
      }
      found.set(name, `${domain}/${name}`);
    }
  }
}

const rules = JSON.parse(readFileSync(join(REPO, "skill-rules.json"), "utf8"));
if (!Array.isArray(rules.activation_rules)) {
  console.error("FAIL: skill-rules.json must contain an 'activation_rules' array.");
  process.exit(1);
}
const ruleSkills = new Set(rules.activation_rules.map((r) => r.skill));

const errors = [];

// Every rule must resolve to a real skill.
for (const r of rules.activation_rules) {
  if (!found.has(r.skill)) {
    errors.push(`rule references unknown skill: ${r.skill}`);
  }
  for (const k of ["keywords", "file_patterns", "commands"]) {
    if (!Array.isArray(r.triggers?.[k])) {
      errors.push(`rule ${r.skill}: triggers.${k} must be an array`);
    }
  }
}

// Every skill should be covered by a rule.
for (const [name, id] of found) {
  if (!ruleSkills.has(name)) errors.push(`skill ${id} has no activation rule`);
}

// Reference orchestrators (agents/*/AGENT.md) may only compose skills that exist.
const AGENTS = join(REPO, "agents");
let agentCount = 0;
if (existsSync(AGENTS)) {
  for (const a of readdirSync(AGENTS)) {
    const apath = join(AGENTS, a, "AGENT.md");
    if (!existsSync(apath)) continue;
    agentCount++;
    const text = readFileSync(apath, "utf8");
    if (!text.includes("Built on SIP")) {
      errors.push(`agent ${a}: missing 'Built on SIP' attestation footer`);
    }
    const m = text.match(/^composes:\s*\[([^\]]*)\]/m);
    const composed = m ? m[1].split(",").map((s) => s.trim()).filter(Boolean) : [];
    if (composed.length === 0) {
      errors.push(`agent ${a}: 'composes' must list at least one skill`);
    }
    for (const skill of composed) {
      if (!found.has(skill)) errors.push(`agent ${a}: composes unknown skill "${skill}"`);
    }
  }
}

if (errors.length) {
  console.error(`FAIL: ${errors.length} issue(s):`);
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}
console.log(
  `OK: ${found.size} skills, ${rules.activation_rules.length} rules, ${agentCount} orchestrators, all resolve.`
);
