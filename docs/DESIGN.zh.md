# Skill Polisher 设计记录

[English](./DESIGN.md)

本文解释当前维护生命周期及其保持投入合宜的权衡。运行时指令仍以
[`SKILL.md`](../skills/skill-polisher/SKILL.md) 为唯一权威来源。

## 行为契约

| 阶段 | 代表性请求 | 可观察的成功条件 | 失败或交接行为 |
|---|---|---|---|
| Review | “为什么这个既有 Skill 会误触发？” | 只读、可决策的证据包，包含稳定 finding 与证据边界 | 没有获授权的证据路径时返回 `NON_DURABLE` ledger |
| 决策 | “现在修 SP-002，暂缓 SP-003。” | finding 级决策、顺序、范围和 baseline 明确 | 沉默保持 `PENDING`；范围改变后刷新授权 |
| Polish | “执行获批的 SP-002 批次。” | 最小 diff、定向证据、未改项、达成效果和残余风险已记录 | 批次后停止；不冒充完成全面 Recheck |
| Recheck 确认 | “候选已经提交。” | 询问是否执行完整 Recheck 并等待 | commit、交接或 Polish 完成只是信号，不是同意 |
| Recheck | “现在执行完整 Recheck。” | 每项 ledger finding 与受影响 contract surface 都获得当前证据 | 剩余问题返回决策门 |
| Release Drift | “安装副本是否与 release 一致？” | source、version、CI、remote 与 installed 状态保持分开 | 发布就绪要求当前 runtime Recheck |
| 重建交接 | “这个 Skill 需要新身份和新架构。” | Polisher 提供行为契约与受保护不变量 | Skill Creator Pro 负责重建和首次发布 |

近似但不应触发的任务包括审核普通应用代码、润色论文，以及从重复工作流创建新 Skill。这些任务属于对应领域工作流或 Skill Creator Pro。

## 设计决策

### 生命周期，而不是模式选择器

Review、Polish、Recheck 与 Release Drift 都可以成为合法入口，但它们不是可互换的权限。宽泛改进从 Review 开始；Polish 消费用户批准的 finding；Recheck 消费已提交候选与明确确认；发布就绪消费当前 Recheck。已经明确获批的 finding 可以直接进入 Polish，不重复无关 Review。

### 只读 Review 与可审阅工件

Review 保持目标不变，但仍必须生成用户可检查的材料。Maintenance Ledger 只写入已经获授权的证据位置；没有该位置时，以 `NON_DURABLE` 形式返回完整 Markdown ledger。持久化证据不能静默扩大修改权限。

### 一份 ledger，分开的状态维度

一份 Maintenance Ledger 负责 finding、用户决策、Polish 批次、Recheck 结果和可选发布状态。它追加历史，不把事实复制到多个阶段文档。决策、实现进度和证据结果保持分开，因此 `decision: ACCEPT_RISK` 可以与 `recheck_outcome: OPEN` 同时存在。

### 显式 Recheck 确认

commit、完成的 Polish 批次、merge request、内部交接或准备发布会让 Recheck 变得合理，但不会启动它。Agent 提出一个聚焦问题并等待。用户当前消息已明确要求 Recheck 时，该消息已经满足门槛。确认绑定 runtime identity 与 material scope；runtime 变化后需要重新确认。

### 完整决策面覆盖，适度工具投入

Recheck 全面覆盖每项 finding、修改行为、受保护不变量、相关回归与 near miss，但不要求运行所有可用测试。Proportional rigor 仍负责选择工具；跳过与阻塞检查必须可见，每项 finding 都必须获得结果。

### Recheck 后的文档体系核对

Recheck 审核文档体系，但保持只读。它汇总 Review 到 Polish 的收尾情况与新增、调整、退役的能力，再按现有职责核对：README 负责当前行为，本文负责设计理由，Changelog 负责迭代历史，测试负责可执行合同，Maintenance Ledger 负责详细证据。缺口形成 finding；获批的纯文档修复只有在 runtime 内容不变时才保留当前 Recheck。

### 独立 drift audit 与发布顺序

Release Drift 仍可独立诊断源码、发布、CI 或安装不一致。但在发布路径中，它必须消费与精确 runtime 对应的当前 Recheck。runtime 修复会使 Recheck 失效；仅文档或版本的修复只重跑受影响 release gate。

### 独立维度与因果 finding

Contract、system、evolution 与 evidence 回答不同问题并保留独立 finding。大型套件可能因一个 runtime、权限或路径 adapter 产生许多失败；原始数量保留，但重复症状归并到最早有证据的共同原因。

### 不内置 runner 或 capability manifest

生命周期明确，但仍然小型且与工具无关。一个 reference 负责 ledger schema，仓库测试执行关键门槛。当前没有重复运行时操作值得新增 bundled script，也没有模块图值得引入 capability manifest。后续行为证据可以改变该决定。

## 证据基础

本设计应用两个相互独立的项目权威：

- [Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro) 提供行为契约、信息层级、前向测试、显式决策与发布工程。
- [Matt Pocock-inspired Skill Writing](https://github.com/Conradgui/matt-pocock-inspired-skill-writing) 提供十二条写作原则、持久工件模型和 proportional evidence 解释。

四个真实 Skill 系统提供架构证据：`paper-review` 支持不可变 ledger 与稳定 ID，`project-verifier` 支持独立状态维度，`zero-to-one-product-discovery` 支持阶段纯度，`immersive-motion-ui` 支持有证据成本的 manifest 与 verifier 边界。扩展的[真实仓库评估](./REAL_WORLD_EVALUATION.zh.md)记录命令和证据。

这些项目保持独立。本仓库不声称 Matt Pocock、OpenAI 或研究对象定义或认可 Skill Polisher 的工作流。
