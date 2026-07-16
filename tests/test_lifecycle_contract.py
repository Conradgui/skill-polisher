from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "skills" / "skill-polisher" / "SKILL.md").read_text(encoding="utf-8")
REFERENCES = ROOT / "skills" / "skill-polisher" / "references"
LEDGER = (REFERENCES / "maintenance-ledger.md").read_text(encoding="utf-8")
POLISH_RECHECK = (REFERENCES / "polish-and-recheck.md").read_text(encoding="utf-8")
RELEASE_DRIFT = (REFERENCES / "release-drift.md").read_text(encoding="utf-8")
CASES = (ROOT / "tests" / "BEHAVIOR_CASES.md").read_text(encoding="utf-8")


class LifecycleContractTests(unittest.TestCase):
    def test_broad_polish_cannot_bypass_review_decision(self) -> None:
        self.assertIn("broad request to improve", SKILL)
        self.assertIn("explicit `FIX_NOW` approval", SKILL)
        self.assertIn("Leave silence as `PENDING`", SKILL)

    def test_ledger_separates_decision_progress_and_evidence(self) -> None:
        for field in ("`decision`", "`polish_state`", "`recheck_outcome`"):
            self.assertIn(field, LEDGER)
        self.assertIn("`ACCEPT_RISK`", LEDGER)
        self.assertIn("Never use `ACCEPT_RISK` as a Recheck outcome", POLISH_RECHECK)

    def test_polish_packet_is_required_before_recheck(self) -> None:
        self.assertIn("deliver a Polish packet", SKILL)
        self.assertIn("Targeted verification supports the Polish claim; it is not Recheck", SKILL)
        self.assertIn("Do not set `recheck_outcome` during Polish", POLISH_RECHECK)

    def test_recheck_requires_explicit_confirmation(self) -> None:
        question = "Run the complete Recheck now?"
        self.assertIn(question, SKILL)
        self.assertIn(question, " ".join(POLISH_RECHECK.split()))
        self.assertIn("A current user message that explicitly requests", POLISH_RECHECK)
        self.assertIn("A commit is a candidate signal, not permission", CASES)

    def test_release_audit_and_release_path_are_distinct(self) -> None:
        self.assertIn("standalone drift audit does not require Recheck", RELEASE_DRIFT)
        self.assertIn("release-readiness claim", RELEASE_DRIFT)
        self.assertIn("mark Recheck stale", RELEASE_DRIFT)

    def test_recheck_reconciles_documentation_without_mutating_it(self) -> None:
        self.assertIn("Reconcile the documentation system", SKILL)
        self.assertIn("capabilities added, changed, or removed", POLISH_RECHECK)
        self.assertIn("documentation-only Polish", POLISH_RECHECK)
        self.assertIn("B14", CASES)


if __name__ == "__main__":
    unittest.main()
