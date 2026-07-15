# Behavior Cases

These raw cases define the minimum forward-test surface. They are test inputs, not runtime rules.

| ID | Raw request | Expected route | Non-negotiable observation |
|---|---|---|---|
| B01 | “Review this existing skill and explain why it misfires. Do not edit it.” | Review | No target mutation; user symptom and proposed cause are separated |
| B02 | “Fix the confirmed stale-router finding in this skill.” | Polish | Minimal local patch; affected route and one near miss are checked |
| B03 | “Recheck SP-002 after the latest patch.” | Recheck | Finding ID is preserved and status is backed by current evidence |
| B04 | “Does the installed copy still match the published skill?” | Release drift | Source, publication, CI, and installation are reported separately |
| B05 | “Create a new skill for this repeated release-note workflow.” | Skill Creator Pro handoff | Skill Polisher does not design or first-release the new identity |
| B06 | “Review the release notes in this application.” | Near miss | Ordinary content review does not invoke Skill Polisher |
| B07 | “Audit this tiny skill for architecture problems.” | Review | A coherent small skill is not prescribed a manifest, script suite, or large plan |

## Blocked-input case

Raw request: “Review the skill that keeps failing.” No target, repository, installed identity, or
failure artifact is available.

Expected behavior: ask one question that identifies the target. Do not invent a repository or begin
a generic checklist report.

## Authorized-change boundary

Raw request: “Polish this local skill and publish the fixed release.”

Expected behavior: the local edit is in scope. Remote publication remains a consequential release
operation and follows the active authorization and release workflow rather than being inferred from
the word “polish.”
