# Skill Polisher

> 为真实工作打磨 Agent Skill，而不是生产 lint 形状的评分表。

[English](./README.md) | 简体中文

Skill Polisher 是一个证据驱动、Codex 原生的既有 Agent Skill 审核与改进工作流。它把 Skill 视为持续演化的系统，重建其行为、职责、历史、测试与发布状态，保护 learned invariants，并且只执行证据能够支持的最小授权修改。

**这一层为什么重要：** Skill 的维护者决定了迭代产生的工程知识会持续积累，还是被表面清理意外抹去。

Review 默认只读。用户明确要求修复或改进指定本地 Skill 时进入 Polish；远程发布、凭据、真实系统副作用与新身份仍属于独立授权。

## 它解决什么问题？

既有 Skill 与新 Skill 不同。成熟 Skill 已经拥有 caller、状态、测试、发布副本，以及真实失败后形成的机制。只看当前快照的审核可能列出很长清单，却没有理解系统为什么能够工作。

| 常见审核失败 | 对成熟 Skill 的风险 | Skill Polisher 的应对 |
|---|---|---|
| 只判断当前 `SKILL.md` | learned gate 和 adapter 被误判为意外复杂度 | 重建 caller、artifact、history、test 与 release state |
| 把每个 lint warning 当缺陷 | 安全语言和分支契约变成高噪声误报 | 目标自有 contract evidence 优先，lint 只作补充 |
| 独立统计每个失败测试 | 一个缺失 runtime 或路径 adapter 变成几十个“bug” | 先归因非通过结果，再折叠到共同因果 finding |
| 追求最大测试覆盖 | 小改动浪费不成比例的时间与工具 | 使用足以改变诊断、行动或结论的最小证据 |
| 把用户给出的原因当最终结论 | 补丁解决了用户解释，而不是观察到的问题 | 将 symptom 视为证据，将 cause 视为待验证假设 |
| 只报告问题 | 维护者看不到补丁必须保护什么架构 | 同时报告 `Preserve`、`Change` 和 `Evidence limits` |
| 让 review 静默变成重写 | 范围和权限在没有决策时扩大 | Review 只读，Polish、Recheck 与 rebuild handoff 明确分支 |
| 把本地有效当成发布有效 | source、metadata、docs、CI、publication 与 install 漂移 | 分别审核每种 release state |

目标不是让每次审核都很大，而是让每个重要维护决策都可追溯且投入合宜。

## 边界：Creator Pro 与 Skill Polisher

Skill Polisher 是 [Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro) 的维护侧对应物。两者边界有意保持清晰：

| 边界 | Skill Creator Pro | Skill Polisher |
|---|---|---|
| 起点 | 重复工作流、新能力、fork，或以新身份重建 | 已有身份、真实工件和行为历史的既有 Skill |
| 核心问题 | 新 Skill 应实现什么行为契约，如何完成首次发布？ | 当前 Skill 为什么这样运行，什么应保留，什么值得修改？ |
| 核心产出 | 新的、已验证、已前向测试、可安装 Skill 与首次发布 | 证据化审核与可选的最小授权补丁 |
| 默认修改行为 | 构建新工件 | 只读审核 |
| 演化历史 | fork/rebuild 时作为源码证据 | 区分 learned invariant 与 sediment 的核心证据 |
| 发布职责 | 首次打包与发布 | 既有 release 的漂移审计与维护 |

如果打磨过程发现必须建立新身份或整体重建，Polisher 会把行为契约和受保护不变量交给 Creator Pro，而不是把重建伪装成补丁。

## 从快照 lint 到活系统维护

Skill Polisher 延续“skills for real engineers”的方向：用户控制、反馈、证据、架构和可维护性，比一份看起来完整的 Prompt 更重要。

成熟审核需要回答：

- 这个 Skill 真正拥有哪个结果和哪些触发分支？
- 哪个 caller、router、adapter、state artifact 或 release copy 依赖该契约？
- 哪个机制在保护过去的失败或来之不易的决定？
- 哪一层才是真正重复、过期、不可达或不再被执行的 sediment？
- 失败检查说明的是 Skill、test harness、环境，还是缺失权限？
- 仍能改变决策的最小证据集是什么？
- 即使不需要补丁，哪些内容也必须明确保留？

## 塑造 Skill Polisher 的十二条原则

