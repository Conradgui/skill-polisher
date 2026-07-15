# 贡献指南

[English](./CONTRIBUTING.md)

欢迎能够改善既有 Skill 诊断、learned invariant 保护、适度证据、可移植性或发布准确性的贡献。

## 运行时语言

英文是运行时指令、reference 与 metadata 的唯一事实来源。面向读者的中文文档同步英文项目文档，不得增加新的运行规则。

## 变更纪律

对于行为变更：

1. 明确被修改的审核分支或 failure mode。
2. 保留无关行为以及与 Creator Pro 的职责边界。
3. 当变更可测试时，新增或更新原始 behavior case 或真实仓库 regression。
4. 让目标自有 contract evidence 优先于新增 heuristic 规则。
5. 先更新英文文档，再同步中文镜像。

对于纯发布变更，除非发布证据暴露运行时缺陷，否则保持运行时工件不变。

## 必需检查

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
python <skill-creator-pro>/scripts/quick_validate.py skills/skill-polisher
python <skill-creator-pro>/scripts/quality_lint.py skills/skill-polisher --strict
```

CI workflow 固定了后两个命令所使用的 Skill Creator Pro 精确 revision。归属或研究仓库范围变化时，请复核 `NOTICE.md`。
