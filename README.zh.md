# Skill Polisher

[English](./README.md)

面向既有 Agent Skill 的证据驱动审核与最小化打磨。

Skill Polisher 将既有 Skill 视为一个持续演化的系统：行为、调用方、状态、历史、测试与发布副本都属于证据。默认只读审核；只有用户明确要求改进且证据支持时，才修改 Skill。

> **适度严谨（Proportional rigor）：** 针对当前决策的风险，使用足以支撑结论的最小证据集。

## 为什么要做这个项目

成熟 Skill 很少从第一天起就被完整设计出来。它们最重要的门槛、账本、适配器和状态模型，往往是迭代中真实失败留下的经验。只看当前快照的 lint，容易把这些保护机制误判为复杂度，把注意力放在偶发的平台细节上，或者在没有理解职责与历史时建议大范围清理。

Skill Polisher 是 [Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro) 的维护侧对应物：Creator Pro 负责创建 Skill 与首次发布；Polisher 负责在 Skill 已经拥有身份和行为历史之后进行诊断与打磨。它的写作与证据纪律遵循独立的 [Matt Pocock-inspired Skill Writing](https://github.com/Conradgui/matt-pocock-inspired-skill-writing) 指南。

它要践行的是真实工程工作中的 Skill：保留用户控制权，使结论可追溯，保护迭代形成的架构，并把测试资源投入到真正可能改变决策的地方。

## 它能做什么

| 模式 | 产出 | 修改行为 |
|---|---|---|
| **Review** | 诊断行为、架构、演化与证据 | 只读 |
| **Polish** | 应用证据支持的最小改进 | 需要明确的本地修改授权 |
| **Recheck** | 根据变更后的工件复核稳定 finding | 除非另行要求修复，否则只读 |
| **Release drift** | 比较源码、仓库、发布、CI 与安装状态 | 默认只读审计 |

它分别判断 contract、system、evolution 和 evidence 四个独立维度，而不是把它们压缩成一个总分。一个技术观察是否值得修改，还要同时通过产品价值、交付效费比和架构完整性判断。

## 与 Creator Pro 的边界

| 场景 | 负责人 |
|---|---|
| 重复工作流或新能力成为新 Skill | Skill Creator Pro |
| 新 Skill 首次发布前的缺陷 | Skill Creator Pro |
| 既有 Skill 的诊断与架构审核 | Skill Polisher |
| 用户明确要求的原位打磨 | Skill Polisher |
| 已发布或已安装 Skill 的漂移 | Skill Polisher |
| 需要新身份或整体重建 | Polisher 给出契约；Creator Pro 重建并发布 |

这条边界避免维护审核在未声明的情况下演变为重写，也让 Creator Pro 保持对创建和首次发布的专注。

## 工作方式

```text
范围与授权
→ 适度的证据边界
→ 活的行为契约与职责归属
→ 独立审核维度
→ 稳定 findings
→ 只读结论、最小补丁、复核或 Creator Pro 交接
```

运行时规范以 [`skills/skill-polisher/SKILL.md`](./skills/skill-polisher/SKILL.md) 为唯一权威来源。[设计记录](./docs/DESIGN.zh.md) 说明行为契约、证据基础，以及让实现保持克制的关键决策。[前向评估](./docs/FORWARD_EVALUATION.zh.md) 将已经观察到的检查结果与仍然存在的迁移风险分开报告。

## 本地安装

在仓库根目录运行：

```bash
npx skills add . --skill skill-polisher
```

也可以把 `skills/skill-polisher` 复制到 Codex skills 目录。如果客户端没有立刻发现新 Skill，请重启或刷新。

## 示例请求

```text
审核这个既有 Skill，解释为什么它的调用不稳定。不要修改文件。
```

```text
打磨这个 Skill，修复已经确认的 stale-router finding，并保留其他行为。
```

```text
基于当前 commit 复核 SP-001 和 SP-003。
```

```text
检查已安装 Skill 是否仍与公开仓库和 release metadata 一致。
```

## 仓库结构

```text
skill-polisher/
├── skills/skill-polisher/   # 可安装运行时 Skill
│   ├── SKILL.md             # 唯一行为权威
│   ├── agents/openai.yaml   # Codex UI 与调用 metadata
│   └── references/          # 条件加载的修改、复核与发布漂移规则
├── docs/                    # 面向读者的设计与前向证据
└── tests/                   # 行为用例与刻意保持简单的 fixtures
```

英文运行时文件是语义上的唯一事实来源。中文文档只同步面向读者的项目信息，不增加独立运行规则。

## 当前状态

项目目前处于本地预发布开发阶段。已经使用 `skills@1.5.17` 完成本地安装验证，源码与安装副本零文件漂移。在实际验证之前，不暗示远程发布、远程 CI 或全新远程安装状态已经成立。

## 归属说明

这是一个受 Skill Creator Pro 和 Matt Pocock-inspired Skill Writing Guidelines 启发的独立项目。它不是 OpenAI 或 Matt Pocock 的官方材料，也不暗示任何背书。详见 [NOTICE.md](./NOTICE.md)。

## 许可证

[MIT](./LICENSE)
