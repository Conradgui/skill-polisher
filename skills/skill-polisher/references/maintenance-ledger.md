# Maintenance Ledger

Use one Maintenance Ledger as the authoritative cross-stage record. Keep it outside the installable
target skill unless that repository explicitly owns maintenance evidence. Prefer a user-provided or
existing project evidence location. When no write location is authorized, return the complete ledger
as Markdown and mark `persistence: NON_DURABLE`.

## Required header

Record:

- target identity and path;
- baseline revision or content hash;
- requested outcome and mutation boundary;
- evidence location and `persistence: DURABLE | NON_DURABLE`;
- current lifecycle stage;
- dates or sequence markers needed to distinguish batches.

## Review packet

Include:

1. **Preserve**: learned invariants and boundaries the patch must not damage.
2. **Findings**: stable ID, independent axis, claim, direct evidence, impact, confidence, smallest
   justified action, recommendation, and dependencies.
3. **Evidence limits**: unavailable sources, checks intentionally skipped, and the claim each limit
   narrows.
4. **Decision register**: the fields below for every actionable finding.

Use exactly these independent state dimensions:

| Field | Allowed values |
|---|---|
| `decision` | `PENDING`, `FIX_NOW`, `DEFER`, `ACCEPT_RISK`, `REJECT` |
| `polish_state` | `NOT_STARTED`, `IMPLEMENTED`, `PARTIAL`, `NOT_APPLICABLE` |
| `recheck_outcome` | `NOT_RUN`, `RESOLVED`, `OPEN`, `PARTIAL`, `NOT_REPRODUCED`, `BLOCKED` |

Record the user-approved scope, order or batch, source revision, and approval evidence beside
`decision`. Do not infer a decision from silence.

## Polish packet

Append one batch record without rewriting the Review evidence:

- batch ID and finding IDs;
- approved scope and baseline identity;
- files changed and behavior changed;
- how each change addresses its finding;
- intentionally unchanged or deferred work;
- targeted verification commands or observations and results;
- invariant comparison, achieved effect, skipped checks, and residual risk;
- resulting revision or content identity;
- resulting `polish_state` for each attempted finding.

## Recheck packet

Append:

- confirmed candidate identity and material scope;
- explicit confirmation source;
- per-finding `recheck_outcome` and current evidence;
- modified-behavior, invariant, regression, near-miss, and target-owned validation results;
- a Review-to-Polish-to-Recheck summary, capabilities added, changed, or removed, and the owning
  README, design, changelog, test, or evidence surfaces checked for each statement;
- stale, missing, duplicated, intentionally unchanged, or not-applicable documentation surfaces;
- checks skipped or blocked and how they narrow readiness;
- overall readiness for the user's stated purpose.

Update evidence outcomes without overwriting the user's decision or the Polish history.

## Release Drift packet

When relevant, append separate states for runtime, harness metadata, repository contract, version
intent, CI, remote publication, and installed copy. Use content hashes or an equivalent identity
when exact agreement matters. Do not collapse these states into one release status.
