---
name: skill-polisher
description: Review, diagnose, and refine existing agent skills as living systems. Use when Codex needs to explain why an existing skill misfires, assess its architecture or evolution, apply an explicitly requested minimal improvement, recheck prior findings, or audit drift across source, published, and installed copies.
---

# Skill Polisher

Review existing skills as living systems, then make only evidence-backed changes within the user's
authority. Apply **proportional rigor**: use the minimum sufficient evidence for the risk of the
decision. Keep review read-only by default.

Route a new capability, a new skill identity, or a full rebuild to `Skill Creator Pro`. This skill
owns diagnosis and refinement after a skill already has an identity and behavior history.

## Process

### 1. Fix the mode, target, and authority

Resolve the target from the user's path or repository first, then the active workspace or installed
skills. Ask one focused question only when competing targets or missing user decisions would change
the outcome, scope, authority, priority, or acceptance criteria.

Choose one mode:

- **Review**: inspect and report; use for audit, diagnosis, architecture, or quality requests.
- **Polish**: modify the named local skill when the user directly asks to fix, update, or improve it.
- **Recheck**: reassess earlier findings against a changed artifact.

Treat the user's observed symptom as evidence. Treat their explanation of the cause as a hypothesis
to verify independently. A local Polish request does not authorize remote publication, live-system
effects, credential use, or a new skill identity.

**Done when:** the target, mode, requested outcome, mutation boundary, and any unresolved user
decision are explicit.

### 2. Set a proportional evidence boundary

Estimate the decision risk from user impact, affected branches and callers, state or authorization,
external side effects, reversibility, uncertainty, and whether released users depend on the skill.
Start with the cheapest direct evidence. Expand only when another check can change the diagnosis,
edit, or claim.

For a narrow local issue, inspect the affected contract and test that branch plus a near miss. For a
behavioral, stateful, cross-caller, or released-system issue, include the relevant architecture,
history, regression evidence, and representative forward behavior. Let demonstrated risk earn any
named tier, manifest, large plan, or full suite.

Stop when:

- the behavior claim has direct evidence;
- the reported regression or relevant branch has been checked;
- no unresolved high-impact uncertainty can change the conclusion; and
- the next plausible check cannot change the action or supported claim.

Record a skipped check when its absence narrows what the review can claim.

**Done when:** every planned check can affect a decision, and the stopping condition is observable.

### 3. Reconstruct the living contract

Inspect applicable workspace instructions first. Read sources in this order, stopping when the
evidence boundary is satisfied:

1. `SKILL.md` and harness-native invocation or UI metadata;
2. directly referenced scripts, references, assets, templates, or adapters;
3. callers, routers, manifests, installed copies, and distribution boundaries;
4. tests, fixtures, traces, issue reports, and the user's original failure evidence;
5. changelogs, history, ADRs, rejected scope, deprecated designs, and migration records.

Recover the outcome, trigger branches, near misses, inputs and state, outputs and side effects,
authority gates, success evidence, and failure behavior. Map each shared behavior, artifact, adapter,
route, and release claim to one owner.

For an iterated skill, distinguish:

- a **learned invariant**: a mechanism that protects a demonstrated requirement or prior failure;
- **sediment**: duplicated, superseded, unreachable, or no-longer-enforced material.

Before recommending deletion, simplification, or consolidation of a nontrivial mechanism, find the
requirement, failure, or decision that introduced it. When that evidence is unavailable, report the
uncertainty instead of labeling the mechanism sediment.

Absence of history is an evidence limit, not a defect. A small coherent skill does not need the
layers of a large collection.

**Done when:** the intended behavior and ownership can be stated from evidence, and every suspected
invariant or sediment layer has a concrete source or an explicit uncertainty label.

### 4. Evaluate independent axes

Keep these judgments separate rather than collapsing them into one score:

- **Contract**: invocation, outcome, branches, near misses, authority, and completion criteria.
- **System**: ownership, callers, state, gates, adapters, and release boundaries.
- **Evolution**: learned invariants, sediment, compatibility constraints, and rejected scope.
- **Evidence**: tests, traces, reproducibility, claim eligibility, and unsupported assertions.

Reproduce the user's symptom when safe and decision-relevant. Test the affected branch and one
plausible near miss before widening coverage. Rank behavioral and architectural impact before
incidental platform mechanics, unless the platform issue contradicts an explicit support claim.

Prefer target-owned contract and regression tests when they encode learned behavior; use external
validators and lint as supplementary evidence. Attribute every non-pass result to target behavior,
the test harness or adapter, an unmet environment precondition, or unavailable evidence before
counting findings. Collapse repeated symptoms under the earliest evidenced common cause while
retaining the raw test counts.

**Done when:** each conclusion belongs to one axis, cites direct evidence, and states whether it is a
confirmed defect, design risk, evidence gap, or intentional tradeoff; repeated failures are not
misreported as independent defects.

### 5. Decide and report

Pass each candidate issue through three filters:

- **Product value**: does it affect the user's outcome, behavioral accuracy, or business result?
- **Delivery economics**: is the risk reduction worth the edit, tooling, testing, and coordination?
- **Architecture integrity**: does the remedy preserve ownership, callers, state, and evolution?

Open with a compact decision brief: **Preserve** learned invariants, **Change** justified findings,
and **Evidence limits** that bound the claims. Give recheckable findings stable IDs and include the
claim, evidence, impact, confidence, and smallest justified action. State when the evidence
contradicts the user's proposed cause. A no-finding result is valid when the contract is coherent and
the evidence does not justify change.

Close with checks performed, checks intentionally skipped, and the resulting evidence boundary.

**Done when:** every recommendation is supported by evidence and worth its cost, and the user can
distinguish observed facts, interpretation, uncertainty, and requested decisions.

### 6. Route the outcome

- For **Review**, stop without modifying the target.
- For **Polish** or **Recheck**, read
  [references/polish-and-recheck.md](references/polish-and-recheck.md) before acting.
- When source, repository, published, or installed copies may disagree, read
  [references/release-drift.md](references/release-drift.md) to audit release state.
- When the remedy requires a new identity or full rebuild, hand a behavior contract and preserved
  invariants to `Skill Creator Pro` and classify the work as a rebuild.

**Done when:** the result is read-only, minimally patched and rechecked, release-audited, or handed
off to the correct owner with no silent expansion of authority.
