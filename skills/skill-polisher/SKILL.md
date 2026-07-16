---
name: skill-polisher
description: Review and improve existing agent skills through an evidence-led maintenance lifecycle. Use when Codex needs to diagnose why an existing skill misfires, produce a decision-ready review ledger, apply user-approved findings, run a user-confirmed final recheck, or audit drift across source, published, and installed copies.
---

# Skill Polisher

Treat an existing skill as a living system. Preserve learned invariants, change only findings the user
approves, and keep Review, Polish, Recheck, and Release Drift connected through one Maintenance
Ledger. Apply **proportional rigor**: use the minimum sufficient evidence for the current decision.

Route a new capability, new identity, or full rebuild to `Skill Creator Pro`. Keep remote
publication, credentials, and live-system effects outside local maintenance authority.

## 1. Resolve the target, entry point, and authority

Resolve the target from the user's path or repository, then the active workspace or installed
skills. Inspect applicable workspace instructions and unrelated user changes before acting. Ask one
focused question only when a missing target, priority, evidence location, or authority decision
would change the outcome.

Enter the lifecycle at the earliest valid stage:

- **Review** is the default for diagnosis, architecture, quality, or a broad request to improve an
  unreviewed skill.
- **Polish** requires a decision-ready Review finding and explicit user approval for its ID and
  scope. A request naming an already confirmed finding may enter here after validating its ledger.
- **Recheck** requires a completed candidate and explicit user confirmation. A current request to
  run Recheck is itself confirmation; otherwise ask `Run the complete Recheck now?` and wait.
- **Release Drift** may run alone as a read-only state audit. In a release path, require a current
  Recheck for the runtime revision before claiming release readiness.

Treat the user's observed symptom as evidence and their proposed cause as a hypothesis. Bind every
approval and Recheck confirmation to the inspected source revision and material scope. A changed
runtime makes them stale.

**Done when:** the target, entry point, baseline revision, mutation boundary, and unresolved user
decisions are explicit.

## 2. Review the living contract

Set an evidence boundary from user impact, affected branches and callers, state or authorization,
external effects, reversibility, uncertainty, and released-user dependence. Start with the cheapest
direct evidence and expand only when another check can change the diagnosis, recommendation, or
supported claim.

Read sources in this order until the boundary is satisfied:

1. `SKILL.md` and harness-native invocation or UI metadata;
2. directly referenced scripts, references, assets, templates, or adapters;
3. callers, routers, manifests, installed copies, and distribution boundaries;
4. tests, fixtures, traces, issue reports, and the user's failure evidence;
5. changelogs, history, ADRs, rejected scope, deprecated designs, and migrations.

Recover the outcome, trigger branches, near misses, inputs and state, outputs and side effects,
authority gates, success evidence, failure behavior, and ownership. Before simplifying a nontrivial
mechanism, identify the requirement, failure, or decision that introduced it. Classify it as:

- a **learned invariant** when it protects demonstrated behavior or history;
- **sediment** only when evidence shows it is duplicated, superseded, unreachable, or unenforced;
- an **evidence limit** when history cannot settle the question.

Evaluate four axes separately: **Contract**, **System**, **Evolution**, and **Evidence**. Prefer
target-owned contract and regression evidence over external lint. Attribute every non-pass result
to target behavior, the harness or adapter, an unmet environment precondition, or unavailable
evidence, then collapse repeated symptoms under the earliest evidenced cause while retaining raw
counts.

Read [references/maintenance-ledger.md](references/maintenance-ledger.md) before completing Review.
Create or update one Maintenance Ledger in an already authorized evidence location. If Review has no
authorized writable location, return the complete Markdown ledger in the response and mark it
`NON_DURABLE`; keep the target unchanged merely to persist Review.

End with a user-reviewable Review packet containing **Preserve**, stable findings, evidence limits,
checks performed, checks skipped, and a decision table. Each finding includes its axis, claim,
evidence, impact, confidence, smallest justified action, and recommendation.

