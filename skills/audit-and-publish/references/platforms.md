# Agentic Harness Platforms Reference

This document provides exact manifest schemas, directory layouts, discovery paths, and configuration requirements for bundling skills into plugins across the top coding and agentic harnesses.

---

## 1. Anthropic Claude Code

Claude Code supports prompt-based workflows and skills invoked directly or via slash commands (e.g., `gstack`, `/review`).

### Discovery Locations
- **Project Scope:** `./.claude/` (committed to version control for team sharing)
- **Global Scope:** `~/.claude/` (user-level configuration)

### Directory Layout
```text
my-stack/
├── CLAUDE.md                # System instructions & operating guidelines
├── settings.json            # Project-specific permissions & tool config
├── skills/                  # Skills directory
│   └── <skill-name>/
│       ├── SKILL.md         # YAML frontmatter + instructions
│       ├── scripts/         # Executable helper scripts
│       └── references/      # Progressive disclosure references
├── commands/                # Custom slash command markdown files
│   └── review.md
└── rules/                   # Modular, path-scoped instructions
    └── *.md
```

### Installation
- **Local/Team:** Clone or symlink the stack into `./.claude/skills/` or `~/.claude/skills/`.
- **Slash Commands:** Any skill in `skills/<name>/SKILL.md` or command in `commands/<name>.md` becomes callable via `/<name>`.

---

## 2. Cursor IDE

Cursor supports modular agent capabilities via **Agent Plugins** (the open standard) and **Cursor Plugins** (`.cursor-plugin/`).

### Discovery Locations
- **Local Plugins:** `~/.cursor/plugins/local/<plugin-name>/`
- **Project Scope:** `.cursor/` or root `.cursorrules` / `.cursor/rules/*.mdc`

### Manifest (`plugin.json` / `.cursor-plugin/plugin.json`)
```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Short description of the plugin and its capabilities.",
  "author": {
    "name": "Author Name"
  },
  "skills": "./skills/",
  "commands": "./commands/",
  "rules": "./rules/",
  "mcp": "./mcp.json"
}
```

### Directory Layout
```text
my-plugin/
├── plugin.json              # Open agent plugin manifest
├── .cursor-plugin/
│   └── plugin.json          # Cursor-specific manifest
├── mcp.json                 # MCP server definitions
├── skills/
│   └── <skill-name>/
│       └── SKILL.md
├── commands/
│   └── workflow.md
└── rules/
    └── conventions.mdc
```

---

## 3. Google Antigravity

Google Antigravity provides a namespaced customization system bundling skills, rules, lifecycle hooks, and MCP servers.

### Discovery Locations
- **Project Scope:** `.agents/plugins/<plugin-name>/` or root of registered workspace plugin repos
- **Global Scope:** `~/.gemini/config/`

### Manifest (`plugin.json`)
```json
{
  "name": "my-plugin",
  "description": "Plugin bundle description",
  "disabled": false
}
```

### Lifecycle Hooks (`hooks.json`)
```json
{
  "hooks": {
    "pre_tool_execution": [
      {
        "matcher": "run_command",
        "script": "scripts/pre_command_check.sh"
      }
    ]
  }
}
```

### MCP Configuration (`mcp_config.json`)
```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["dist/index.js"]
    }
  }
}
```

---

## 4. OpenAI Codex & Operator Platforms

OpenAI's agent ecosystem packages skills alongside MCP servers for agentic execution.

### Discovery Locations
- **Workspace/Package Root:** `skills/` + `plugin.json`
- **MCP Discovery:** `.well-known/mcp.json` or `mcp.json`

### Manifest (`plugin.json`)
```json
{
  "schema_version": "v1",
  "name_for_human": "My Stack",
  "name_for_model": "my_stack",
  "description_for_human": "Human-facing description of the stack.",
  "description_for_model": "Guidance for model routing and skill triggers.",
  "skills": "./skills/",
  "mcp": "./mcp.json"
}
```

---

## 5. GitHub Copilot

GitHub Copilot supports custom agents (`*.agent.md`), skills, instructions, and hooks into installable plugins.

### Discovery Locations
- **Repository Scope:** `.github/copilot-instructions.md`, `.github/agents/`
- **Plugin Scope:** Root of plugin repository with `plugin.json`

### Directory Layout
```text
my-copilot-plugin/
├── plugin.json
├── mcp.json
├── hooks/
│   └── hooks.json
├── agents/
│   └── reviewer.agent.md
├── skills/
│   └── <skill-name>/
│       └── SKILL.md
└── instructions/
    └── coding-guidelines.md
```
