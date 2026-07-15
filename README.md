# Skill Polisher

> Refine agent skills for real work—not lint-shaped scorecards.

English | [简体中文](./README.zh.md)

Skill Polisher is an evidence-led, Codex-native workflow for reviewing and refining existing agent
skills as living systems. It reconstructs behavior, ownership, evolution, tests, and release state;
protects learned invariants; and applies only the smallest authorized change the evidence justifies.

**Why this layer matters:** a skill maintainer determines whether operational knowledge compounds
through iteration or is erased by surface-level cleanup.

Review is read-only by default. A direct request to fix or improve the named local skill selects the
Polish branch; remote publication, credentials, live effects, and a new identity remain separate
authorities.

## What problem does it solve?

Existing skills are different from new skills. Mature skills contain callers, state, tests, release
copies, and mechanisms introduced after real failures. A snapshot-only review can produce a long
list while missing why the system works.

| Common review failure | Risk to a mature skill | Skill Polisher response |
|---|---|---|
| Judge only the current `SKILL.md` | Learned gates and adapters look like accidental complexity | Reconstruct callers, artifacts, history, tests, and release state |
| Treat every lint warning as a defect | Safety language and branch contracts become noisy false positives | Prefer target-owned contract evidence; use lint as supplementary evidence |
| Count every failed test independently | One missing runtime or path adapter becomes dozens of “bugs” | Attribute non-pass results and collapse shared symptoms to one causal finding |
| Optimize for maximum test coverage | Small changes consume disproportionate time and tools | Use the minimum evidence capable of changing the diagnosis, action, or claim |
| Accept the user's proposed cause as final | The patch may solve the explanation rather than the observed problem | Treat the symptom as evidence and the proposed cause as a hypothesis |
| Report only problems | Maintainers cannot see what architecture must survive the patch | Report `Preserve`, `Change`, and `Evidence limits` |
| Let review silently become rewriting | Scope and authority expand without a deliberate decision | Keep Review read-only; make Polish, Recheck, and rebuild handoff explicit |
| Treat local validity as release validity | Source, metadata, docs, CI, publication, and installation drift apart | Audit each release state separately |

The goal is not to make every review large. It is to make every consequential maintenance decision
traceable and proportionate.

## Scope: Creator Pro vs. Skill Polisher

Skill Polisher is the maintenance counterpart to
[Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro). Their boundary is deliberately
narrow:

| Boundary | Skill Creator Pro | Skill Polisher |
|---|---|---|
| Starting point | Repeated workflow, new capability, deliberate fork, or rebuild under a new identity | Existing skill with an identity, real artifacts, and behavior history |
| Primary question | What behavior contract should the new skill implement, and how should it first ship? | Why does the current skill behave as it does, what should survive, and what is worth changing? |
| Primary output | New validated, forward-tested, installable skill and first release | Evidence-backed review and optional authorized minimal patch |
| Mutation default | Build the new artifact | Read-only review |
| Evolution history | Source evidence when rebuilding or forking | Core evidence for learned invariants versus sediment |
| Release ownership | Initial packaging and publication | Drift audit and maintenance of an existing release |

When refinement reveals that a new identity or full rebuild is required, Polisher hands a behavior
contract and preserved invariants to Creator Pro. It does not disguise a rebuild as a patch.

## From snapshot lint to living-system maintenance

Skill Polisher follows the “skills for real engineers” direction: user control, feedback, evidence,
architecture, and maintainability matter more than a prompt that looks comprehensive.

A mature review should answer:

- What outcome and trigger branches does this skill actually own?
- Which caller, router, adapter, state artifact, or release copy depends on that contract?
- Which mechanism protects a prior failure or hard-won decision?
- Which layer is truly duplicated, superseded, unreachable, or no longer enforced?
- Is a failed check evidence about the skill, the test harness, the environment, or missing access?
- What is the smallest evidence set that can still change the decision?
- What should be preserved even when no patch is justified?

## Twelve principles that shape Skill Polisher

