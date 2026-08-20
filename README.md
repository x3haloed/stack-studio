# Stack Studio

> Design, iterate, evaluate, and prepare coherent agent skill stacks for truthful release.

Stack Studio helps an agent turn an evolving human goal into a coherent, tested, release-ready "skill stack." Its shared skill format is portable, while packaging and runtime support are claimed separately for each harness and only to the level demonstrated by evidence.

The repository currently has deterministic packaging contracts for **Claude Code** and **OpenAI ChatGPT/Codex**. Cursor, Google Antigravity, and GitHub Copilot remain unclaimed until current harness-specific contracts and live discovery evidence are added.

---

## Included Skills

| Skill | Description | Entry Point |
| :--- | :--- | :--- |
| **`create-stack`** | Own the end-to-end design, implementation, evaluation, and release-readiness loop for a coherent "*-stack". | [`skills/create-stack/SKILL.md`](skills/create-stack/SKILL.md) |
| **`audit-release-readiness`** | Verify deterministic release properties and calibrate harness-support claims to evidence. | [`skills/audit-release-readiness/SKILL.md`](skills/audit-release-readiness/SKILL.md) |
| **`writing-skills`** | TDD-driven skill creation, evaluation benchmarks, and progressive disclosure design. | [`skills/writing-skills/SKILL.md`](skills/writing-skills/SKILL.md) |
| **`wizard`** | Scope and generate interactive bash wizards for manual human-gated steps. | [`skills/wizard/SKILL.md`](skills/wizard/SKILL.md) |
| **`stack-studio-init`** | Environment initializer to pull skills into context. | [`skills/stack-studio-init/SKILL.md`](skills/stack-studio-init/SKILL.md) |

---

## Harness packaging

### 1. Anthropic Claude Code

Test the repository as a plugin checkout:
```bash
git clone https://github.com/x3haloed/stack-studio.git stack-studio
claude --plugin-dir ./stack-studio
```

The Claude adapter is `.claude-plugin/plugin.json`.

### 2. OpenAI ChatGPT and Codex

The OpenAI adapter is `.codex-plugin/plugin.json`. Add the checkout to a local or repository marketplace, install it, restart the host, and verify discovery in a new task. See the current [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins) for marketplace setup.

These are structural installation paths, not behavior claims. Record discovery and representative journey evidence before describing a harness as discovery-verified or behavior-verified.

---

## Auditing a Stack

Stack Studio includes an auditor for deterministic repository and packaging properties:

```bash
python3 skills/audit-release-readiness/scripts/audit_stack.py . --strict
```

Options:
- `--strict`: Fail on warnings as well as errors.
- `--json`: Output structured machine-readable JSON.
- `--platform <platform>`: Target checks for `claude`, `cursor`, `antigravity`, `openai`, or `copilot`.

---

## License
MIT
