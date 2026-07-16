# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Added a Maintenance Ledger runtime reference and lifecycle contract regressions for review
  packets, explicit decisions, Polish evidence, Recheck confirmation, and release sequencing.
- Added a read-only Recheck documentation reconciliation that maps current behavior, rationale,
  iteration history, executable contracts, and detailed evidence to their owning surfaces.

### Changed

- Replaced the parallel mode picker with a Review -> decision -> Polish -> confirmed Recheck
  maintenance lifecycle while preserving direct entry for already approved findings and standalone
  drift audits.
- Require a user-reviewable evidence packet after Review, each Polish batch, and Recheck.
- Separate user `decision`, `polish_state`, and `recheck_outcome` so accepted risk cannot be mistaken
  for resolved evidence.
- Treat commits, completed Polish batches, handoffs, and release preparation as reasons to offer
  Recheck; require explicit user confirmation before starting it.
- Require a current runtime Recheck before claiming release readiness and invalidate it only when
  runtime content changes.
- Keep the README compatibility summary environment-neutral and move one-session platform, installer,
  and model limitations to the historical real-world evaluation.

### Removed

- Removed direct broad-improvement-to-Polish routing, automatic Recheck assumptions, and the use of
  accepted risk as a resolution signal. Approved-finding Polish and standalone drift audits remain.

## [0.1.0] - 2026-07-15

### Added

- Published the first public repository contract with pinned Windows/Ubuntu CI, semantic version
  state, repository validation, regression tests, and verified Codex installation from GitHub.
- Initial `skill-polisher` runtime with Review, Polish, Recheck, and release-drift branches.
- Proportional-evidence stopping rules and a default read-only authority boundary.
- Creator Pro handoff for new identities and full rebuilds.
- English and Simplified Chinese project documentation.
- Behavior cases and a deliberately small fixture for forward validation.
- Forward evidence from three mature skill systems, one small fixture, and a local release-drift
  comparison, with remaining transfer risk stated explicitly.
- Verified local `npx skills` discovery and installation with byte-identical runtime files.
- Added `zero-to-one-product-discovery` to the real-world test set and replaced the initial forward
  note with a four-repository bilingual evaluation.

### Changed

- Attribute non-pass results to target behavior, harness, environment, or unavailable evidence
  before counting findings.
- Collapse repeated symptoms under the earliest evidenced common cause while retaining raw counts.
- Prefer target-owned contract tests over external heuristic signals when reconstructing learned
  behavior.
- Report `Preserve`, `Change`, and `Evidence limits` as the compact maintenance decision brief.
- Rebuilt the English and Chinese READMEs around the richer Skill Creator Pro project structure.
