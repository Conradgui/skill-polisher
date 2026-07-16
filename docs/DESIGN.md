# Skill Polisher Design Record

[简体中文](./DESIGN.zh.md)

This record explains the current maintenance lifecycle and the tradeoffs that keep it proportional.
Runtime instructions remain canonical in
[`SKILL.md`](../skills/skill-polisher/SKILL.md).

## Behavior contract

| Stage | Representative request | Observable success | Failure or handoff |
|---|---|---|---|
| Review | “Why does this existing skill misfire?” | A read-only, decision-ready packet with stable findings and evidence limits | Return a `NON_DURABLE` ledger when no evidence path is authorized |
| Decision | “Fix SP-002 now; defer SP-003.” | Finding-level decisions, order, scope, and baseline are explicit | Silence remains `PENDING`; changed scope refreshes approval |
| Polish | “Apply the approved SP-002 batch.” | Minimal diff, targeted evidence, omissions, achieved effect, and residual risk are recorded | Stop after the batch; no comprehensive Recheck claim |
| Recheck confirmation | “The candidate is committed.” | Ask whether to run complete Recheck and wait | A commit, handoff, or completed Polish is a signal, not consent |
| Recheck | “Run the complete Recheck now.” | Every ledger finding and affected contract surface receives current evidence | Remaining issues return to the decision gate |
| Release Drift | “Does the installed copy match the release?” | Source, version, CI, remote, and installed states remain separate | Release readiness requires a current runtime Recheck |
| Rebuild handoff | “This skill needs a new identity and architecture.” | Polisher supplies a behavior contract and protected invariants | Skill Creator Pro owns rebuilding and first release |

Near misses include reviewing ordinary application code, polishing a manuscript, and creating a new
skill from a repeated workflow. Those tasks belong to their domain workflow or Skill Creator Pro.

## Design decisions

### A lifecycle, not a mode picker

Review, Polish, Recheck, and Release Drift are valid entry points, but they are not interchangeable
authorities. A broad improvement request starts with Review. Polish consumes user-approved findings;
Recheck consumes a submitted candidate plus explicit confirmation; release readiness consumes a
current Recheck. A request naming an already approved finding can enter at Polish without repeating
unrelated Review work.

### Read-only Review with a reviewable artifact

Review keeps the target unchanged but must still produce a material the user can inspect. The
Maintenance Ledger is written only to an already authorized evidence location. Without one, the full
Markdown ledger is returned as `NON_DURABLE`; persisting evidence does not silently expand mutation
authority.

### One ledger, separate state dimensions

One Maintenance Ledger owns findings, user decisions, Polish batches, Recheck outcomes, and optional
release state. It appends history rather than copying facts into stage-specific documents. Decision,
implementation progress, and evidence outcome remain separate so `decision: ACCEPT_RISK` can coexist
with `recheck_outcome: OPEN`.

### Explicit Recheck confirmation

A commit, completed Polish batch, merge request, internal handoff, or release preparation makes
Recheck reasonable; it does not start Recheck. The agent asks one focused question and waits. A
current user message explicitly requesting Recheck already satisfies the gate. Confirmation is bound
to runtime identity and material scope, so a changed runtime requires confirmation again.

### Complete decision coverage, proportional tools

Recheck is comprehensive across every finding, modified behavior, preserved invariant, relevant
regression, and near miss. It is not an instruction to run every available test. Proportional rigor
still selects tools, but skipped and blocked checks remain visible and every finding receives an
outcome.

### Documentation reconciliation after Recheck

Recheck audits the documentation system but remains read-only. It summarizes the Review-to-Polish
closure and capabilities added, changed, or removed, then checks each statement against its existing
owner: README for current behavior, this record for rationale, Changelog for iteration history, tests
for executable contracts, and the Maintenance Ledger for detailed evidence. A gap becomes a finding;
an approved documentation-only repair preserves a runtime Recheck only when runtime content is
unchanged.

### Standalone drift audit versus release sequence

Release Drift remains independently useful for diagnosing source, publication, CI, or installation
mismatch. In a release path, however, it consumes a current Recheck for the exact runtime. A runtime
repair invalidates Recheck; a documentation-only or version-only repair reruns only affected release
gates.

### Independent axes and causal findings

Contract, system, evolution, and evidence answer different questions and keep separate findings. A
broad suite may emit many failures from one runtime, permission, or path adapter; raw counts remain,
but repeated symptoms collapse under the earliest evidenced cause.

### No bundled runner or capability manifest

The lifecycle is explicit but still small and tool-agnostic. A reference owns the ledger schema and
repository tests enforce key gates. No repeated runtime operation earns a bundled script, and no
module graph earns a capability manifest. Future behavioral evidence can change this decision.

## Evidence basis

The design applies two independent project authorities:

- [Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro) supplies behavior contracts,
  information hierarchy, forward testing, explicit decisions, and release engineering.
- [Matt Pocock-inspired Skill Writing](https://github.com/Conradgui/matt-pocock-inspired-skill-writing)
  supplies the twelve writing principles, durable artifact model, and proportional-evidence
  interpretation.

Four real skill systems supplied architecture evidence: `paper-review` for immutable ledgers and
stable IDs, `project-verifier` for separate state dimensions, `zero-to-one-product-discovery` for
stage-pure orchestration, and `immersive-motion-ui` for earned manifests and verifier boundaries.
The expanded [real-world evaluation](./REAL_WORLD_EVALUATION.md) records the commands and evidence.

These projects remain independent. This repository does not claim that Matt Pocock, OpenAI, or the
study repositories define or endorse Skill Polisher's workflow.
