# Real-World Evaluation

[简体中文](./REAL_WORLD_EVALUATION.zh.md)

> **Historical evidence snapshot:** the results below record pinned repositories and the Windows,
> model, and tooling context available in one authoring session. They preserve causal evidence; they
> are not a current compatibility matrix, cross-platform certification, or current-model benchmark.

Four independently developed public skill repositories were used as read-only test objects for
Skill Polisher:

1. [`Conradgui/Academic-Paper-Review-Skill`](https://github.com/Conradgui/Academic-Paper-Review-Skill/tree/9f3288f7a13e25400a8ff0c00eeb16270e37fe98)
2. [`Conradgui/zero-to-one-product-discovery`](https://github.com/Conradgui/zero-to-one-product-discovery/tree/b4556c895ba8c38af22c3662f326a1b45f1d434e)
3. [`Conradgui/project-verifier-skill`](https://github.com/Conradgui/project-verifier-skill/tree/df0bb00c06eae2a088c83ce45e51d64bbeb678f4)
4. [`Conradgui/immersive-motion-ui-skill`](https://github.com/Conradgui/immersive-motion-ui-skill/tree/51f5adb9949c5c8731011637958fcdfc82128fd3)

All four checkouts matched their GitHub `main` branches and were clean before and after testing. No
study repository was modified.

## Evaluation question

The test was not “how many lint warnings can Polisher produce?” It asked whether Polisher could:

- reconstruct the behavior and ownership contract of four different skill architectures;
- recognize mechanisms earned through iteration instead of treating complexity as automatic debt;
- prefer target-owned contract evidence over external heuristics;
- distinguish target defects from harness, platform, permission, and missing-evidence failures;
- collapse many repeated symptoms into the earliest evidenced common cause; and
- stop without prescribing architecture when the evidence does not justify change.

## Evidence labels

| Label | Meaning |
|---|---|
| **Preserve** | A learned invariant or coherent boundary supported by current artifacts and tests |
| **Change** | A confirmed defect or risk whose smallest justified action is evidence-backed |
| **Evidence limit** | A missing runtime, permission, platform, paid call, or independent context that narrows the claim |

External lint warnings are review prompts, not findings by themselves.

## Summary

| Repository | Target-owned evidence | Preserve | Change |
|---|---|---|---|
| Academic Paper Review | 28/28 skill-contract and 10/10 proofing tests pass; full suite 92/95 with three Windows symlink errors | Mode router, scientific/text axes, immutable polishing ledger, stable delta IDs, opt-in external research | 65-character Codex short description; make isolated-auth tests permission-aware on Windows |
| Zero-to-One Product Discovery | 71/71 unit tests pass | Controller-owned routing, stage purity, child-skill boundaries, narrow workbench state, schema-validated export and revision traces | 106-character Codex short description |
| Project Verifier | 11/11 static contract tests pass; full suite 27/105 in this Windows environment | Four-stage control plane, decision envelope, no-call preflight, separate progress/outcome/scope/claim state | Declare or adapt the Bash and `python3` maintainer runtime that drives 73 failures and 5 errors |
| Immersive Motion UI | Standalone manifest validator and 15/15 data-UI suite pass; ten other selected commands fail at the same path family | Core/optional-Library boundary, 14-capability graph, audit/redesign split, exact evidence outcomes | Replace 16 Windows-unsafe file-URL pathname conversions across runtime and test tooling |

## 1. Academic Paper Review

### Preserve

The repository contains two related but distinct skills. `paper-review` owns manuscript review,
delta review, reference audit, and explicitly requested authorial polishing; `latex-paper-review`
owns the LaTeX-specific specialist boundary. Within `paper-review`:

- scientific review and text-quality review remain independent axes;
- review is read-only while polishing protects claims, numbers, equations, citations, and labels;
- delta review preserves finding IDs and exact status vocabulary;
- external literature retrieval is opt-in;
- blind evaluation keeps source evidence and candidate output bounded.

The 337-line runtime is therefore not a defect merely because it is long. Current contract tests
assert the mode, ledger, ID, source, and evaluator boundaries that would be at risk in a casual
rewrite.

### Tests

- Skill Creator Pro structural validation: `paper-review` fails one metadata rule;
  `latex-paper-review` passes.
- `test_skill_contract.py`: 28/28 pass.
- `test_proofing_scan.py`: 10/10 pass.
- Full local suite: 95 tests run; 92 pass and three error.

The three errors all occur when the forward-evaluation harness creates authentication symlinks in
isolated Codex or judge homes. Windows returned `WinError 1314` because the current process lacks
symlink privilege. No manuscript-review, proofing, evaluator, or contract assertion failed.

### Change

- **APR-001 — Confirmed metadata defect:** `paper-review/agents/openai.yaml` has a 65-character
  `short_description`; the active Codex validator accepts 25–64. Shorten only that value and rerun
  the direct validator.
- **APR-002 — Maintainer portability gap:** isolated-auth tests require symlink privilege on
  Windows. Either declare the prerequisite, skip with a precise reason, or use a separately reviewed
  permission-limited adapter. Copying credentials should not become the silent fallback.

The quality lint also reported concentrated negative wording and a runtime over 300 lines. Those are
review signals, not supported architecture findings; target-owned tests show that many guardrails
protect real review and editing boundaries.

## 2. Zero-to-One Product Discovery

### Preserve

This repository is the strongest orchestration stress test in the set. The main skill owns stage
gates and user experience; local child-skill contracts produce bounded artifacts but cannot choose
the next stage or call one another. The Controller owns routing, while producer statuses remain
signals rather than decisions.

The Runtime Workbench stores current decision state instead of transcript history. Export manifests,
execution handoffs, revision traces, controller actions, and evidence maturity use schemas and
deterministic scripts. Public evaluation runs remain outside the installable runtime. These are
coherent ownership and state boundaries, not reasons to split the skill by file count.

### Tests

- Unit suite: 71/71 pass in 0.531 seconds.
- The tests cover schema integrity, workbench persistence, provider error handling, artifact
  manifests, revision boundaries, execution handoffs, and phase-three response checkers.
- Skill Creator Pro structural validation fails one metadata rule.

Integration tests were intentionally skipped because the repository declares
`DEEPSEEK_API_KEY` or `MIMO_API_KEY` as a prerequisite. Running a real provider call was unnecessary
to decide the local contract and metadata findings.

### Change

- **Z2O-001 — Confirmed metadata defect:** `agents/openai.yaml` has a 106-character
  `short_description`. Replace it with a 25–64 character description while keeping the longer branch
  detail in `SKILL.md` and `default_prompt`.

The 37 hard-negative lines reported by heuristic lint are not 37 findings. Many implement stage
purity, user authority, artifact eligibility, or controller ownership and are supported by the unit
suite.

## 3. Project Verifier

### Preserve

The roughly 30-line `SKILL.md` is a thin stable contract over four conditional stage references.
Its control plane keeps these dimensions separate:

- `phase_status`: workflow progress;
- `result_outcome`: evidence result;
- `execution_scope`: none, plan-only, pilot, or full;
- `claim_eligibility`: which claim the evidence may support.

The decision envelope binds material authorization, source revision, capabilities, limits, and
side-effect scope. Preflight validates without making the live model, scan, API, or target call. The
lean-core deletion record and V3 design history explain why these structures exist and which older
mechanisms were removed.

### Tests

- Skill Creator Pro structural validation: pass.
- Static `test_contract.py`: 11/11 pass.
- Full documented suite: 105 tests run; 27 pass, 73 fail, and five error on this Windows host.

The broad non-pass count is not evidence of 78 project-verification defects. Five errors come from
missing `bash`; most failures then share a `python3` command that resolves to the Windows Microsoft
Store alias instead of the active Python 3.12 interpreter. This is a maintainer-runtime and adapter
boundary. The static skill contract remains green.

### Change

- **PV-001 — Repository test-runtime gap:** state Bash plus a working `python3` as the supported
  maintainer runtime, or route Python subprocesses through the active interpreter and add a
  Windows-capable runner adapter. Until then, the README's unit-suite command is not portable to a
  normal Windows Python installation.

This finding does not justify collapsing the four-stage architecture or the independent state
dimensions. Those mechanisms are supported by design history and direct contract tests.

## 4. Immersive Motion UI

### Preserve

The skill's Core remains complete without the optional MotionSites Library. A 14-capability manifest
maps active modules to triggers, local references, dependencies, fallbacks, and verifiers. `audit`
is read-only; `redesign` protects working structure before targeted edits. Verification uses exact
`PASS`, `PASS WITH FINDINGS`, `FAIL`, and `NOT EXECUTED` outcomes.

That routing surface is large enough for a machine-readable manifest to earn its cost. The test did
not find evidence for replacing it with prose or turning the optional Library into a hard dependency.

### Tests

Twelve zero-dependency commands from the README were selected:

- standalone capability-manifest CLI: pass;
- data-UI suite: 15/15 pass;
- core package, capability-manifest tests, routing, industry, casebook, minimal showcases, browser
  evidence, commerce, specialty, and trigger suites: fail.

The ten failing commands share one path family. Sixteen JavaScript files use
`new URL(..., import.meta.url).pathname` before local path operations. On Windows this produces
percent-encoded or `/C:/...` forms that later resolve to paths such as `C:\C:\...`; valid files are
then reported missing. The failures must remain ten raw command outcomes but collapse to one causal
finding.

### Change

- **IMUI-001 — Confirmed cross-platform path defect:** use Node's
  `fileURLToPath(import.meta.url)` and derive local paths with `path.dirname` / `path.resolve` in all
  16 affected runtime and test files. Rerun the ten blocked suites afterward; their downstream
  behavior remains unproven until the shared path precondition is fixed.

The external lint found only the runtime occurrence in `verify-ui-evidence.mjs`; repository-wide
test execution was necessary to expose the full maintainer-tooling reach.

## What the test set changed in Skill Polisher

The four repositories produced four direct runtime refinements:

1. **Failure attribution before finding creation.** Classify target behavior, harness/adapter,
   environment precondition, and unavailable evidence separately.
2. **Causal collapse.** Preserve raw suite counts, but group repeated symptoms under the earliest
   evidenced common cause.
3. **Target-owned evidence first.** Contract and regression tests can prove why a guardrail exists;
   external lint remains supplementary.
4. **A maintenance decision brief.** Report `Preserve`, `Change`, and `Evidence limits` so learned
   architecture is visible even when the recommended patch is tiny.

No new mode, manifest, mandatory risk tier, or bundled test runner was added to Skill Polisher. The
existing workflow could express the reviews; it needed sharper attribution and reporting rules.

## Commands executed

```text
python quick_validate.py <each runtime skill>
python quality_lint.py <each runtime skill>
python -m unittest discover -s tests -q
python -m unittest discover -s tests/unit -q
python -m unittest discover -s skills/project-verifier/tests -p test_*.py -q
node scripts/validate-core-package.mjs --pretty
node skills/immersive-motion-ui/scripts/validate-capability-manifest.mjs --pretty
node tests/<selected-suite>/run-tests.mjs
```

Python suites were rerun outside the filesystem sandbox after sandbox temporary-directory ACLs
caused unrelated permission errors. Only the unsandboxed local results are reported above. The test
commands made no network calls and no source changes.

## Evidence limits and skipped checks

- No paid Codex, Claude, DeepSeek, or MIMO forward run was started.
- No live API, security target, browser production system, credentialed workflow, or external issue
  tracker was invoked.
- Existing recorded forward evaluations were inspected as historical evidence but not relabeled as
  current-model benchmarks.
- Only the current Windows environment was executed; Linux/macOS outcomes were not inferred.
- The test was run in the authoring session rather than a fresh independent Agent context.

These limits do not affect the two metadata length findings or the directly reproduced Windows
runtime findings. They do limit claims about cross-model invocation quality and post-fix behavior.
