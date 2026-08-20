## Orientation

Stack Studio directs an agent to:

1. Initialize the skill catalog with `stack-studio-init`.
2. Enter through `create-stack` for target selection, the human’s desired outcome, stack composition, iterative work, and eventual audit.
3. Use `iterate-toward-outcomes` for continued progress, evidence gathering, optional work-frontier state, and conditional transitions.
4. Use `writing-skills` to author and behaviorally evaluate individual skills.
5. Use `wizard` only for genuinely human-only procedures.
6. Finish with `audit-and-publish` for structural validation and packaging readiness.

The repository already contains a work frontier tailored to this exact self-hosting goal. Its outcome and preservation envelope are strong: agent-facing use from incomplete goals, stack-level coherence, responsiveness to human evidence, self-hosting, one truthful authority per workflow concern, preserved authoring/evaluation/auditing/portability, and separation of deterministic mechanics from judgment.

## Current authorities and transitions

The effective authority map is:

- Human: desired outcome and consequential subjective decisions.
- Target repository: authoritative implementation state.
- `create-stack`: stack domain, target, composition, user experience, and review cadence.
- `iterate-toward-outcomes`: ongoing work selection, observation, reorientation, and exceptional-condition routing.
- Optional work frontier: outcome, learned invariants, active evaluation regime, and unresolved prediction errors.
- `writing-skills`: individual-skill creation and behavioral evaluation.
- `audit-and-publish`: structural integrity and packaging readiness.
- `wizard`: bounded manual/human-only setup.
- Supporting outcome skills: ambiguity resolution, prediction-error handling, invariant discovery, reorientation, evaluator evolution, and frontier compaction.

The important transition defect is that `create-stack → iterate-toward-outcomes` is only inferred. Likewise, `create-stack → writing-skills` and `create-stack → wizard` are discoverable from metadata but not explicitly composed into one lifecycle. By contrast, transitions internal to `iterate-toward-outcomes` are explicit and carefully documented.

This creates two competing stack-level authorities:

- `create-stack` says to work iteratively, continually reorient, and review.
- `iterate-toward-outcomes` independently owns the actual iteration loop, evidence model, stopping conditions, and transition routing.

A diligent agent can reconcile them, but the intended end-to-end process is emergent rather than repository-owned.

## Evaluation and publication path

Individual-skill evaluation is comparatively mature. `writing-skills` defines a scaled RED/GREEN/REFACTOR loop:

- capture intent and trigger conditions;
- author the smallest reusable skill change;
- create realistic prompts;
- run paired with-skill/baseline checks when warranted;
- add objective assertions where appropriate;
- grade outputs, aggregate benchmarks, inspect transcripts, and optionally use blind comparison;
- present qualitative outputs and quantitative evidence to the human;
- iterate from feedback;
- optimize trigger descriptions and package a `.skill` artifact.

Stack-level evaluation is the missing layer. The existing `.codex/evaluation-scenarios.md` correctly requires fresh-agent, end-to-end journeys and checks cross-skill routing, shared representations, preservation constraints, human-decision boundaries, deterministic tools, and stopping conditions. That is the right evidence model, but no production skill owns it or transitions to it.

A reliable assembled-stack evaluation should therefore freeze a scenario/check set, run fresh agents against the whole installed stack, preserve raw transcripts and artifacts, and judge:

- whether the correct skills trigger;
- whether transitions are explicit rather than invented;
- whether all outcome capabilities are covered;
- whether shared state and tooling have one authority;
- whether cross-skill journeys succeed;
- whether individual-skill improvements survive composition;
- whether the stack reaches a release-ready or explicitly blocked state.

Publication currently means preparation, not publication. `audit-and-publish` runs an automated audit, checks frontmatter, structure, permissions, manifests, cleanliness, links, and installation documentation. It does not define versioning, tagging, releases, marketplace/registry submission, or a destination-specific transaction. A truthful lifecycle must either add those actions or rename/scope the boundary as “release preparation” and explicitly hand off to destination-specific publishing.

The current strict self-audit reports “PASSED” and optimistic platform readiness scores, but those scores are presence heuristics. They do not prove semantic compatibility. Some documented requirements—such as descriptions starting with “Use when,” link validity, README quality, and practical installation behavior—are manual or unenforced. The description-optimization/evaluation entry points also fail under the snapshot’s Python runtime because `str | None` is evaluated on a Python version that does not support that syntax; `package_skill.py` does run.

## Ambiguities requiring resolution

- Which skill becomes the sole authority for continued stack-level progress: a strengthened `create-stack`, a stack-specific replacement for the generic iteration loop, or a renamed unified orchestrator?
- Whether the generic outcome/frontier skills remain public standalone skills, become supporting references behind the primary stack workflow, or move elsewhere.
- Whether stack-level behavioral evaluation belongs inside the primary lifecycle or in one explicitly invoked supporting skill.
- Whether “publish” includes actual external release transactions, and which destinations are supported.
- What “supported across a harness” means operationally: manifest presence, successful discovery, trigger behavior, or an end-to-end installed probe.
- Whether the platform documentation’s claims are current and authoritative; it calls itself exact but records neither provenance nor version boundaries.
- Which Python versions the bundled evaluation tools promise to support.

Most of these can be resolved by repository evidence and targeted probes. The publication destination and any compatibility promises that materially affect scope should be confirmed with the human before implementation.

## First concrete work unit

Consolidate the stack-level lifecycle before reorganizing supporting skills.

The first candidate change should make one primary skill explicitly own the complete loop from incomplete goal to release-ready stack, with named transitions to:

- individual-skill authoring and evaluation;
- whole-stack behavioral evaluation;
- bounded human evidence;
- deterministic audit/package verification;
- publication or an explicit external-publication boundary.

I would start by drafting that authority and transition contract, using the current `create-stack` and `iterate-toward-outcomes` content as source material rather than immediately deleting either. Then I would test the draft against the existing self-hosting scenario with a fresh agent. This work unit attacks the highest-leverage prediction error, remains reversible, and provides evidence for which supporting skills can later be merged, demoted to references, or retained independently. No files were changed.
