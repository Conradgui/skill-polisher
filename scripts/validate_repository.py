#!/usr/bin/env python3
"""Validate Skill Polisher's release identity and repository boundaries."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "skill-polisher"
DOC_PAIRS = (
    (ROOT / "README.md", ROOT / "README.zh.md"),
    (ROOT / "CONTRIBUTING.md", ROOT / "CONTRIBUTING.zh.md"),
    (ROOT / "docs" / "DESIGN.md", ROOT / "docs" / "DESIGN.zh.md"),
    (
        ROOT / "docs" / "REAL_WORLD_EVALUATION.md",
        ROOT / "docs" / "REAL_WORLD_EVALUATION.zh.md",
    ),
)
CREATOR_PRO_REVISION = "eb23656e56ea3555599a6c5278a8b5834dc56b6d"
LOCAL_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def strip_fenced_blocks(text: str) -> str:
    """Remove fenced examples before treating links or placeholders as live content."""

    kept: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        marker = line.lstrip()
        if fence is None and (marker.startswith("```") or marker.startswith("~~~")):
            fence = marker[:3]
            kept.append("\n")
            continue
        if fence is not None:
            if marker.startswith(fence):
                fence = None
            kept.append("\n")
            continue
        kept.append(line)
    return "".join(kept)


def local_link_targets(markdown: str) -> list[str]:
    """Return live repository-local Markdown link targets."""

    targets: list[str] = []
    for match in LOCAL_LINK_RE.finditer(strip_fenced_blocks(markdown)):
        target = match.group(1).strip().strip("<>")
        if not target or target.startswith("#"):
            continue
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
            continue
        path_part = unquote(target.split("#", 1)[0])
        if path_part:
            targets.append(path_part)
    return targets


def heading_levels(markdown: str) -> tuple[int, ...]:
    """Return the ordered ATX heading-level structure outside fenced blocks."""

    return tuple(
        len(match.group(1))
        for match in re.finditer(r"^(#{1,6})\s+", strip_fenced_blocks(markdown), re.MULTILINE)
    )


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse the flat fields Skill Polisher requires from SKILL.md frontmatter."""

    if not text.startswith("---\n"):
        return {}
    parts = text.split("---", 2)
    if len(parts) != 3:
        return {}
    values: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line or line[:1].isspace():
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def repository_markdown(root: Path) -> list[Path]:
    """Return human and runtime Markdown while excluding generated local state."""

    excluded = {".git", ".agents", ".tmp"}
    return [
        path
        for path in root.rglob("*.md")
        if not excluded.intersection(path.relative_to(root).parts)
    ]


def validate_identity(root: Path, errors: list[str]) -> None:
    required = (
        "README.md",
        "README.zh.md",
        "CONTRIBUTING.md",
        "CONTRIBUTING.zh.md",
        "CHANGELOG.md",
        "LICENSE",
        "NOTICE.md",
        "VERSION",
    )
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"{relative}: required release file is missing")

    version_path = root / "VERSION"
    if version_path.is_file():
        version = version_path.read_text(encoding="utf-8").strip()
        if not VERSION_RE.fullmatch(version):
            errors.append(f"VERSION: expected semantic X.Y.Z version, got {version!r}")
        else:
            changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
            if f"## [{version}]" not in changelog:
                errors.append(f"CHANGELOG.md: missing release heading for {version}")

    readme = (root / "README.md").read_text(encoding="utf-8")
    required_readme = (
        "Conradgui/skill-polisher",
        "skills/skill-polisher",
        "$skill-polisher",
        "Skill Creator Pro",
        "Real-World Evaluation",
    )
    for snippet in required_readme:
        if snippet not in readme:
            errors.append(f"README.md: missing public identity or evidence marker {snippet!r}")


def validate_installable_boundary(root: Path, errors: list[str]) -> None:
    installable = sorted(
        path.parent.relative_to(root).as_posix()
        for path in (root / "skills").glob("*/SKILL.md")
    )
    if installable != ["skills/skill-polisher"]:
        errors.append(
            "skills/: installable allow-list must be exactly ['skills/skill-polisher']; "
            f"found {installable}"
        )

    skill_path = root / "skills" / "skill-polisher" / "SKILL.md"
    if not skill_path.is_file():
        errors.append("skills/skill-polisher/SKILL.md: missing")
        return
    frontmatter = parse_frontmatter(skill_path.read_text(encoding="utf-8"))
    name = frontmatter.get("name", "")
    if not NAME_RE.fullmatch(name):
        errors.append(f"SKILL.md: invalid or missing name {name!r}")
    if name != "skill-polisher":
        errors.append(f"SKILL.md: name must be 'skill-polisher', got {name!r}")
    if not frontmatter.get("description"):
        errors.append("SKILL.md: description is required")
    if not (root / "skills" / "skill-polisher" / "agents" / "openai.yaml").is_file():
        errors.append("skills/skill-polisher/agents/openai.yaml: missing")

    for path in (root / "skills" / "skill-polisher").rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {
            ".md",
            ".yaml",
            ".yml",
            ".json",
            ".py",
            ".txt",
        }:
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root)
        if CJK_RE.search(text):
            errors.append(f"{relative}: English is the sole runtime source of truth")
        if re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", strip_fenced_blocks(text)):
            errors.append(f"{relative}: unresolved placeholder")


def validate_document_pairs(root: Path, errors: list[str]) -> None:
    for english_path, chinese_path in DOC_PAIRS:
        if not english_path.is_file() or not chinese_path.is_file():
            errors.append(
                "documentation pair missing: "
                f"{english_path.relative_to(root)} <-> {chinese_path.relative_to(root)}"
            )
            continue
        english = english_path.read_text(encoding="utf-8")
        chinese = chinese_path.read_text(encoding="utf-8")
        if f"./{chinese_path.name}" not in english:
            errors.append(f"{english_path.relative_to(root)}: missing Chinese mirror link")
        if f"./{english_path.name}" not in chinese:
            errors.append(f"{chinese_path.relative_to(root)}: missing English mirror link")
        if heading_levels(english) != heading_levels(chinese):
            errors.append(
                "heading parity mismatch: "
                f"{english_path.relative_to(root)} <-> {chinese_path.relative_to(root)}"
            )


def validate_local_links(root: Path, errors: list[str]) -> None:
    resolved_root = root.resolve()
    for path in repository_markdown(root):
        content = path.read_text(encoding="utf-8")
        for target in local_link_targets(content):
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(resolved_root)
            except ValueError:
                errors.append(f"{path.relative_to(root)}: local link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(root)}: broken local link: {target}")


def validate_ci_contract(root: Path, errors: list[str]) -> None:
    path = root / ".github" / "workflows" / "validate.yml"
    if not path.is_file():
        errors.append(".github/workflows/validate.yml: missing")
        return
    workflow = path.read_text(encoding="utf-8")
    required = (
        "ubuntu-latest",
        "windows-latest",
        CREATOR_PRO_REVISION,
        "python -m compileall -q scripts tests",
        "python scripts/validate_repository.py",
        "python -m unittest discover -s tests -v",
        "quick_validate.py skills/skill-polisher",
        "quality_lint.py skills/skill-polisher --strict",
    )
    for snippet in required:
        if snippet not in workflow:
            errors.append(f".github/workflows/validate.yml: missing {snippet!r}")


def collect_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    validate_identity(root, errors)
    validate_installable_boundary(root, errors)
    validate_document_pairs(root, errors)
    validate_local_links(root, errors)
    validate_ci_contract(root, errors)
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Repository validation passed: release identity, installable boundary, bilingual docs, "
        "runtime language, local links, version state, and CI contract are consistent."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
