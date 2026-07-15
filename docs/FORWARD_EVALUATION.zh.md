# 前向评估

[English](./FORWARD_EVALUATION.md)

本评估关注 Skill Polisher 能否对简单和成熟 Skill 应用预期的决策纪律，而不是为研究仓库打质量总分。三个研究仓库均未被修改。

## 证据边界

本次由开发会话将运行时工作流应用到原始仓库工件，并执行确定性的结构检查。没有使用全新的独立 Agent，没有修改研究仓库，没有重跑大范围跨平台测试，也没有查询当前远程 CI。因此，调用迁移能力以及完整的 Polish/Recheck 执行分支仍是发布前的证据缺口。

源码快照：

| 仓库 | 审核 revision |
|---|---|
| [`immersive-motion-ui-skill`](https://github.com/Conradgui/immersive-motion-ui-skill/tree/51f5adb9949c5c8731011637958fcdfc82128fd3) | `51f5adb9949c5c8731011637958fcdfc82128fd3` |
| [`project-verifier-skill`](https://github.com/Conradgui/project-verifier-skill/tree/df0bb00c06eae2a088c83ce45e51d64bbeb678f4) | `df0bb00c06eae2a088c83ce45e51d64bbeb678f4` |
| [`Academic-Paper-Review-Skill`](https://github.com/Conradgui/Academic-Paper-Review-Skill/tree/9f3288f7a13e25400a8ff0c00eeb16270e37fe98) | `9f3288f7a13e25400a8ff0c00eeb16270e37fe98` |
| [`skill-creator-pro`](https://github.com/Conradgui/skill-creator-pro/tree/eb23656e56ea3555599a6c5278a8b5834dc56b6d) | `eb23656e56ea3555599a6c5278a8b5834dc56b6d` |

每个研究 checkout 在被审核的 revision 上都保持 clean。

## 结果

### 1. 简单且完整的 Skill：及时停止，不增加仪式

刻意保持简单的 `release-note-cleaner` fixture 通过了 Skill Creator Pro 的结构 validator，quality lint 为零 warning。它已经明确规定结果、受保护事实、修改边界与可观察完成条件。

**决策：** 无 finding。审核在直接负责的运行时与 metadata 层停止。manifest、脚本套件、架构文档或大型 forward matrix 都不会改变当前决策。

这是防止过度工程化的主要测试案例。

### 2. Immersive Motion UI：识别通过迭代换来的模块化架构

运行时契约保证 Core 在没有可选 Library 时仍然完整，区分只读 `audit` 与会修改文件的 `redesign`，并使用精确的验证结果 token。capability manifest 将 14 个条件模块映射到 references、dependencies、fallbacks 与 verifiers。

**决策：** 将 capability graph 视为 learned invariant，而不是自动判定为 sprawl。它的路由面足够大，manifest 能让依赖与 fallback 漂移变得可检查。本次针对性审核没有证据支持高置信度的架构修改。

### 3. Project Verifier：保留独立状态维度

当前 Skill 与 artifact contract 分别记录 `phase_status`、`result_outcome`、`execution_scope` 和 `claim_eligibility`。V3 设计记录解释了为什么授权从完整计划 hash 收敛为 material decision envelope，同时保持 preflight 不进行真实调用。lean-core 删除记录表明旧机制经过判断，而不是默认保留。

**决策：** 这些都是 learned control-plane invariants。可安装 Skill 之外的历史 workbench 是演化证据，而不是运行时 sediment。本次审核不支持合并状态模型或删除历史。

### 4. Academic Paper Review：保护模式与复核契约，隔离一个局部缺陷

`paper-review` 分开 default review、delta review、reference audit 与 authorial polishing。其测试约束稳定 finding ID、精确复核状态和 evidence-bounded blind evaluation。这些机制保护科学结论不被编辑流程覆盖，也让复核可追踪。

本次直接复现了一个独立的结构缺陷：

- **SP-001 — 已确认 metadata 缺陷：** `paper-review/agents/openai.yaml` 的 `short_description` 为 65 个字符；当前 validator 接受 25–64 个字符，因此该字段导致运行时 Skill 结构验证失败。

**最小合理行动：** 只缩短这一项 metadata，并重跑直接 validator。没有证据表明这个局部问题需要重构 337 行的运行时 Skill。研究仓库保持只读。

### 5. Release drift：区分本地源码与安装状态

Skill Creator Pro 的运行时源码目录与全局安装副本各有 16 个文件。基于相对路径和 SHA-256 的比较在源码 revision `eb23656e56ea3555599a6c5278a8b5834dc56b6d` 上得到零条漂移记录。

**可支持结论：** 当前观察到的本地源码与安装副本逐字节一致。

**没有声称：** 当前远程 CI、tag、GitHub Release 或全新 installer replay。本次没有查询这些状态。

### 6. 本地安装：验证文档中的真实命令

使用 `skills@1.5.17` 运行了 `npx skills add . --skill skill-polisher --yes`。安装器验证本地路径，只发现一个 Skill，选择 `skill-polisher` 并完成项目本地安装。安装副本的 5 个运行时文件与源码的 5 个文件按相对路径和 SHA-256 完全一致。

安装器生成的 `.agents/` 内容和含绝对路径的 `skills-lock.json` 属于本地环境状态，已排除在仓库版本控制之外。

## 已执行检查

- 对 Skill Polisher、简单 fixture 与三个成熟运行时 Skill 执行 Skill Creator Pro `quick_validate.py`。
- 对 Skill Polisher 和简单 fixture 执行 Skill Creator Pro `quality_lint.py`。
- 直接检查运行时契约、harness metadata、条件 references、manifests、workbench 设计与删除记录，以及代表性测试。
- 检查每个研究仓库的 clean tree 与 revision。
- 按相对路径和 SHA-256 比较 Skill Creator Pro 源码与安装目录。
- 对 Skill Polisher 执行真实 `npx skills` 发现、本地安装和源码到安装副本的 hash 比较。

## 主动跳过的检查

- 研究仓库大范围测试套件：没有修改目标行为，且既往平台结果不会改变本次架构判断。
- 跨平台 replay：本轮只新增 Markdown/YAML Skill，没有运行时脚本或平台声明。
- 真实 Polish 或发布：研究仓库只是只读输入，远程修改不在任务范围内。
- 全新 Agent 的 trigger 与 near-miss 运行：本轮没有使用独立执行上下文。

下一道 release gate 应优先关闭最后一项缺口，然后执行一个获得授权的最小 Polish fixture 和一个 Recheck fixture。在此之前重复大范围测试，只会增加成本，而不能关闭当前最大的行为证据缺口。
