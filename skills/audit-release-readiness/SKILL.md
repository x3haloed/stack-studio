---
name: audit-release-readiness
description: Use when checking whether a skill-stack repository is structurally ready for release, calibrating harness-support claims to evidence, or preparing a truthful handoff to a separately authorized publication process.
---

# Audit Release Readiness

Read [stack-studio-init](../stack-studio-init/SKILL.md) once if Stack Studio has not yet been oriented in this task.

This skill owns deterministic repository checks and the release-readiness handoff. It does not install into a harness, prove runtime behavior, create a release, submit to a marketplace, or publish externally.

## Support contract

Use these evidence levels; never replace them with percentages:

1. **Not claimed:** No current, documented harness contract is implemented.
2. **Structure verified:** Repository files satisfy the deterministic contract documented for that harness.
3. **Discovery verified:** A recorded test shows the target harness installed or discovered the stack and exposed the expected skills.
4. **Behavior verified:** Recorded target-harness journeys show the installed stack producing the intended behavior.

Each level includes the levels below it. State the harness, harness version or observation date, test procedure, and evidence location for discovery or behavior claims. A repository audit can award only **structure verified**.

## Workflow

1. Read [Harness Contracts](references/platforms.md) and select only the intended targets. Do not infer one harness’s manifest from another’s.
2. Run the deterministic audit:

   ```bash
   python3 skills/audit-release-readiness/scripts/audit_stack.py . --strict
   ```

   Use `--platform <name>` to limit the support report or `--json` for structured output.
3. Resolve errors. Review warnings rather than converting them into compatibility claims.
4. For each claimed harness, record the highest evidence level actually reached. Follow [Repository Layout](references/universal-layout.md) for the shared core and harness-specific adapters.
5. Run discovery and behavioral probes in each target harness when those stronger claims matter. Preserve commands, versions, transcripts, and artifacts.
6. Produce a release-readiness handoff containing:

   - deterministic audit result;
   - support matrix with evidence levels and dates;
   - behavioral evaluation result;
   - unresolved warnings or unsupported targets;
   - intended version and destination;
   - clean-tree or exact-diff evidence.

Stop there unless the user separately authorizes a specific publication transaction. Publication authority belongs to the destination-specific release process and may require credentials, versioning decisions, tags, marketplace metadata, review, or external writes.

## Deterministic promises

The bundled auditor checks only:

- `skills/<name>/SKILL.md` inventory, required frontmatter, directory/name agreement, description size, and progressive-disclosure warnings;
- JSON syntax, required identity, declared in-repository paths, and the documented Claude Code and OpenAI manifest locations;
- relative links from `README.md` and skill entry files;
- executable permission on script files that declare a shebang;
- common generated or platform-local artifacts;
- README presence.

It does not validate prose quality, semantic compatibility, installation, skill triggering, runtime behavior, credentials, marketplace acceptance, or publication.
