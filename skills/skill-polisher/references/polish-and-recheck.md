# Polish and Recheck

Read this reference only for an approved Polish batch or a user-confirmed Recheck.

## Polish an approved batch

1. Read the Maintenance Ledger and confirm that each requested finding is `FIX_NOW`, the approved
   scope is explicit, and the authorization still matches the baseline revision.
2. Preserve unrelated user changes and the ledger's learned invariants.
3. Fix the earliest causal failure with the smallest coherent patch. Keep one authority for each
   meaning and update adjacent surfaces only when the approved behavior makes them stale.
4. Run targeted verification for the original regression, affected branch, and one plausible near
   miss. Expand to related callers or suites only when another check can change the Polish claim.
5. Inspect the final diff against the approved scope and invariants.
6. Update the batch record with files, behavior changes, targeted evidence, omissions, achieved
   effect, residual risk, and the resulting revision or content identity.

Use `IMPLEMENTED`, `PARTIAL`, or `NOT_APPLICABLE` for `polish_state`; keep `NOT_STARTED` for approved
work not attempted. Do not set `recheck_outcome` during Polish.

Ask before a test that is expensive, substantially time-consuming, newly authorized, or capable of
changing a live system. A local edit request does not authorize those effects.

## Confirm Recheck

Treat a delivered Polish batch, completed candidate, commit, merge request, internal handoff, or
release preparation as a reason to offer Recheck, not as permission to start it. Ask `Run the
complete Recheck now?` and wait. Silence is pending. A current user message that explicitly requests
Recheck already satisfies this gate.

Bind confirmation to the candidate revision and material scope. Ask again when runtime content or
the completion claim changes before Recheck begins.

## Run the complete Recheck

1. Reproduce against the confirmed candidate without modifying it.
2. Account for every finding in the Maintenance Ledger, including deferred, rejected, and
   accepted-risk items; user decision does not determine the evidence outcome.
3. Verify every modified behavior, preserved invariant, relevant regression surface, and near miss.
4. Run target-owned validators and tests required by the requested completion claim. Apply
   proportional rigor to tools, not to ledger coverage: every finding must receive an outcome even
   when a check is skipped or blocked.
5. Preserve finding IDs. Add a new ID only when current evidence reveals a separate causal issue.
6. Reconcile the documentation system read-only. Summarize Review findings, Polish resolutions,
   Recheck closure, and capabilities added, changed, or removed; check them against the existing
   owners for current behavior, rationale, iteration history, executable contracts, and detailed
   evidence. Record stale, missing, or duplicated surfaces as findings.
7. Record current evidence, source-versus-environment changes, skipped checks, documentation
   reconciliation, and overall readiness.

Use exactly these `recheck_outcome` values:

- `RESOLVED`
- `OPEN`
- `PARTIAL`
- `NOT_REPRODUCED`
- `BLOCKED`

Keep Recheck read-only. A new or remaining issue returns to the decision gate; it does not silently
authorize another Polish batch. Never use `ACCEPT_RISK` as a Recheck outcome because it belongs to
the independent `decision` dimension.

After a separately approved documentation-only Polish, keep the runtime Recheck current only when
runtime content is unchanged and rerun the affected documentation or repository gates. If runtime
content changes, mark Recheck stale and require confirmation again.
