# Description Optimization and Environment Adaptation

The description field in `SKILL.md` frontmatter is the primary mechanism that determines whether an agent invokes a skill. After creating or improving a skill, optimize the description for triggering accuracy.

## Adapters for Model Behavior

- **Default for Codex:** `--trigger-adapter codex-exec` and `--improver-adapter codex`.
- **Optional Anthropic Compatibility:** `--trigger-adapter claude-code` and `--improver-adapter anthropic`.
- **Headless Mode:** Pass `--no-open` to `scripts/run_loop.py` to write reports without opening a browser. Use `--report none` to disable reports entirely.

---

## 4-Step Optimization Workflow

### Step 1: Generate Trigger Eval Queries
Create 20 eval queries — a balanced mix of should-trigger (8-10) and should-not-trigger (8-10 near misses). Save as JSON:
```json
[
  {"query": "concrete realistic user prompt", "should_trigger": true},
  {"query": "near miss prompt that should not trigger", "should_trigger": false}
]
```

### Step 2: Review with User
1. Read the template from `assets/eval_review.html`.
2. Replace placeholders `__EVAL_DATA_PLACEHOLDER__`, `__SKILL_NAME_PLACEHOLDER__`, `__SKILL_DESCRIPTION_PLACEHOLDER__`.
3. Save to a temporary HTML file and review with the user to export `eval_set.json`.

### Step 3: Run the Optimization Loop
```bash
python scripts/run_loop.py \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --trigger-adapter codex-exec \
  --improver-adapter codex \
  --model <model-id-powering-this-session> \
  --max-iterations 5 \
  --no-open \
  --verbose
```

### Step 4: Apply the Result
Take `best_description` from the output JSON and update the skill's `SKILL.md` frontmatter.

---

## Environment Adaptation

- **CLI-enabled environments:** Use `run_eval.py` and `improve_description.py`.
- **No subagents:** Run test prompts sequentially in conversation.
- **No browser/display:** Use `generate_review.py --static <output_path>`.
- **Packaging:** `python scripts/package_skill.py <path/to/skill-folder>`.
