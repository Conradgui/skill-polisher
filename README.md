# Skill Polisher

[简体中文](./README.zh.md)

Evidence-led review and minimal refinement for existing agent skills.

Skill Polisher treats an existing skill as a living system: behavior, callers, state, history,
tests, and release copies all contribute evidence. It reviews read-only by default and changes a
skill only when the user asks for an improvement and the evidence justifies it.

> **Proportional rigor:** use the minimum sufficient evidence for the risk of the decision.

## Why this project exists

Mature skills rarely arrive fully designed. Their strongest gates, ledgers, adapters, and state
models often encode failures learned through iteration. A snapshot-only lint can mistake those
safeguards for complexity, focus on incidental platform details, or recommend broad cleanup without
understanding ownership and history.

Skill Polisher is the maintenance counterpart to
[Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro): Creator Pro creates and first
releases a skill; Polisher diagnoses and refines it after an identity and behavior history exist.
Its writing and evidence discipline follows the independent
[Matt Pocock-inspired Skill Writing](https://github.com/Conradgui/matt-pocock-inspired-skill-writing)
guidelines.

The goal is a skill for real engineering work: preserve user control, make claims traceable, protect
learned architecture, and spend testing effort where it can change a decision.

## What it does

| Mode | Outcome | Mutation |
|---|---|---|
| **Review** | Diagnose behavior, architecture, evolution, and evidence | Read-only |
| **Polish** | Apply the smallest evidence-backed improvement | Explicit local authority required |
| **Recheck** | Reassess stable findings against a changed artifact | Read-only unless another fix is requested |
| **Release drift** | Compare source, repository, published, CI, and installed states | Read-only audit by default |

It evaluates four independent axes—contract, system, evolution, and evidence—without flattening
them into one score. Product value, delivery economics, and architecture integrity determine whether
a technically valid observation is worth changing.

## Creator Pro boundary

| Situation | Owner |
|---|---|
| Repeated workflow or new capability becomes a new skill | Skill Creator Pro |
| Pre-release defects in a new skill | Skill Creator Pro |
| Existing skill diagnosis and architectural review | Skill Polisher |
| Explicitly requested in-place refinement | Skill Polisher |
| Drift in an existing published or installed skill | Skill Polisher |
| A new identity or full rebuild is required | Polisher specifies the contract; Creator Pro rebuilds and releases |

This boundary prevents a maintenance review from becoming an unannounced rewrite and keeps Creator
Pro focused on creation and first release.

## How it works

```text
Scope and authority
→ Proportional evidence boundary
→ Living contract and ownership
→ Independent review axes
→ Stable findings
→ Read-only result, minimal patch, recheck, or Creator Pro handoff
```

The runtime workflow is canonical in
[`skills/skill-polisher/SKILL.md`](./skills/skill-polisher/SKILL.md). The
[design record](./docs/DESIGN.md) captures the behavior contract, evidence basis, and decisions that
keep the implementation intentionally small. The
[forward evaluation](./docs/FORWARD_EVALUATION.md) reports observed checks separately from remaining
transfer risk.

## Install locally

From this repository root:

```bash
npx skills add . --skill skill-polisher
```

Or copy `skills/skill-polisher` into your Codex skills directory. Restart or refresh the client if
it does not detect newly installed skills immediately.

## Example requests

```text
Review this existing skill and explain why its invocation is unreliable. Do not edit it.
```

```text
Polish this skill to fix the confirmed stale-router finding, preserving all other behavior.
```

```text
Recheck findings SP-001 and SP-003 against the current commit.
```

```text
Audit whether the installed skill still matches the published repository and release metadata.
```

## Repository structure

```text
skill-polisher/
├── skills/skill-polisher/   # Installable runtime skill
│   ├── SKILL.md             # Canonical behavior
│   ├── agents/openai.yaml   # Codex UI and invocation metadata
│   └── references/          # Conditional Polish/Recheck and release-drift rules
├── docs/                    # Human-facing design and forward evidence
└── tests/                   # Behavior cases and deliberately small fixtures
```

English runtime files are the semantic source of truth. Chinese documentation mirrors human-facing
project information and does not add independent runtime rules.

## Status

The project is in local pre-release development. Local installation with `skills@1.5.17` has been
verified with zero source-to-installed file drift. No remote publication, remote CI, or fresh-remote
installation claim is implied until those states are actually verified.

## Attribution

This independent project is informed by Skill Creator Pro and the Matt Pocock-inspired Skill
Writing Guidelines. It is not official OpenAI or Matt Pocock material, and no endorsement is
implied. See [NOTICE.md](./NOTICE.md).

## License

[MIT](./LICENSE)
