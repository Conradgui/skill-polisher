# Skill Polisher 设计记录

[English](./DESIGN.md)

本文解释 Skill Polisher 当前边界的原因，也说明为什么若干看似合理的机制被有意省略。运行时指令仍以 [`SKILL.md`](../skills/skill-polisher/SKILL.md) 为唯一权威来源。

## 行为契约

| 分支 | 代表性请求 | 可观察的成功条件 | 失败或交接行为 |
|---|---|---|---|
| Review | “为什么这个既有 Skill 会误触发？” | 给出有证据的 findings 或明确的无 finding 结论；不修改文件 | 只有在目标缺失或用户决定会改变结论时才提问 |
| Polish | “修复这个 Skill 已确认的路由问题。” | 最小 diff 恢复受影响契约并保留不变量 | 在远程、真实系统或新增范围的副作用前停止 |
| Recheck | “补丁完成后复核 SP-002。” | 稳定 finding ID 获得证据支持的当前状态 | 无法重建原始标准时报告 `BLOCKED` |
| Release drift | “安装副本与 release 是否一致？” | 分别说明源码、版本、CI、远程与安装状态 | 无法观察相关状态时收窄结论 |
| 重建交接 | “这个 Skill 需要新身份和新架构。” | Polisher 给出行为契约与受保护不变量 | Skill Creator Pro 负责重建和首次发布 |

近似但不应触发的任务包括审核普通应用代码、润色论文，以及把重复工作流创建成新 Skill。这些任务应交给对应领域工作流或 Skill Creator Pro。

## 设计决策

### 隐式调用

用户经常只会说“这个 Skill 总是误触发”，而不会知道产品名称。description 已限定为既有 Agent Skill，并覆盖每个真实维护分支，因此隐式调用所占用的上下文成本是合理的。

### 默认只读

诊断与修改属于不同权限。Review 请求只产出证据，不改变目标。明确要求本地修复时进入 Polish；发布、凭据与真实系统副作用仍需单独授权。

### 适度严谨，但不强制分级

风险并不由改动行数决定：一行授权规则可能比大段文档修改更重要。因此工作流判断“下一项检查能否改变诊断、行动或结论”，而不是给每项任务套用固定的 T0–T3 仪式。这是一条横向运行纪律，不是新增的写作原则。

### 独立维度，不计算总分

Contract、system、evolution 与 evidence 回答不同问题。合并成单一分数，会让优质文档掩盖坏掉的 caller，或者让大量测试掩盖错误的目标。每个 finding 都保留自己的维度和证据。

### 不内置脚本或 capability manifest

当前工作流是线性的，也不依赖特定工具。既有平台 validator 已能检查 Skill 结构，而证据采集会随目标仓库变化。目前没有反复出现的确定性操作值得新增脚本，也没有模块化路由图值得引入 manifest。后续前向证据可以改变这一决定。

## 证据基础

本设计应用两个相互独立的项目权威：

- [Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro) 提供行为契约、信息层级、前向测试与首次发布工作流。
- [Matt Pocock-inspired Skill Writing](https://github.com/Conradgui/matt-pocock-inspired-skill-writing) 提供十二条写作原则和 proportional evidence 的解释。

三个真实 Skill 系统提供了架构研究对象：

| 系统 | Skill Polisher 吸收的 learned invariant |
|---|---|
| `immersive-motion-ui` | capability graph、fallback 与 verifier 可能是迭代换来的架构，而不是多余复杂度 |
| `project-verifier` | progress、outcome、execution scope 与 claim eligibility 不能被合并 |
| `paper-review` | 审核与修改需要不同模式；编辑可能需要不变量账本；复核需要稳定 ID |

这些研究也暴露了只看快照的审核弱点：偶发的 Windows 问题可以是真问题，但未必是价值最高的架构结论。因此 Skill Polisher 会先排序行为和架构；只有平台行为违反明确支持声明时，才提高其优先级。

这些项目彼此独立。本仓库不声称 Matt Pocock、OpenAI 或三个研究仓库定义或认可 Skill Polisher 的工作流。
