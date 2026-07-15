# Polish and Recheck

Read this reference only after the main workflow selects **Polish** or **Recheck**.

## Polish an existing skill

1. Preserve unrelated user changes and establish the pre-edit baseline.
2. Record the invariants the patch must preserve. Use a short note for a local wording or metadata
   change; create a durable ledger only when the edit could alter claims, state, identifiers,
   citations, authorization, or other high-consequence facts.
3. Fix the earliest causal failure. Prefer the smallest patch that restores the behavior contract
   over nearby cleanup.
4. Update a caller, router, adapter, test, or documentation only when the changed behavior makes it
   stale. Keep one authority for each meaning.
5. Validate the original regression, the affected branch, and one near miss. Expand to related
   callers, representative forward tests, or the broader suite only when impact or uncertainty
   warrants it.
6. Compare the result with the invariant record and inspect the final diff.

Ask before a test that is expensive, substantially time-consuming, newly authorized, or capable of
changing a live system. A request to edit local files does not authorize those effects.

Hand off the files changed, behavior restored, evidence collected, checks skipped, and residual
risk. Do not claim a platform, installation path, or release state that was not exercised.

## Recheck prior findings

Reuse the original evidence standard and preserve finding IDs. Reproduce against the current source
revision before changing status. If no existing status vocabulary controls the report, use exactly:

- `OPEN`
- `RESOLVED`
- `PARTIAL`
- `NOT_REPRODUCED`
- `ACCEPTED_RISK`
- `BLOCKED`

For each changed status, cite the new evidence and distinguish source change from environment change.
Add a new finding only when the current evidence reveals a separate causal issue; do not mutate an
old finding into a different claim.

Recheck only the stable findings and regression surface unless a changed dependency, caller, state
model, or release claim widens the evidence boundary.
