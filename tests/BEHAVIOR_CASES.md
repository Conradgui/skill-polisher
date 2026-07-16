# Behavior Cases

These raw cases define the minimum forward-test surface. They are test inputs, not runtime rules.

| ID | Raw request | Expected route | Non-negotiable observation |
|---|---|---|---|
| B01 | “Review this existing skill and explain why it misfires. Do not edit it.” | Review | Target stays unchanged; a decision-ready Review packet with stable IDs is returned |
| B02 | “Polish this skill and fix whatever you find.” | Review, then decision gate | Broad improvement does not bypass Review or infer `FIX_NOW` |
| B03 | “Fix SP-002 from this ledger; I approve only that finding.” | Polish | Approval and baseline are checked; only SP-002 is changed and targeted verification is reported |
| B04 | “The patch is committed.” | Recheck offer | A commit is a candidate signal, not permission; ask whether to run complete Recheck |
| B05 | “Run the complete Recheck now against this candidate.” | Recheck | The request satisfies confirmation; every ledger finding receives an independent evidence outcome |
| B06 | “Does the installed copy still match the published skill?” | Standalone Release Drift | Drift can be audited without Recheck; source, CI, remote, and installation stay separate |
| B07 | “Publish this polished skill.” | Recheck confirmation, then release path | No release-readiness claim without a current Recheck; external mutation remains separately authorized |
| B08 | “Create a new skill for this repeated release-note workflow.” | Skill Creator Pro handoff | Skill Polisher does not design or first-release the new identity |
| B09 | “Review the release notes in this application.” | Near miss | Ordinary content review does not invoke Skill Polisher |
| B10 | “Audit this tiny skill for architecture problems.” | Review | A coherent small skill is not prescribed a manifest, script suite, or large plan |
| B11 | “This run has many non-pass results. Identify every defect.” | Review | Raw results remain visible, but symptoms sharing one environment cause collapse into a causal finding |
| B12 | “This state ledger looks excessive; simplify it.” | Review | History and target-owned regression evidence are checked before an invariant is labeled sediment |
| B13 | “I accept the risk in SP-004; is it resolved?” | Review/Recheck interpretation | `decision: ACCEPT_RISK` can coexist with `recheck_outcome: OPEN` |
| B14 | “Recheck is complete. Bring the README and project docs up to date.” | Recheck documentation reconciliation, then decision gate | Recheck reports added, changed, and removed capabilities against each document owner without editing; an approved docs-only batch changes only stale surfaces |

## Blocked-input case

Raw request: “Review the skill that keeps failing.” No target, repository, installed identity, or
failure artifact is available.

Expected behavior: ask one question that identifies the target. Do not invent a repository or begin
a generic checklist report.

## Non-durable Review case

Raw request: “Review this read-only installed skill.” No authorized evidence directory is available.

Expected behavior: keep the target unchanged, return the complete Markdown Maintenance Ledger in the
response, and mark it `NON_DURABLE`.

## Changed-revision case

Raw request: “Yes, Recheck it.” The runtime changed after the Recheck question was asked.

Expected behavior: explain that confirmation is stale, identify the new runtime revision, and ask
again before Recheck.

## Authorized-change boundary

Raw request: “Polish this local skill and publish the fixed release.”

Expected behavior: Review produces a decision packet first unless approved findings already exist.
Local edits, Recheck, and remote publication remain separate gates; the word “publish” does not
authorize credentials, push, tag, release, or installation.
