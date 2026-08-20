# Shared repository layout

There is no universal plugin manifest. Share skill content where contracts overlap and keep packaging adapters explicit.

```text
<stack-repo>/
├── README.md
├── AGENTS.md                         # repository guidance, not plugin proof
├── .claude-plugin/
│   └── plugin.json                   # Claude Code adapter
├── .codex-plugin/
│   └── plugin.json                   # OpenAI plugin adapter
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── scripts/
│       ├── references/
│       └── assets/
└── .codex/
    └── evaluations/                  # optional preserved evidence
```

Add a harness adapter only when a current primary source defines it and the repository has a deterministic contract test. Do not create a root `plugin.json` as a synthetic common denominator.

- Shared skill content can be structurally reusable.
- A harness-specific manifest can make structure verifiable.
- Only a live harness probe can verify discovery.
- Only journey evidence can verify behavior.
- Only a completed external transaction can establish publication.