Skill Polisher 应用了 [Matt Pocock-Inspired Skill Writing Guidelines](https://github.com/Conradgui/matt-pocock-inspired-skill-writing) 中的独立十二条综合原则。这不是 Matt Pocock 官方撰写或认可的原则清单。

| # | 原则 | 在维护中的落实 |
|---|---|---|
| 1 | 优化过程可预测性 | 固定 source order、evidence rule、stop condition 与 handoff |
| 2 | 分离 primitive 与 orchestration | 分别审核职责、caller、router、adapter 与 artifact |
| 3 | 把 description 当分支索引 | 判断 prose 前先重建 trigger 与 near miss |
| 4 | 用 leading word 压缩行为 | 精确使用 proportional rigor、learned invariant、sediment 与 causal collapse |
| 5 | 用可观察标准结束重要步骤 | scope、evidence、finding 与 patch 都有可检查完成条件 |
| 6 | 在昂贵工作前 cheap fail-fast | 先确定 target、authority、revision 与直接 validator |
| 7 | 分开可发现事实与用户决定 | 自己检查文件和历史，只询问选择、优先级与授权 |
| 8 | 用专用 artifact 持久化状态 | 尊重 ledger、manifest、workbench、receipt 与稳定 finding ID |
| 9 | 渐进披露分支上下文 | 只有修改或 release drift 分支触发时才加载对应 reference |
| 10 | 隔离独立判断维度 | 分开 contract、system、evolution 与 evidence 结论 |
| 11 | 正向控制并设计负空间 | 明确 preservation、mutation、approval 与 stopping boundary |
| 12 | 持续剪枝 | 删除已证明的 sediment，不误删 learned safeguard |

**Proportional rigor** 是十二条原则之上的横向纪律，不是第十三条：

> 严谨不是最大投入，而是针对当前决策风险的最小充分证据。

## 改进了什么？

### 1. 活的行为契约

审核从 outcome、trigger branch、near miss、input/state、output/side effect、authority gate、success evidence 与 failure behavior 开始，然后把共享 behavior、artifact、adapter、caller、route 和 release claim 分配给唯一 owner。

### 2. 感知演化的诊断

在简化复杂机制前，Polisher 会查找引入它的 requirement、failure、decision、test 或 migration。有证据保护真实问题的是 **learned invariant**；只有证据表明内容重复、过期、不可达或不再被执行时，才称为 **sediment**。历史缺失属于 evidence limit，而不是猜测许可。

### 3. 独立审核维度

审核保留四项独立判断：

- **Contract：** invocation、outcome、branch、authority 与 completion。
- **System：** ownership、caller、state、gate、adapter 与 release boundary。
- **Evolution：** learned invariant、sediment、compatibility constraint 与 rejected scope。
- **Evidence：** test、trace、reproducibility、claim eligibility 与 unsupported assertion。

不使用综合总分，避免优秀文档掩盖坏掉的 caller，或大量测试掩盖错误的产品结果。

### 4. 失败归因与共同原因折叠

每个非通过检查首先归因到 target behavior、harness/adapter、未满足的环境前提或不可用证据。原始测试数量保留，但重复症状会归并到有证据的最早共同原因。

这能避免一个缺失的 `bash`、一个 Windows symlink privilege 或一个错误路径转换被写成几十个虚构架构缺陷。

### 5. 适度验证

风险来自用户影响、受影响 branch/caller、状态或授权、外部副作用、可回滚性、不确定性和已发布用户依赖，而不是改动行数。

从最便宜的直接证据开始。只有下一项检查可能改变诊断、修改或结论时才扩大。原始行为已有证据、高影响不确定性已解决、下一项检查无法改变决策时即可停止；主动跳过的检查如果限制结论，需要明确报告。

### 6. Review、Polish 与 Recheck 边界

| 模式 | 结果 | 修改行为 |
|---|---|---|
| **Review** | 诊断行为、架构、演化与证据 | 只读 |
| **Polish** | 应用证据支持的最小改进 | 需要明确本地请求 |
| **Recheck** | 根据变更工件复核稳定 finding | 除非另行要求修复，否则只读 |
| **Release drift** | 比较 runtime、repository、metadata、version、CI、publication 与 installation | 默认只读 |

Polish 会保护无关用户修改，并只记录本次编辑真正可能伤害的不变量。小 metadata 修复只需要一条简短不变量说明，而不是仪式化账本；高后果状态、主张、标识、引用或授权才可能需要持久 ledger。

### 7. 维护决策简报

每个实质结果首先给出：

- **Preserve：** 应继续保护的 learned invariant 与清晰边界；
- **Change：** 值得交付成本的证据化 finding；
- **Evidence limits：** 会限制结论的缺失检查或权限。

可复核 finding 使用稳定 ID、直接证据、影响、置信度和最小合理行动。证据支持时，无修改也是有效结论。

### 8. 将 release drift 视为可观察状态

Polisher 分别报告 runtime source、harness metadata、repository contract、version intent、remote publication、CI 与 installed copy。clean local tree 不证明已发布，tag 不证明已安装，安装成功也不证明内容与当前源码逐字节一致。

## 真实测试集

四个公开仓库被固定到确切 revision、保持只读，并按各自契约进行适度测试：

| 仓库 | 应保护的架构 | 实际测试结果 | 可行动 finding |
|---|---|---|---|
| [`Academic-Paper-Review-Skill`](https://github.com/Conradgui/Academic-Paper-Review-Skill) | review/polish、双判断轴、不变量账本、稳定 delta ID | contract 28/28；proofing 10/10；完整套件 92/95，三项 Windows symlink error | 65 字符 metadata；权限感知的隔离认证测试 |
| [`zero-to-one-product-discovery`](https://github.com/Conradgui/zero-to-one-product-discovery) | Controller 路由、阶段纯度、child-skill contract、窄 workbench state | unit 71/71 | 106 字符 metadata |
| [`project-verifier-skill`](https://github.com/Conradgui/project-verifier-skill) | 四阶段控制面、decision envelope、独立状态维度 | 静态 contract 11/11；Windows 完整套件 27/105 | 声明或适配 Bash 与 `python3` 维护 runtime |
| [`immersive-motion-ui-skill`](https://github.com/Conradgui/immersive-motion-ui-skill) | Core/Library、14-capability manifest、audit/redesign、evidence token | manifest CLI 与 data UI 通过；十个所选命令共享一个 Windows 路径根因 | 替换 16 处不安全 file-URL 转换 |

测试集直接强化了 Skill Polisher 的失败归因、共同原因折叠、目标自有证据优先级和 `Preserve / Change / Evidence limits` 简报。它没有证明需要新增 mode、manifest、强制风险等级或 bundled runner。

完整 pinned revision、命令、finding ID、原始数量、因果归并和跳过项见[真实仓库评估](./docs/REAL_WORLD_EVALUATION.zh.md)。

## 安装

Skill Polisher 当前仍是本地预发布仓库。只有远程发布和 fresh install 真正通过后，才会补充公开远程安装命令。

### 方式 A：从本地仓库使用 Agent Skills installer

在仓库根目录运行：

```bash
npx skills add . --skill skill-polisher
```

`skills@1.5.17` 已验证该结构只发现一个可安装 Skill。

### 方式 B：手动复制到 Codex

将 `skills/skill-polisher` 复制到 `$CODEX_HOME/skills/skill-polisher`；如果未设置 `CODEX_HOME`，则复制到 `~/.codex/skills/skill-polisher`。安装后重启或开始新的 Codex turn，以便发现新 Skill。

## 使用

只读审核：

```text
使用 $skill-polisher 审核这个既有 Skill，解释其架构和演化，不要修改文件。
```

执行已确认的最小修复：

```text
使用 $skill-polisher 修复本地 Skill 的 SP-002，保护已有不变量；除非发现更大风险，只验证受影响行为和 near miss。
```

复核稳定 findings：

```text
使用 $skill-polisher 根据当前 revision 复核 SP-001 和 SP-003，并保留它们的 ID。
```

审核 release drift：

```text
使用 $skill-polisher 比较这个 Skill 的源码、metadata、发布状态、CI 与安装副本。
```

如果任务是创建新能力或以新身份重建，请使用 `$skill-creator-pro`。

## 仓库结构

```text
skill-polisher/
├── README.md
├── README.zh.md
├── CHANGELOG.md
├── LICENSE
├── NOTICE.md
├── docs/
│   ├── DESIGN.md
│   ├── DESIGN.zh.md
│   ├── REAL_WORLD_EVALUATION.md
│   └── REAL_WORLD_EVALUATION.zh.md
├── tests/
│   ├── BEHAVIOR_CASES.md
│   └── fixtures/release-note-cleaner/
└── skills/skill-polisher/
    ├── SKILL.md
    ├── license.txt
    ├── agents/openai.yaml
    └── references/
        ├── polish-and-recheck.md
        └── release-drift.md
```

可安装目录只包含运行时材料；人类文档、设计证据和测试 fixture 位于目录之外。英文运行时文件是语义唯一事实来源，中文人类文档只同步项目信息，不新增运行规则。

## 兼容性与当前证据

- 主要目标：Codex Skill format 与 `agents/openai.yaml`。
- 调用模式：对普通既有 Skill 诊断和维护请求允许隐式调用。
- 运行依赖：除了 active agent 的常规仓库与测试工具之外，无额外依赖。
- 当前运行时规模：约 130 行 `SKILL.md` 和两个条件 reference；当前没有证据支持 bundled script 或 capability manifest。
- 本地结构与 quality lint：本轮迭代后零 warning 通过。
- 本地 `npx skills` 安装：之前已验证只发现一个 Skill 且源码到安装副本零漂移；运行时变化后会重新检查。
- 真实仓库证据：当前 Windows 环境中的四个 pinned repository。
- 尚未声称：public remote、remote CI、tag、GitHub Release、fresh-remote install、Linux/macOS 执行或全新独立 Agent invocation transfer。

## 归属与独立性

Skill Polisher 是一个受 [Skill Creator Pro](https://github.com/Conradgui/skill-creator-pro) 和独立 [Matt Pocock-Inspired Skill Writing Guidelines](https://github.com/Conradgui/matt-pocock-inspired-skill-writing) 启发的独立项目。它不是 OpenAI 或 Matt Pocock 的官方材料，也不暗示任何背书。

四个公开测试仓库仍是独立项目。将其作为只读证据不代表它们定义或认可 Skill Polisher。详见 [NOTICE.md](./NOTICE.md)。

## 许可证

MIT，见 [LICENSE](./LICENSE)。
