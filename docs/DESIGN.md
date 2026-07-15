# Skill Polisher Design Record

[简体中文](./DESIGN.zh.md)

This record explains why Skill Polisher has its current boundary and why several plausible mechanisms
are intentionally absent. Runtime instructions remain canonical in
[`SKILL.md`](../skills/skill-polisher/SKILL.md).

## Behavior contract

| Branch | Representative request | Observable success | Failure or handoff |
|---|---|---|---|
| Review | “Why does this existing skill misfire?” | Evidence-backed findings or an explicit no-finding result; no mutation | Ask only if the target or a decision-changing requirement is unavailable |
| Polish | “Fix the confirmed routing defect in this skill.” | Minimal diff restores the affected contract and preserves invariants | Stop before remote, live, or newly expanded effects |
| Recheck | “Recheck SP-002 after this patch.” | Stable finding ID receives an evidence-backed current status | Report `BLOCKED` when the original standard cannot be reconstructed |
| Release drift | “Does the installed copy match the release?” | Source, version, CI, remote, and installed states are distinguished | Narrow the claim when a relevant state cannot be observed |
| Rebuild handoff | “This skill needs a new identity and architecture.” | Polisher supplies a behavior contract and protected invariants | Skill Creator Pro owns rebuilding and first release |

Near misses include reviewing ordinary application code, polishing a manuscript, and creating a new
skill from a repeated workflow. Those tasks belong to their domain workflow or Skill Creator Pro.

## Design decisions

### Implicit invocation

Users often report “this skill keeps misfiring” without knowing the product name. Implicit invocation
earns its context cost because the description is restricted to existing agent skills and names each
genuine maintenance branch.

### Read-only default

Diagnosis and mutation are different authorities. Review requests produce evidence without changing
the target. A direct local fix request selects Polish, while release, credentials, and live effects
remain separately authorized.

### Proportional rigor without mandatory tiers

Risk is multi-dimensional: one authorization line can matter more than a large documentation edit.
The workflow therefore asks whether another check can change the diagnosis, action, or claim instead
of assigning every task a ceremonial T0–T3 package. This is a cross-cutting discipline, not a new
writing principle.

### Independent axes without a composite score

Contract, system, evolution, and evidence answer different questions. Combining them into one score
would let strong documentation hide a broken caller or let extensive tests hide a wrong outcome.
Findings keep their axis and evidence.

### Causal findings instead of failure-count theater

A broad suite may emit many failures from one missing runtime, permission, or path adapter. Skill
Polisher preserves raw counts but attributes each non-pass result before creating findings, then
collapses repeated symptoms under the earliest evidenced common cause. This prevents environmental
noise from outranking the behavior and architecture under review.

### Preserve, change, and evidence limits

Mature-skill maintenance needs an explicit preservation decision, not only a defect list. The report
therefore names learned invariants to preserve, evidence-backed changes worth making, and limits that
bound the supported claims. This makes a no-change decision as auditable as a patch recommendation.

### No bundled scripts or capability manifest

The current workflow is linear and tool-agnostic. Existing platform validators already check skill
structure, while evidence collection varies by target repository. No repeated deterministic operation
currently earns a new script, and no modular routing graph earns a manifest. Forward evidence can
change this decision later.

## Evidence basis

The design applies two independent project authorities:

- [Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro) supplies the behavior-contract,
  information-hierarchy, forward-testing, and first-release workflow.
- [Matt Pocock-inspired Skill Writing](https://github.com/Conradgui/matt-pocock-inspired-skill-writing)
  supplies the twelve writing principles and proportional-evidence interpretation.

Three real skill systems supplied architecture studies:

| System | Learned invariant carried into Skill Polisher |
|---|---|
| `immersive-motion-ui` | A capability graph, fallback, and verifier may be earned architecture rather than excess complexity |
| `project-verifier` | Progress, outcome, execution scope, and claim eligibility must not be collapsed |
| `paper-review` | Review and mutation require different modes; edits may need an invariant ledger and rechecks need stable IDs |

A fourth study, `zero-to-one-product-discovery`, added evidence for controller-owned routing,
stage-pure orchestration, narrow persistent state, and machine-validated artifact boundaries. The
expanded [real-world evaluation](./REAL_WORLD_EVALUATION.md) records the commands and feedback loop.

These studies also exposed a weakness in snapshot-only review: incidental Windows findings can be
real without being the highest-value architectural conclusion. Skill Polisher explicitly ranks
behavior and architecture first unless platform behavior breaks a support claim.

The projects remain independent. This repository does not claim that Matt Pocock, OpenAI, or the
four study repositories define or endorse Skill Polisher's workflow.
