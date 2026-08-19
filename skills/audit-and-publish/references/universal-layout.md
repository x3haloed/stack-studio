# Universal Polyglot Stack Layout

This reference blueprint shows how to configure a single repository so it can be installed, discovered, and executed cleanly across all 5 major platforms (Claude Code, Cursor, Antigravity, OpenAI Codex, GitHub Copilot).

---

## The Master Blueprint

```text
<stack-repo-name>/
├── README.md                          # Human onboarding & installation instructions
├── AGENTS.md                          # Universal agent guidelines (cross-platform standard)
├── CLAUDE.md                          # Claude Code root instructions
├── GEMINI.md                          # Antigravity project-level rules (optional)
├── plugin.json                        # Root plugin manifest (Cursor, OpenAI, Copilot, Antigravity)
├── .cursor-plugin/                    # Cursor IDE plugin manifest
│   └── plugin.json
├── mcp.json                           # Standard MCP config (Cursor, Claude, Copilot, OpenAI)
├── mcp_config.json                    # Antigravity MCP config (can mirror mcp.json)
├── hooks.json                         # Lifecycle hooks (Antigravity, Copilot)
├── skills/                            # Universal Skills (All harnesses)
│   ├── <skill-1>/
│   │   ├── SKILL.md                   # YAML frontmatter + Markdown body
│   │   ├── scripts/                   # Executable scripts (chmod +x)
│   │   └── references/                # Deep reference docs (< 500 lines)
│   └── <skill-2>/
│       └── SKILL.md
├── rules/                             # Guidelines / Scoped rules (.md or .mdc)
│   └── *.md
└── commands/                          # Slash commands / workflows (.md)
    └── *.md
```

---

## Universal Manifest (`plugin.json`)

Place this `plugin.json` at the root of the repository:

```json
{
  "name": "my-stack",
  "version": "1.0.0",
  "description": "Multi-agent skill stack providing specialized workflows and capabilities.",
  "author": {
    "name": "Author Name"
  },
  "skills": "./skills/",
  "rules": "./rules/",
  "commands": "./commands/",
  "mcp": "./mcp.json",
  "hooks": "./hooks.json"
}
```

---

## Universal Skill Standard (`SKILL.md`)

Every skill within `skills/<skill-name>/SKILL.md` must follow progressive disclosure:

1. **YAML Frontmatter (Level 1 - Metadata in context):**
   ```yaml
   ---
   name: <skill-name>
   description: Use when <concrete triggering conditions and symptoms>.
   ---
   ```
2. **SKILL.md Body (Level 2 - In context when triggered):**
   - High-level playbook, principles, and decision logic.
   - Target line count: **< 500 lines**.
3. **Bundled Resources (Level 3 - Loaded on demand):**
   - `scripts/`: Deterministic code. Ensure files are executable (`chmod +x`).
   - `references/`: Detailed specifications, API documentation, schemas.
   - `assets/`: Templates, images, boilerplates.