**Done when:** every conclusion has direct evidence or an uncertainty label, every finding has a
stable ID, and the user can decide what to fix without reconstructing the review from chat.

## 3. Stop at the Review decision gate

Ask the user to set each actionable finding's `decision` to `FIX_NOW`, `DEFER`, `ACCEPT_RISK`, or
`REJECT`, and to choose the order or batch. Leave silence as `PENDING`. Keep `decision`,
`polish_state`, and `recheck_outcome` as separate dimensions.

Edit only findings in the proposed batch with explicit `FIX_NOW` approval.
If the baseline revision or material scope changed, refresh affected evidence and ask for the
decision again.

**Done when:** the ledger records the user's explicit decision, approved scope, sequence, and source
revision. Stop and wait when any of these is pending.

## 4. Polish only the approved batch

Read [references/polish-and-recheck.md](references/polish-and-recheck.md) before editing. Preserve
unrelated changes and ledger invariants. Fix the earliest causal failure with the smallest coherent
patch. Update callers, routers, adapters, tests, metadata, or documentation only when the approved
behavior makes them stale.

Run **targeted verification** for the approved batch: reproduce the original regression, exercise
the affected branch and a near miss, inspect the diff, and expand only when impact or uncertainty
warrants it. Targeted verification supports the Polish claim; it is not Recheck.

Update the Maintenance Ledger and deliver a Polish packet that states:

- which finding IDs were attempted and their resulting `polish_state`;
- what changed, how it changed, and which files changed;
- what was intentionally not changed and why;
- targeted checks and results, skipped checks, preserved invariants, achieved effect, and residual
  risk.

Stop after each approved batch so the user can inspect the packet. When the candidate may be
complete, ask `Run the complete Recheck now?` and wait. Treat a commit, silence, or completed Polish
as pending confirmation.

**Done when:** every approved ID maps to a diff and evidence or an explicit incomplete result with
its blocker recorded, the packet is reviewable, and no comprehensive Recheck has been claimed.

## 5. Recheck only after explicit confirmation

Read [references/polish-and-recheck.md](references/polish-and-recheck.md) again for the Recheck
contract. Confirm that the user's authorization still matches the candidate revision. If it does
not, ask again before starting.

Recheck the complete decision surface rather than rerunning every available test: account for every
ledger finding, every modified behavior and preserved invariant, the relevant regression surface,
near misses, target-owned validation, and any evidence needed for the requested completion claim.
Report non-relevant or unavailable checks as skipped instead of silently omitting them.

Reconcile the documentation system before concluding, without editing it during Recheck. Summarize
the Review findings, Polish resolutions, Recheck closure, and capabilities added, changed, or
removed. Check each summary against its existing owner: README for current user-facing behavior,
design records for rationale, changelog for iteration history, tests for executable contracts, and
the Maintenance Ledger for detailed evidence. Record stale, missing, or duplicated surfaces as
findings and return them to the decision gate.

Keep Recheck read-only. Record each finding's `recheck_outcome` with current evidence; preserve IDs
and keep user decisions separate. Add a new finding only for a distinct causal issue. If a remedy is
needed, return to the Review decision gate and require new Polish approval.

Deliver a Recheck packet with the candidate revision, confirmation source, per-finding outcomes,
regression results, documentation reconciliation, evidence limits, and overall readiness for the
user's stated purpose.

**Done when:** every ledger finding and affected contract surface is accounted for, the candidate
revision is unchanged, and readiness is supported without converting accepted risk into resolution.

## 6. Audit Release Drift when relevant

Read [references/release-drift.md](references/release-drift.md) for a standalone drift audit or when
the user asks to share, install, or publish an existing skill. Keep source, version intent, remote
publication, CI, and installed state separate.

In a release path, consume the current Recheck result before claiming readiness. If drift repair
changes runtime behavior, mark Recheck stale and return to its confirmation gate. If only release
metadata or human documentation changes, rerun the affected release gates without pretending the
runtime changed.

**Done when:** the result is a read-only drift matrix, an explicitly authorized repair, or a release
handoff with no state or authority silently inferred.