Skill Polisher applies the independent twelve-part synthesis in
[Matt Pocock-Inspired Skill Writing Guidelines](https://github.com/Conradgui/matt-pocock-inspired-skill-writing).
This is not an official list authored or endorsed by Matt Pocock.

| # | Principle | Applied to maintenance as |
|---|---|---|
| 1 | Optimize for process predictability | Stable source order, evidence rules, stop conditions, and handoff paths |
| 2 | Separate primitives from orchestration | Review ownership, callers, routers, adapters, and artifacts independently |
| 3 | Treat the description as a branch index | Reconstruct intended triggers and near misses before judging prose |
| 4 | Compress behavior with leading words | Use proportional rigor, learned invariant, sediment, and causal collapse precisely |
| 5 | End consequential steps with observable criteria | Require checkable completion for scope, evidence, findings, and patches |
| 6 | Put cheap fail-fast gates before expensive work | Resolve target, authority, revision, and direct validators first |
| 7 | Separate discoverable facts from user decisions | Inspect files and history; ask only for choices, priority, or authority |
| 8 | Persist state in purpose-built artifacts | Respect ledgers, manifests, workbenches, receipts, and stable finding IDs |
| 9 | Disclose branch-specific context progressively | Load modification and release-drift references only when those branches fire |
| 10 | Isolate independent judgment axes | Keep contract, system, evolution, and evidence conclusions distinct |
| 11 | Prompt the positive and design the negative space | Name preservation, mutation, approval, and stopping boundaries explicitly |
| 12 | Prune continuously | Remove proven sediment without deleting learned safeguards |

**Proportional rigor** is a cross-cutting discipline over these principles, not a thirteenth item:

> Rigor is not maximum effort. It is the minimum sufficient evidence for the risk of the decision.

## What changed?

### 1. A living behavior contract

Review starts from the outcome, trigger branches, near misses, inputs and state, outputs and side
effects, authority gates, success evidence, and failure behavior. It then maps each shared behavior,
artifact, adapter, caller, route, and release claim to one owner.

### 2. Evolution-aware diagnosis

Before simplifying a nontrivial mechanism, Polisher looks for the requirement, failure, decision,
test, or migration that introduced it. A demonstrated safeguard is a **learned invariant**. Content
is **sediment** only when evidence shows that it is duplicated, superseded, unreachable, or no longer
enforced. Missing history becomes an evidence limit rather than permission to guess.

### 3. Independent review axes

The review preserves four separate judgments:

- **Contract:** invocation, outcome, branches, authority, and completion.
- **System:** ownership, callers, state, gates, adapters, and release boundaries.
- **Evolution:** learned invariants, sediment, compatibility constraints, and rejected scope.
- **Evidence:** tests, traces, reproducibility, claim eligibility, and unsupported assertions.

No composite score is allowed to let strong documentation hide a broken caller or let a large test
suite hide the wrong product outcome.

### 4. Failure attribution and causal collapse

Every non-pass check is first attributed to target behavior, a harness or adapter, an unmet
environment precondition, or unavailable evidence. Raw test counts remain visible, but repeated
symptoms are grouped under the earliest evidenced common cause.

This prevents one missing `bash`, one Windows symlink privilege, or one unsafe path conversion from
becoming dozens of fictional architecture findings.

### 5. Proportional verification

Risk is based on user impact, affected branches and callers, state or authorization, external side
effects, reversibility, uncertainty, and released-user dependence—not changed line count.

Start with the cheapest direct evidence. Expand only when another check can change the diagnosis,
edit, or claim. Stop when the original behavior is evidenced, high-impact uncertainty is resolved,
and another plausible check cannot change the decision. State skipped checks when they narrow the
supported claim.

### 6. Review, Polish, and Recheck boundaries

| Mode | Outcome | Mutation |
|---|---|---|
| **Review** | Diagnose behavior, architecture, evolution, and evidence | Read-only |
| **Polish** | Apply the smallest evidence-backed improvement | Explicit local request required |
| **Recheck** | Reassess stable findings against a changed artifact | Read-only unless another fix is requested |
| **Release drift** | Compare runtime, repository, metadata, version, CI, publication, and installation | Read-only by default |

Polish protects unrelated user changes and records only the invariants the edit can actually harm. A
small metadata fix needs a short invariant note, not a ceremonial ledger; high-consequence state,
claims, identifiers, citations, or authorization may justify a durable ledger.

### 7. A maintenance decision brief

Every substantial result opens with:

- **Preserve:** learned invariants and coherent boundaries that should survive;
- **Change:** evidence-backed findings worth their delivery cost;
- **Evidence limits:** missing checks or access that narrow the claim.

Recheckable findings receive stable IDs, direct evidence, impact, confidence, and the smallest
justified action. A no-change conclusion is valid when the evidence supports it.

### 8. Release drift as observable state

Polisher reports runtime source, harness metadata, repository contract, version intent, remote
publication, CI, and installed copies separately. A clean local tree does not prove publication; a
tag does not prove installation; an install does not prove byte identity with current source.

## Real-world test set

Four public repositories were pinned to exact revisions, kept read-only, and tested in proportion to
their own contracts:

| Repository | Architecture preserved | Actual test result | Actionable finding |
|---|---|---|---|
| [`Academic-Paper-Review-Skill`](https://github.com/Conradgui/Academic-Paper-Review-Skill) | Review/polish modes, dual judgment axes, immutable ledger, stable delta IDs | Contract 28/28; proofing 10/10; full suite 92/95 with three Windows symlink errors | 65-character metadata; permission-aware isolated-auth testing |
| [`zero-to-one-product-discovery`](https://github.com/Conradgui/zero-to-one-product-discovery) | Controller routing, stage purity, child-skill contracts, narrow workbench state | Unit suite 71/71 | 106-character metadata |
| [`project-verifier-skill`](https://github.com/Conradgui/project-verifier-skill) | Four-stage control plane, decision envelope, separate state dimensions | Static contract 11/11; full suite 27/105 on Windows | Declare or adapt Bash and `python3` maintainer runtime |
| [`immersive-motion-ui-skill`](https://github.com/Conradgui/immersive-motion-ui-skill) | Core/Library boundary, 14-capability manifest, audit/redesign, evidence tokens | Manifest CLI and data UI pass; ten selected commands share one Windows path root cause | Replace 16 unsafe file-URL pathname conversions |

The test set directly sharpened Skill Polisher's failure attribution, causal collapse, target-owned
evidence priority, and `Preserve / Change / Evidence limits` brief. It did not justify a new mode,
manifest, mandatory risk tier, or bundled test runner.

Read [Real-World Evaluation](./docs/REAL_WORLD_EVALUATION.md) for pinned revisions, commands,
finding IDs, raw counts, causal grouping, and skipped checks.

## Install

### Option A: Agent Skills installer

```bash
npx skills@latest add Conradgui/skill-polisher
```

Select `skill-polisher` and Codex when prompted.

### Option B: Codex Skill Installer

Ask Codex:

```text
Use $skill-installer to install the skill at
https://github.com/Conradgui/skill-polisher/tree/main/skills/skill-polisher
```

### Option C: Manual copy

Clone or download the repository, then copy `skills/skill-polisher` into
`$CODEX_HOME/skills/skill-polisher`, or into
`~/.codex/skills/skill-polisher` when `CODEX_HOME` is unset. Restart or begin a new Codex turn after
installation so the skill is discovered.

## Use

Review without editing:

```text
Use $skill-polisher to review this existing skill, explain its architecture and evolution, and do
not edit it.
```

Apply a confirmed minimal fix:

```text
Use $skill-polisher to fix finding SP-002 in this local skill, preserve the documented invariants,
and validate only the affected behavior and near miss unless wider risk emerges.
```

Recheck stable findings:

```text
Use $skill-polisher to recheck SP-001 and SP-003 against the current revision and preserve their IDs.
```

Audit release drift:

```text
Use $skill-polisher to compare this skill's source, metadata, published state, CI, and installed copy.
```

If the task is to create a new capability or rebuild under a new identity, use
`$skill-creator-pro` instead.

## Repository structure

```text
skill-polisher/
├── README.md
├── README.zh.md
├── CONTRIBUTING.md
├── CONTRIBUTING.zh.md
├── CHANGELOG.md
├── VERSION
├── LICENSE
├── NOTICE.md
├── .github/workflows/validate.yml
├── docs/
│   ├── DESIGN.md
│   ├── DESIGN.zh.md
│   ├── REAL_WORLD_EVALUATION.md
│   └── REAL_WORLD_EVALUATION.zh.md
├── tests/
│   ├── BEHAVIOR_CASES.md
│   ├── test_validate_repository.py
│   └── fixtures/release-note-cleaner/
├── scripts/
│   └── validate_repository.py
└── skills/skill-polisher/
    ├── SKILL.md
    ├── license.txt
    ├── agents/openai.yaml
    └── references/
        ├── polish-and-recheck.md
        └── release-drift.md
```

The installable folder contains only runtime material. Human documentation, design evidence, and
test fixtures remain outside it. English runtime files are the semantic source of truth; Chinese
human documentation mirrors project information without adding runtime rules.

## Compatibility and current evidence

- Primary target: Codex Skill format and `agents/openai.yaml`.
- Invocation: implicit for ordinary existing-skill diagnosis and maintenance requests.
- Runtime dependencies: none beyond the active agent's normal repository and test tools.
- Current runtime size: one 130-line-class `SKILL.md` plus two conditional references; no bundled
  script or capability manifest is currently justified.
- Local structure and quality lint: pass with zero warnings after the current iteration.
- Release candidate: `v0.1.0`; Windows and Ubuntu CI run the same repository and skill checks.
- Local `npx skills` installation: verified with one discovered skill and zero source-to-installed
  drift.
- Real-world evidence: four pinned repositories on the current Windows environment.
- Pending until the release gates complete: public remote, remote CI result, tag, GitHub Release,
  and fresh-remote installation.
- Not claimed by this release: macOS execution or fresh-independent-agent invocation transfer.

## Attribution and independence

Skill Polisher is an independent project informed by
[Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro) and the independent
[Matt Pocock-Inspired Skill Writing Guidelines](https://github.com/Conradgui/matt-pocock-inspired-skill-writing).
It is not official OpenAI or Matt Pocock material, and no endorsement is implied.

The four public test repositories remain independent projects. Their use as read-only evidence does
not imply that they define or endorse Skill Polisher. See [NOTICE.md](./NOTICE.md).

## License

MIT. See [LICENSE](./LICENSE).
