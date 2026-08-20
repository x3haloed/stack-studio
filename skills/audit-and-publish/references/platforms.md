# Agentic Harness Platforms Reference

This document provides exact manifest schemas, directory layouts, discovery paths, and configuration requirements for bundling skills into plugins across the top coding and agentic harnesses.

---

## 1. Anthropic Claude Code

Claude Code supports modular capabilities either packaged as **Plugins** or as standalone **Skills**.

### Discovery & Plugin Architecture
- **Official Plugin Manifest:** `.claude-plugin/plugin.json` located at the root of the plugin directory.
- **Plugin Discovery Locations:** `~/.claude/plugins/<plugin-name>/` or loaded via `claude --plugin-dir <plugin-directory>`.
- **Standalone Skills Location:** `~/.claude/skills/<skill-name>/SKILL.md` (individual skill folders directly inside `~/.claude/skills/`). Claude Code does not recursively scan subdirectories of `~/.claude/skills/` looking for nested skill bundles; a bundle repo must either be installed as a plugin with `.claude-plugin/plugin.json` or have its individual skill folders symlinked into `~/.claude/skills/`.
- **Important Context Rule:** A `CLAUDE.md` located inside a plugin repository is **not** loaded as project context when the plugin is installed. Project instructions only load from the active workspace root or `~/.claude/CLAUDE.md`.

### Manifest (`.claude-plugin/plugin.json`)
```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Short description of the plugin and its capabilities.",
  "author": {
    "name": "Author Name"
  },
  "skills": "./skills/"
}
```

### Directory Layout (Plugin Mode)
```text
my-stack/
├── .claude-plugin/
│   └── plugin.json          # Required Claude Code plugin manifest
├── skills/                  # Skills directory discovered by plugin
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
- **As a Plugin (Recommended):** Clone into `~/.claude/plugins/my-stack/` or test with `claude --plugin-dir <stack-directory>`.
- **As Standalone Skills:** Symlink each folder in `skills/*` into `~/.claude/skills/`.
- **Slash Commands:** Skills inside the plugin are accessible via the `/plugin-name:skill-name` namespace or direct skill name if uniquely matched.

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
