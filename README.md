# Stack Studio

> Easily craft, iterate, audit, and publish skill stacks as plugins across major AI coding harnesses.

Stack Studio is a meta-suite of skills, reference blueprints, and verification tooling designed to help developers and AI agents build high-quality, reusable "skill stacks" (similar to [gstack](https://github.com/garrytan/gstack) or [pstack](https://github.com/cursor/plugins/tree/main/pstack)) that work seamlessly across:

- **Anthropic Claude Code**
- **Cursor IDE**
- **Google Antigravity**
- **OpenAI Codex & Operator**
- **GitHub Copilot**

---

## Included Skills

| Skill | Description | Entry Point |
| :--- | :--- | :--- |
| **`create-stack`** | Design or modify a "*-stack" bundle of related skills. | [`skills/create-stack/SKILL.md`](skills/create-stack/SKILL.md) |
| **`audit-and-publish`** | Audit frontmatter, script permissions, and plugin manifests for multi-harness compatibility. | [`skills/audit-and-publish/SKILL.md`](skills/audit-and-publish/SKILL.md) |
| **`writing-skills`** | TDD-driven skill creation, evaluation benchmarks, and progressive disclosure design. | [`skills/writing-skills/SKILL.md`](skills/writing-skills/SKILL.md) |
| **`wizard`** | Scope and generate interactive bash wizards for manual human-gated steps. | [`skills/wizard/SKILL.md`](skills/wizard/SKILL.md) |
| **`iterate-toward-outcomes`** | Manage long-running, outcome-anchored iterations without premature architectural lock-in. | [`skills/iterate-toward-outcomes/SKILL.md`](skills/iterate-toward-outcomes/SKILL.md) |
| **`stack-studio-init`** | Environment initializer to pull skills into context. | [`skills/stack-studio-init/SKILL.md`](skills/stack-studio-init/SKILL.md) |

---

## Installation Across Platforms

### 1. Anthropic Claude Code
Clone or link into your project's `.claude/skills/` directory (or globally in `~/.claude/skills/`):
```bash
git clone https://github.com/x3haloed/stack-studio.git ~/.claude/skills/stack-studio
```

### 2. Cursor IDE
Clone or link into your local plugins directory:
```bash
git clone https://github.com/x3haloed/stack-studio.git ~/.cursor/plugins/local/stack-studio
```
Then reload the window in Cursor (`Developer: Reload Window`).

### 3. Google Antigravity
Clone or link into your workspace `.agents/plugins/` directory:
```bash
git clone https://github.com/x3haloed/stack-studio.git .agents/plugins/stack-studio
```

### 4. OpenAI Codex & GitHub Copilot
Add as a submodule or plugin dependency within your project root:
```bash
git submodule add https://github.com/x3haloed/stack-studio.git plugins/stack-studio
```

---

## Auditing a Stack

Stack Studio includes an automated auditor to verify frontmatter, progressive disclosure limits, script permissions, and multi-platform plugin manifests:

```bash
python3 skills/audit-and-publish/scripts/audit_stack.py /path/to/target-stack
```

Options:
- `--strict`: Fail on warnings as well as errors.
- `--json`: Output structured machine-readable JSON.
- `--platform <platform>`: Target checks for `claude`, `cursor`, `antigravity`, `openai`, or `copilot`.

---

## License
MIT
