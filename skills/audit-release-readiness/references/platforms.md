# Harness contracts

Harness contracts change. Treat this as a dated source map, not proof that a repository works in a harness. Reviewed 2026-08-20.

## Claude Code

The auditor verifies `skills/<name>/SKILL.md`, `.claude-plugin/plugin.json`, a kebab-case manifest name, and any declared in-repository component paths. Default component locations make a `skills` manifest field optional.

Official sources: [Create plugins](https://code.claude.com/docs/en/plugins) and [Plugins reference](https://code.claude.com/docs/en/plugins-reference).

To claim discovery, record a `claude --plugin-dir .` test (or marketplace installation), confirm the expected skills appear, and record the version. Claim behavior only after representative journeys succeed.

## OpenAI ChatGPT and Codex

The auditor verifies `skills/<name>/SKILL.md` and `.codex-plugin/plugin.json`. A minimal distributable plugin has stable kebab-case `name`, `version`, `description`, and `skills: "./skills/"`. Repo-scoped `.agents/skills` discovery is a separate authoring mode, not distributable-plugin evidence.

Official sources: [Build skills](https://learn.chatgpt.com/docs/build-skills) and [Package your plugin](https://developers.openai.com/plugins/build/plugins).

To claim discovery, install from a local or repository marketplace and record that expected skills appear in a new task. Claim behavior only after representative journeys succeed.

## Cursor, Google Antigravity, and GitHub Copilot

Stack Studio currently makes no deterministic packaging claim for these harnesses. A root `plugin.json`, `.cursor-plugin/plugin.json`, `AGENTS.md`, or `skills/` directory alone is not proof of support.

Before adding one of these targets:

1. identify a current primary-source discovery or packaging contract;
2. add a harness-specific deterministic validator and fixtures;
3. add repository-relative installation instructions;
4. preserve a target-harness discovery probe;
5. preserve behavior probes before claiming behavior verification.

Portable `SKILL.md` syntax can reduce authoring differences, but format portability is not installation, discovery, or behavioral support.
