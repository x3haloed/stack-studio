## Orientation

Stack Studio directs this request into `create-stack`, after a one-time `stack-studio-init` check. The repository is not greenfield: it is a self-hosting reorganization with useful behavior to preserve.

The persisted outcome already matches the request: an agent should be able to take an incomplete human “-stack” goal and collaboratively produce or improve a coherent, tested, publishable stack across supported harnesses. The preservation envelope includes:

- agent-facing use without requiring the human to learn the internal catalog;
- stack-level coherence;
- iterative response to human intent and observed evidence;
- self-hosting;
- one truthful authority per behavior;
- adapted rather than mechanically copied iteration patterns;
- deterministic tooling separated from agent and human judgment;
- cross-harness portability.

No files were edited.

## Workflow the repository directs

The intended loop is:

1. Inspect the target repository and classify the work as greenfield, extension, or reorganization.
2. Establish the outcome, preservation requirements, relevant environments, and trustworthy evidence.
3. Use the target repository as implementation authority and maintain only durable decision state in one work frontier.
4. Design from end-to-end agent journeys, assigning each behavior one authority and making contracts and handoffs explicit.
5. Execute one coherent work unit at a time.
6. Use `writing-skills` for individual-skill creation or material revision.
7. Obtain practical evidence, including assembled cross-skill behavior.
8. Update only decision-relevant frontier state and continue until verified, release-ready, published, or genuinely blocked.
9. Run `audit-and-publish` after structural changes and before release.
10. Distinguish behavioral verification, release readiness, and actual publication.

That control loop is explicit in `create-stack`, including the stack-building cycle and completion states.

## Authorities and transitions

The intended authority map is substantially clearer than the repository’s broad skill catalog initially suggests:

- Human: consequential outcome and experiential judgment.
- Target repository: authoritative implementation record.
- `create-stack`: continued stack-level progress, topology, cross-skill coherence, stack-level evaluation, and honest completion state.
- `writing-skills`: individual-skill authoring and individual-skill evaluation.
- `audit-and-publish`: structural validation and release preparation.
- Scripts: deterministic mechanics, never outcome judgment.
- Work frontier: only nonduplicative, durable decision state.
- `wizard`: durable human-operated procedures for steps an agent cannot perform.
- Exceptional-condition skills: transition handlers inside the `create-stack` loop, not parallel project workflows.

The explicit transition handlers are prediction-error resolution, bounded human evidence, invariant discovery, outcome reorientation, frontier compaction, evaluation-regime evolution, and wizard creation. `create-stack` states this well.

`writing-skills` still contains its own broad iterative language—“figure out where the user is” and move to the next useful step—but its operating domain is individual skills. The hierarchy is recoverable because `create-stack` explicitly limits it; without reading `create-stack`, the standalone metadata and body could still make `writing-skills` appear to own more of a stack project than intended.

## Evaluation and publication path

For assembled evaluation, the repository directs me to:

- freeze the current criterion;
- run realistic primary and boundary journeys with fresh agents;
- expose only ordinary user/harness context;
- observe routing, authority handoffs, shared state, deterministic outputs, bounded human input, and final outcome satisfaction;
- preserve raw output separately from assessments;
- score checks as `pass`, `fail`, or `not_exercised`;
- compare candidates only under unchanged scenarios;
- evolve the evaluator only at an explicit boundary.

The self-hosting, greenfield ETL, and existing VM scenarios provide a reasonable stack-level evaluation set. `stack_eval.py` now supplies initialization, schema validation, finalization, and same-scenario comparison. Its four unit tests pass.

The release path is currently weaker:

1. Obtain behavioral evidence.
2. Run the structural audit.
3. Review manifests, links, permissions, installation guidance, and repository cleanliness.
4. Prepare release metadata.
5. Perform an explicitly authorized external publication transaction.
6. Verify that transaction before claiming “published.”

The repository handles steps 1–4 conceptually, but not step 5 for any concrete destination.

## Material findings and ambiguities

1. `create-stack` is now the clear progress authority. The largest original authority-collapse problem appears structurally addressed in that file.

2. Publication remains an authority gap. `audit-and-publish` claims “publishing” in its trigger and heading, but its procedure ends with preparation and handoff; it defines no versioning, tagging, registry, marketplace, or release transaction. The frontier records the same unresolved discrepancy.

3. Cross-harness claims are not yet trustworthy enough for “release-ready.” The platform reference calls its schemas exact, but its root universal manifest and its OpenAI-specific manifest describe incompatible shapes. The current root manifest follows the former.

4. The auditor overstates compatibility. It assigns “Ready” scores largely from file/directory presence. For example, OpenAI receives 80% from any `plugin.json` plus `skills/`, without validating the OpenAI-specific schema documented in the reference. It similarly reports Copilot 100% from a generic manifest, `AGENTS.md`, and `skills/`.

5. The strict audit passes despite missing stated checks. The skill promises verification of descriptions starting with “Use when,” relative Markdown links, repository cleanliness, and executable helper scripts. The script does not enforce the prefix, does not check links or scratch files, and only warns about non-executable shell scripts. A committed `.DS_Store` exists under `skills/writing-skills/`, yet strict audit passes.

6. README discoverability is stale. It lists only five skills and omits the transition handlers that `create-stack` relies on. This does not necessarily require cataloging every helper, but the README should make the primary entry point and subordinate topology unmistakable.

7. Supported harness scope needs human confirmation before publication work. “Support” could mean syntactic packaging, discoverability, tested installation, or exercised behavior. Those are materially different promises.

8. Publication destination needs human authority. Git tags, GitHub releases, registries, and harness marketplaces have different credentials and irreversible external effects. Stack Studio should either own explicitly selected destinations or name a clean external handoff.

9. The worktree already contains modified and untracked self-hosting/evaluation work. Any implementation must preserve and understand those changes rather than treating the current checkout as a clean baseline.

## First concrete work unit

I would make the first work unit a narrow release-readiness contract repair:

- define exactly what “supported” and “release-ready” mean per claimed harness;
- reconcile the universal and platform-specific manifest guidance;
- align `audit-and-publish`’s name, scope, and handoff with actual publication authority;
- add deterministic checks for the promises it already makes: trigger prefix, links, scratch artifacts, relevant executable permissions, and platform-specific manifest shape;
- test those checks with passing and deliberately failing fixtures;
- rerun the strict audit and the self-hosting scenario under the frozen evaluation criterion.

This is the highest-leverage first slice because it preserves the newly clear `create-stack` authority while closing the strongest remaining gap between “publishable” and what the repository can presently verify.
