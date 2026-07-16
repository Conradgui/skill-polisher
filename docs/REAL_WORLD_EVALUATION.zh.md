# 真实仓库评估

[English](./REAL_WORLD_EVALUATION.md)

> **历史证据快照：** 以下结果记录固定 revision，以及一次开发会话当时可用的 Windows、模型和工具环境。它们用于保存因果证据，不构成当前兼容性矩阵、跨平台认证或当前模型 benchmark。

Skill Polisher 使用四个独立开发的公开 Skill 仓库作为只读测试对象：

1. [`Conradgui/Academic-Paper-Review-Skill`](https://github.com/Conradgui/Academic-Paper-Review-Skill/tree/9f3288f7a13e25400a8ff0c00eeb16270e37fe98)
2. [`Conradgui/zero-to-one-product-discovery`](https://github.com/Conradgui/zero-to-one-product-discovery/tree/b4556c895ba8c38af22c3662f326a1b45f1d434e)
3. [`Conradgui/project-verifier-skill`](https://github.com/Conradgui/project-verifier-skill/tree/df0bb00c06eae2a088c83ce45e51d64bbeb678f4)
4. [`Conradgui/immersive-motion-ui-skill`](https://github.com/Conradgui/immersive-motion-ui-skill/tree/51f5adb9949c5c8731011637958fcdfc82128fd3)

四个 checkout 均与 GitHub `main` 一致，并在测试前后保持 clean；没有修改任何研究仓库。

## 评估问题

本次测试不是“Polisher 能产生多少 lint warning”，而是判断它能否：

- 重建四种不同 Skill 架构的行为与职责契约；
- 识别迭代换来的机制，而不是把复杂度自动视为债务；
- 让目标仓库自己的契约证据优先于外部 heuristic；
- 区分目标缺陷、测试 harness、平台、权限和缺失证据；
- 将许多重复症状折叠到有证据的最早共同原因；
- 在证据不足时停止，而不是强行推荐架构修改。

## 证据标签

| 标签 | 含义 |
|---|---|
| **Preserve** | 当前工件与测试支持的 learned invariant 或清晰边界 |
| **Change** | 有证据支持最小行动的确定缺陷或风险 |
| **Evidence limit** | 会限制结论的 runtime、权限、平台、付费调用或独立上下文缺口 |

外部 lint warning 只是审核提示，不自动成为 finding。

## 总览

| 仓库 | 目标自有证据 | Preserve | Change |
|---|---|---|---|
| Academic Paper Review | Skill contract 28/28、proofing 10/10；完整套件 92/95，三项为 Windows symlink error | 模式路由、科学/文本双轴、不变量账本、稳定 delta ID、外部检索 opt-in | 65 字符 Codex 简介；让隔离认证测试感知 Windows 权限 |
| Zero-to-One Product Discovery | 71/71 unit 通过 | Controller 路由所有权、阶段纯度、child-skill 边界、窄 workbench 状态、schema 化导出与 revision trace | 106 字符 Codex 简介 |
| Project Verifier | 静态契约 11/11；当前 Windows 环境完整套件 27/105 | 四阶段控制面、decision envelope、无真实调用 preflight、独立状态维度 | 声明或适配导致 73 failure 与 5 error 的 Bash / `python3` 维护 runtime |
| Immersive Motion UI | manifest CLI 与 data-UI 15/15 通过；其余十个所选命令在同一路径族失败 | Core/可选 Library、14 capability graph、audit/redesign、精确 evidence token | 修复运行时与测试工具中的 16 处 Windows 不安全 file-URL 转换 |

## 1. Academic Paper Review

### Preserve

仓库包含两个相关但职责不同的 Skill。`paper-review` 负责稿件审核、delta review、reference audit 和明确请求的 authorial polishing；`latex-paper-review` 负责 LaTeX 专项边界。`paper-review` 中：

- 科学性审核与文本质量审核保持独立；
- review 只读，polishing 保护主张、数字、公式、引用和标签；
- delta review 保留 finding ID 和精确 status；
- 外部文献检索为 opt-in；
- blind evaluation 约束源码证据与候选输出。

因此，337 行运行时不能仅因长度被判定为缺陷。当前契约测试直接保护这些边界。

### Tests

- Skill Creator Pro 结构验证：`paper-review` 只有一项 metadata 失败；`latex-paper-review` 通过。
- `test_skill_contract.py`：28/28 通过。
- `test_proofing_scan.py`：10/10 通过。
- 完整本地套件：95 项中 92 通过、3 error。

三项 error 都发生在 forward-evaluation harness 为隔离 Codex/Judge home 创建认证 symlink 时。当前 Windows 进程没有 symlink privilege，返回 `WinError 1314`。没有稿件审核、proofing、evaluator 或 contract assertion 失败。

### Change

- **APR-001 — 确定 metadata 缺陷：** `paper-review/agents/openai.yaml` 的 `short_description` 为 65 个字符，Codex validator 接受 25–64。只需缩短该值并重跑直接 validator。
- **APR-002 — 维护可移植性缺口：** Windows 隔离认证测试依赖 symlink privilege。可明确声明前提、精确 skip，或使用另行审核的低权限 adapter；不应静默复制凭据。

Quality lint 报告的集中否定措辞和超过 300 行只是信号。目标自有测试表明其中许多 guardrail 保护真实审核与编辑边界。

## 2. Zero-to-One Product Discovery

### Preserve

这是测试集中最强的 orchestration 压力案例。主 Skill 负责 stage gate 与用户体验；本地 child-skill contract 只能产出有边界的工件，不能选择下一阶段或互相调用。Controller 独占路由权，producer status 只是 signal 而不是 decision。

Runtime Workbench 保存当前决策状态，不保存 transcript 历史。导出 manifest、execution handoff、revision trace、controller action 与 evidence maturity 由 schema 和确定性脚本约束；公开 eval runs 位于可安装运行时之外。这些是清晰职责与状态边界，不是按文件数量拆分 Skill 的理由。

### Tests

- Unit suite：71/71 通过，用时 0.531 秒。
- 覆盖 schema、workbench persistence、provider error、artifact manifest、revision boundary、execution handoff 与 phase-three response checker。
- Skill Creator Pro 结构验证只有一项 metadata 失败。

Integration tests 需要 `DEEPSEEK_API_KEY` 或 `MIMO_API_KEY`，因此主动跳过。判断本地契约和 metadata 不需要真实 provider 调用。

### Change

- **Z2O-001 — 确定 metadata 缺陷：** `agents/openai.yaml` 的 `short_description` 为 106 个字符。应换成 25–64 字符简介，把较长分支信息保留在 `SKILL.md` 和 `default_prompt`。

Heuristic lint 报告的 37 行否定措辞不是 37 个 finding；其中很多由 unit suite 证明是在保护阶段纯度、用户权限、工件资格与 controller 所有权。

## 3. Project Verifier

### Preserve

约 30 行的 `SKILL.md` 是四个条件 stage reference 之上的稳定薄契约。控制面分别保存：

- `phase_status`：流程进度；
- `result_outcome`：证据结果；
- `execution_scope`：none、plan-only、pilot 或 full；
- `claim_eligibility`：证据允许支持的 claim。

Decision envelope 绑定 material authorization、source revision、capability、限制与副作用范围。Preflight 不进行真实模型、扫描、API 或 target 调用。Lean-core 删除记录与 V3 设计历史解释了这些结构为什么存在，以及哪些旧机制已经移除。

### Tests

- Skill Creator Pro 结构验证：通过。
- 静态 `test_contract.py`：11/11 通过。
- 完整文档套件：105 项中 27 通过、73 fail、5 error。

78 个非通过项不等于 78 个 Project Verifier 缺陷。5 个 error 来自缺少 `bash`；大部分 failure 继续共享 `python3` 命令，该命令在 Windows 上命中 Microsoft Store alias，而不是当前 Python 3.12。这是维护 runtime 和 adapter 边界，静态 Skill contract 仍为绿色。

### Change

- **PV-001 — 仓库测试 runtime 缺口：** 明确声明 Bash 与可用 `python3` 为支持的维护环境，或通过 active interpreter 调用 Python 并增加 Windows runner adapter。在此之前，README 的 unit-suite 命令不能直接支持普通 Windows Python 安装。

这个 finding 不支持合并四阶段架构或独立状态维度；设计历史和直接 contract test 都支持这些机制。

## 4. Immersive Motion UI

### Preserve

没有可选 MotionSites Library 时，Core 仍然完整。14-capability manifest 将 active module 映射到 trigger、本地 reference、dependency、fallback 和 verifier。`audit` 只读；`redesign` 在定向修改前保护现有结构。验证使用精确的 `PASS`、`PASS WITH FINDINGS`、`FAIL` 与 `NOT EXECUTED`。

这个路由面足够大，机器可读 manifest 已经证明其成本合理。没有证据支持把它改回纯 prose，或把可选 Library 变成硬依赖。

### Tests

从 README 选择了十二个零依赖命令：

- capability-manifest CLI：通过；
- data-UI：15/15 通过；
- core package、capability-manifest tests、routing、industry、casebook、minimal showcases、browser evidence、commerce、specialty 与 trigger：失败。

十个失败命令共享同一路径族。16 个 JavaScript 文件在本地路径操作前使用 `new URL(..., import.meta.url).pathname`。Windows 会产生 percent-encoded 或 `/C:/...` 形式，随后得到 `C:\C:\...`，使有效文件被报告为缺失。原始命令结果仍是十个失败，但应折叠成一个因果 finding。

### Change

- **IMUI-001 — 确定跨平台路径缺陷：** 在全部 16 个运行时与测试文件中使用 `fileURLToPath(import.meta.url)`，再通过 `path.dirname` / `path.resolve` 派生路径。修复后重跑十个被阻塞套件；在共同前提修复前，不能声称其下游行为通过。

外部 lint 只发现 `verify-ui-evidence.mjs` 的运行时点；必须运行仓库级测试，才能看到维护工具的完整影响范围。

## 测试集如何反哺 Skill Polisher

四个仓库带来了四项直接运行时优化：

1. **创建 finding 前先归因。** 分开目标行为、harness/adapter、环境前提和不可用证据。
2. **共同原因折叠。** 保留原始测试数量，但把重复症状归并到最早的证据化原因。
3. **目标自有证据优先。** Contract 和 regression test 能说明 guardrail 为什么存在；外部 lint 只是补充。
4. **维护决策简报。** 用 `Preserve`、`Change` 和 `Evidence limits` 同时呈现应保护的架构与最小改动。

Skill Polisher 没有新增 mode、manifest、强制风险等级或 bundled runner。原工作流已经能表达这些审核，只需要更清晰的归因和报告规则。

## 执行命令

```text
python quick_validate.py <each runtime skill>
python quality_lint.py <each runtime skill>
python -m unittest discover -s tests -q
python -m unittest discover -s tests/unit -q
python -m unittest discover -s skills/project-verifier/tests -p test_*.py -q
node scripts/validate-core-package.mjs --pretty
node skills/immersive-motion-ui/scripts/validate-capability-manifest.mjs --pretty
node tests/<selected-suite>/run-tests.mjs
```

沙箱临时目录 ACL 曾导致与仓库无关的权限错误，因此 Python 套件随后在沙箱外本地复测。上文只报告复测结果。测试没有进行网络调用，也没有修改源码。

## 证据限制与主动跳过

- 没有启动付费 Codex、Claude、DeepSeek 或 MIMO forward run。
- 没有调用真实 API、安全目标、浏览器生产系统、凭据工作流或外部 issue tracker。
- 已阅读仓库既有 forward evaluation 作为历史证据，但没有把它们改称当前模型 benchmark。
- 只执行当前 Windows 环境，没有推断 Linux/macOS 结果。
- 测试由开发会话执行，不是全新独立 Agent 上下文。

这些限制不影响两个 metadata 长度 finding 或直接复现的 Windows runtime finding，但会限制关于跨模型 invocation 质量和修复后行为的结论。
