# Forward Evaluation

[简体中文](./FORWARD_EVALUATION.zh.md)

This evaluation asks whether Skill Polisher applies its intended decision discipline to small and
mature skills. It is not a quality ranking of the study repositories, and the repositories remained
unmodified.

## Evidence boundary

The authoring session applied the runtime workflow to raw repository artifacts and ran deterministic
structural checks. It did not use a fresh independent agent, mutate a study repository, replay broad
cross-platform suites, or query current remote CI. Invocation transfer and the full Polish/Recheck
execution branches therefore remain pre-release evidence gaps.

Source snapshots:

| Repository | Reviewed revision |
|---|---|
| [`immersive-motion-ui-skill`](https://github.com/Conradgui/immersive-motion-ui-skill/tree/51f5adb9949c5c8731011637958fcdfc82128fd3) | `51f5adb9949c5c8731011637958fcdfc82128fd3` |
| [`project-verifier-skill`](https://github.com/Conradgui/project-verifier-skill/tree/df0bb00c06eae2a088c83ce45e51d64bbeb678f4) | `df0bb00c06eae2a088c83ce45e51d64bbeb678f4` |
| [`Academic-Paper-Review-Skill`](https://github.com/Conradgui/Academic-Paper-Review-Skill/tree/9f3288f7a13e25400a8ff0c00eeb16270e37fe98) | `9f3288f7a13e25400a8ff0c00eeb16270e37fe98` |
| [`skill-creator-pro`](https://github.com/Conradgui/skill-creator-pro/tree/eb23656e56ea3555599a6c5278a8b5834dc56b6d) | `eb23656e56ea3555599a6c5278a8b5834dc56b6d` |

Each study checkout was clean at the reviewed revision.

## Results

### 1. Small coherent skill: stop without ceremony

The deliberately small `release-note-cleaner` fixture passed Skill Creator Pro's structural
validator and quality lint with zero warnings. Its outcome, protected facts, edit boundary, and
observable completion criterion are already explicit.

**Decision:** no finding. The review stopped after the directly owned runtime and metadata. A
manifest, script suite, architecture document, or broad forward matrix would not change the decision.

This is the primary anti-overengineering case.

### 2. Immersive Motion UI: recognize earned modular architecture

The runtime contract keeps Core usable without its optional Library, separates read-only `audit`
from modifying `redesign`, and uses exact verification outcomes. Its capability manifest maps 14
conditional modules to references, dependencies, fallbacks, and verifiers.

**Decision:** treat the capability graph as a learned invariant, not automatic sprawl. The routing
surface is large enough that the manifest makes dependency and fallback drift checkable. No
high-confidence architecture change was justified by the targeted review.

### 3. Project Verifier: preserve independent state dimensions

The current skill and artifact contract keep `phase_status`, `result_outcome`, `execution_scope`,
and `claim_eligibility` separate. The V3 design record explains why authorization moved from whole
plan hashes to a material decision envelope, while preflight remains no-call. The lean-core deletion
record shows that old mechanisms were evaluated rather than retained by default.

**Decision:** these are learned control-plane invariants. Historical workbench material outside the
installable skill is evidence of evolution, not runtime sediment. The targeted review did not justify
collapsing the state model or deleting the history.

### 4. Academic Paper Review: protect mode and recheck contracts, isolate one local defect

`paper-review` separates default review, delta review, reference audit, and authorial polishing.
Its tests enforce stable finding IDs, exact recheck statuses, and evidence-bounded blind evaluation.
Those mechanisms protect scientific claims from an editing pass and make rechecks traceable.

One independent structural defect was reproduced:

- **SP-001 — Confirmed metadata defect:** `paper-review/agents/openai.yaml` has a 65-character
  `short_description`; the active validator accepts 25–64 characters. The runtime skill therefore
  fails structural validation on this field.

**Smallest justified action:** shorten that one metadata value and rerun the direct validator. The
review found no evidence that this local defect requires restructuring the 337-line runtime skill.
The study repository remained read-only.

### 5. Release drift: distinguish local source and installed state

The Skill Creator Pro runtime folder and globally installed copy each contained 16 files. Relative
path plus SHA-256 comparison produced zero drift records at source revision
`eb23656e56ea3555599a6c5278a8b5834dc56b6d`.

**Supported claim:** the observed local source and installed copies match byte-for-byte.

**Not claimed:** current remote CI, tag, GitHub release, or a fresh installer replay. Those states
were not queried in this evaluation.

### 6. Local installation: verify the documented command

`npx skills add . --skill skill-polisher --yes` ran with `skills@1.5.17`. The installer validated
the local path, discovered exactly one skill, selected `skill-polisher`, and completed the project-
local installation. The five installed runtime files matched the five source files by relative path
and SHA-256.

Installer-generated `.agents/` content and the absolute-path `skills-lock.json` are local environment
state and are excluded from repository version control.

## Checks performed

- Skill Creator Pro `quick_validate.py` on Skill Polisher, the simple fixture, and all three mature
  runtime skills.
- Skill Creator Pro `quality_lint.py` on Skill Polisher and the simple fixture.
- Direct inspection of runtime contracts, harness metadata, conditional references, manifests,
  workbench design and deletion records, and representative tests.
- Clean-tree and revision checks for each study repository.
- Relative-path SHA-256 comparison between Skill Creator Pro source and installed runtime folders.
- Real `npx skills` discovery, local installation, and source-to-installed hash comparison for Skill
  Polisher.

## Checks intentionally skipped

- Broad target test suites: no target behavior was changed, and their previous platform results
  could not change the architecture decisions in this review.
- Cross-platform replay: this iteration changes only the new Markdown/YAML skill and adds no runtime
  script or platform claim.
- Live Polish or release publication: the study repositories were review-only inputs, and remote
  mutation was outside the task.
- Fresh-agent trigger and near-miss runs: no independent execution context was used in this pass.

The next release gate should prioritize the last item, then execute one authorized minimal Polish
fixture and one Recheck fixture. Repeating broad suites before those behavior branches would add
cost without closing the largest current evidence gap.
