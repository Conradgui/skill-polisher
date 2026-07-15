from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_repository.py"
SPEC = importlib.util.spec_from_file_location("validate_repository", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class RepositoryValidatorTests(unittest.TestCase):
    def test_fenced_examples_do_not_create_live_links(self) -> None:
        markdown = "Before\n```md\n[missing](./not-real.md)\n```\n[real](./README.md)\n"
        self.assertEqual(["./README.md"], validator.local_link_targets(markdown))

    def test_urls_and_anchors_are_not_local_files(self) -> None:
        markdown = "[web](https://example.com) [mail](mailto:a@example.com) [here](#section)"
        self.assertEqual([], validator.local_link_targets(markdown))

    def test_heading_levels_preserve_order_and_ignore_fences(self) -> None:
        markdown = "# One\n```md\n## Example\n```\n## Two\n### Three\n"
        self.assertEqual((1, 2, 3), validator.heading_levels(markdown))

    def test_flat_frontmatter_is_parsed(self) -> None:
        text = "---\nname: skill-polisher\ndescription: Review skills.\n---\n\n# Body\n"
        self.assertEqual(
            {"name": "skill-polisher", "description": "Review skills."},
            validator.parse_frontmatter(text),
        )

    def test_current_repository_contract_passes(self) -> None:
        self.assertEqual([], validator.collect_errors(ROOT))


if __name__ == "__main__":
    unittest.main()
