---
name: audit-and-publish
description: Use when auditing, validating, packaging, or publishing a stack/plugin repository to ensure compatibility across major agentic harnesses (Claude Code, Cursor, Antigravity, OpenAI Codex, GitHub Copilot).
---

# Audit and Publish

**Important:** read [skill-studio-init](../stack-studio-init/SKILL.md) if you haven't yet to ensure you've got all the context you need about stack-studio skills. This is a one-time operation.

This skill guides you through auditing a stack repository for structural integrity, validating skill frontmatter, checking script execution permissions, and preparing the repository to be installed cleanly as a plugin across major agentic harnesses.

## Reference Guides

- [Universal Polyglot Stack Layout](references/universal-layout.md): Blueprint for configuring a single repository to work across all 5 major platforms.
- [Platforms Reference](references/platforms.md): Exact manifest schemas, discovery paths, and platform-specific behaviors for Claude Code, Cursor, Antigravity, OpenAI Codex, and GitHub Copilot.

---

## Audit and Publishing Workflow

Follow this procedure whenever creating, modifying, or finalizing a stack repository:

### 1. Run Automated Verification

Execute the bundled audit script against the target repository:

```bash
python <path-to-stack-studio>/skills/audit-and-publish/scripts/audit_stack.py <target-repo-path>
```

Add `--strict` to treat warnings as errors, or `--json` for structured reporting.

### 2. Verify Core Frontmatter and Structure

Check that each skill in `skills/<skill-name>/` satisfies the standard contract:

1. **Naming:** `name` in frontmatter matches the directory name.
2. **Triggering Description:** `description` is concise (< 600 characters), starts with `Use when...`, and lists concrete triggering conditions rather than workflow summaries.
3. **Progressive Disclosure:** Keep `SKILL.md` under 500 lines. Move heavy documentation, API specifications, and schemas into `references/`.
4. **Script Permissions:** Any helper in `scripts/` must have executable permissions (`chmod +x scripts/*`).

### 3. Ensure Multi-Harness Manifests

To allow the stack to be installed as a plugin, verify or create the appropriate manifest files (see [Universal Layout](references/universal-layout.md)):

- **Root `plugin.json`**: For open standard agent plugins, Cursor, OpenAI Codex, Antigravity, and GitHub Copilot.
- **`.cursor-plugin/plugin.json`**: For Cursor IDE native discovery.
- **`mcp.json` / `mcp_config.json`**: When tools or external servers are bundled.
- **`CLAUDE.md` / `AGENTS.md`**: For repository-level agent guidance.

### 4. Perform a Clean Review Pass

Before publishing or handing off the stack:
- Run `git status` or file inspection to ensure no temporary scratch files, dangling logs, or `.DS_Store` files are present.
- Verify relative markdown links between `SKILL.md` files, references, and scripts.
- Ensure the `README.md` clearly explains how to install the stack on each target harness (e.g., cloning into `~/.claude/skills/`, adding to `.cursor/plugins/local/`, or registering in `.agents/plugins/`).
