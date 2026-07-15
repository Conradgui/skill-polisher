# Contributing

[简体中文](./CONTRIBUTING.zh.md)

Contributions are welcome when they improve existing-skill diagnosis, preservation of learned
invariants, proportional evidence, portability, or release accuracy.

## Runtime language

English is the sole source of truth for runtime instructions, references, and metadata. Human-facing
Chinese documentation mirrors the English project documents and must not introduce new runtime
rules.

## Change discipline

For a behavior change:

1. Name the review branch or failure mode being changed.
2. Preserve unrelated behavior and the Creator Pro boundary.
3. Add or update a raw behavior case or real-world regression when the change is testable.
4. Prefer target-owned contract evidence over new heuristic rules.
5. Update English documentation first, then its Chinese mirror.

For a release-only change, keep the runtime artifact untouched unless the release evidence exposes a
runtime defect.

## Required checks

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
python <skill-creator-pro>/scripts/quick_validate.py skills/skill-polisher
python <skill-creator-pro>/scripts/quality_lint.py skills/skill-polisher --strict
```

The CI workflow pins the exact Skill Creator Pro revision used for the last two commands. Review
`NOTICE.md` whenever attribution or study-repository scope changes.
