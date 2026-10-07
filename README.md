# MiniMax H3 Prompt Skill

一个面向 **MiniMax H3 视频生成提示词编译、优化、修复与经验管理** 的 compiler-first Skill。

本项目的重点不是把提示词写得“更长”，也不是替用户擅自设计镜头和剧情，而是：

> **把用户已经授权的意图，稳定、清晰、可验证地编译成符合 MiniMax H3 模式与结构要求的可直接使用提示词。**

本项目同时以 **NSFW 场景的语义保持、动作连续性、阶段隔离、参考图角色隔离、POV / Camera 分离、提示词优化** 为核心生产能力，并逐步建立从图片/视频视觉证据到 H3 工程经验的受控学习链路。

---

## 1. 这个项目解决什么问题？

使用 H3 编写复杂提示词时，常见问题并不只是“提示词不够详细”，而是：

- 用户明确要求的内容在优化过程中被删掉；
- 模型为了让场景看起来完整，擅自补充用户没有要求的动作、镜头、道具或对白；
- Phase A / Transition / Phase B 相互泄漏；
- POV 被错误地当成 Camera Movement；
- 参考图中的背景、姿态或动作被错误带入；
- Audio Reference 的声音特征与对白内容混在一起；
- 修改一个局部问题时，整个 Prompt 被无关重写；
- 历史成功案例被错误地当成新的通用规则；
- 图片/视频观察到的内容未经验证就被提升为 Experience。

因此，本项目把 H3 Prompt Writing 当作一个**受约束的编译问题**，而不是自由创作问题。

---

# 2. 核心原则

## 补该补的，不该补的绝不补

这是整个项目最重要的原则。

如果用户没有授权：

- 新动作
- 新人物
- 新道具
- 新对白
- 新镜头
- 新机位
- 新灯光
- 新时长
- 新情绪
- 新剧情

Skill 不应仅仅因为“这样看起来更电影化”或“模型通常喜欢这样”就自行添加。

### 完整编译 ≠ 填满所有空白

Skill 的职责是：

> **完整表达用户的意图，而不是替用户创造新的意图。**

---

# 3. Semantic Authority（语义权威层级）

项目采用明确的语义优先级：

1. **用户当前请求与明确约束**
2. **用户明确指定的 Reference Role**
3. **MiniMax H3 官方模式 / Schema 要求**
4. **项目批准的 Skill 规则**
5. **用户明确批准的 Production Experience**
6. **Reference Knowledge / 已验证案例**
7. **模型自身推断**

低优先级信息不能覆盖高优先级信息。

尤其需要注意：

> **历史 Prompt、示例、模型习惯、常见做法，都不是新增剧情语义的授权。**

---

# 4. H3 Prompt Compiler

Skill 当前按照任务类型区分：

- **GENERATE** — 生成新的 H3 Prompt
- **REWRITE** — 将已有 Prompt 编译为 H3 结构
- **OPTIMIZE** — 在不改变意图的前提下优化
- **REPAIR** — 修复指定问题，并冻结无关维度
- **DIAGNOSE** — 分析问题，不擅自重写
- **EXPLAIN** — 解释 H3 概念或机制

核心编译流程：

```
USER INTENT
→ SCOPE LOCK
→ H3 MODE
→ REFERENCE ROLES
→ REQUIRED SCHEMA
→ EXTRACT
→ PRESERVE
→ NORMALIZE
→ NECESSARY LANGUAGE COMPILATION
→ H3 PAYLOAD
→ QA
```

这里的 **Necessary Language Compilation** 只负责把已经授权的内容表达得足够明确，不负责创造新的故事事实。

---

# 5. 支持的 MiniMax H3 模式

项目以官方 H3 模式为底层传输结构：

- **T2VA** — Text to Video
- **I2VA** — Image to Video
- **FL2VA** — First / Last Frame to Video
- **L2VA** — Last Frame to Video
- **Ref2VA** — Reference-based Video Generation

对于 Base Modes，遵循官方三字段结构：

```text
integrated_multimodal_description:
overall_soundscape:
non_diegetic_music:
```

Ref2VA 使用官方六段结构：

```text
subject_definitions:
summary:
retention_analysis:
detailed_description:
overall_soundscape:
non_diegetic_music:
```

项目不会因为某个任务属于 NSFW，就自行发明一个“第七种 H3 模式”。

**NSFW 是语义与编译控制层，不是新的 H3 Mode。**

---

# 6. NSFW 是本项目的核心生产能力

本项目是一个 **NSFW-focused H3 Skill successor**。

NSFW 能力并不是简单增加一层“成人内容描述”，而是重点解决复杂场景中的工程问题：

- Adult semantic preservation
- Action / body-state representation
- Spatial relationship
- POV / Camera separation
- Phase / Transition isolation
- Action continuity
- Reference-role isolation
- Dialogue / audio separation
- Prompt density optimization
- Multi-subject consistency
- Failure diagnosis and smallest-responsible-layer repair

核心结构仍然是：

```
INITIAL STATE
→ TRIGGER / CONTACT
→ ACTION
→ INTERMEDIATE STATE
→ FINAL STATE
```

并通过 Phase / Transition 控制避免后续动作泄漏到前一阶段。

### NSFW 的重要边界

历史 Prompt、示例或经验可以帮助理解“如何表达”，但不能自动授权 Skill 增加用户没有要求的内容。

因此：

> **经验可以改变 HOW，不能擅自改变 WHAT。**

---

# 7. Reference Role Lock

Reference Asset 不是“看到什么就全部继承什么”。

用户可以明确指定：

- Identity / Appearance
- Environment / Setting
- Motion / Choreography
- Camera / POV
- Voice Timbre / Delivery
- Visible Text
- First / Last Frame
- 其他明确属性

例如：

```
Picture 1 → Identity / Appearance
Picture 2 → Environment
Video 1   → Motion / Temporal Sequence
Audio 1   → Voice Timbre / Delivery
```

则每个 Reference 只能在其授权范围内提供信息。

这可以避免：

> “参考图里有某个动作，所以模型自动把这个动作带进当前场景。”

---

# 8. User-Directed Visual Learning

项目正在建立一个受控的 **Visual-to-H3 Experience Pipeline**。

核心原则：

> **用户决定 WHAT TO LEARN，系统决定 HOW TO OBSERVE / STRUCTURE / TEST / VALIDATE。**

Visual Learning 不是：

> “把图片/视频全部交给 AI，让 AI 自己学习。”

而是要求建立明确的 Learning Scope：

```
TARGET
SOURCE
RANGE
EXCLUDE
PURPOSE
```

例如：

```
TARGET:
action sequence

SOURCE:
Video 1

EXCLUDE:
camera
environment
appearance
dialogue

PURPOSE:
extract reusable H3 engineering pattern
```

此时被排除的 Camera / Environment / Appearance / Dialogue，即使视频中清晰可见，也不能自动进入 Experience Candidate。

### 图片与视频的证据定位

**图片主要提供 State Evidence：**

- 姿态 / Body State
- 空间关系
- 人物状态
- 环境状态
- Composition / Camera State

**视频主要提供 Transition / Temporal Evidence：**

```
INITIAL STATE
→ TRIGGER
→ ACTION
→ INTERMEDIATE STATE
→ FINAL STATE
```

但媒体类型不是学习范围的最终决定者。

**Learning Scope 才是硬边界。**

---

# 9. Visual Evidence 不等于 Active Experience

视觉学习采用分层证据：

- **O1** — Direct Observation
- **O2** — Reliable Structural Inference
- **H1** — H3 Engineering Hypothesis
- **V1** — H3 Experiment Validated
- **A1** — User-approved Active Experience

经验晋升：

```
CANDIDATE
→ VALIDATED
→ APPROVED
```

只有：

```
APPROVED
+
approved_by_user: true
```

才能影响未来 H3 Prompt 编译。

因此：

> **Observation ≠ Experience**

> **Validated ≠ Approved**

> **Grok / AI 分析结果 ≠ 自动 Skill Rule**

---

# 10. 历史 NSFW Prompt 资产与工程规则分离

本项目特别重视历史生产资产。

历史 Prompt、实验、失败案例和验证样例具有实际生产价值，因此不应因为“架构清理”而被简单删除。

项目将其分成三个不同层次：

```
Historical Prompt / Evidence
        ↓
Engineering Pattern
        ↓
Approved Active Experience
```

它们不能混为一谈。

### Historical Prompt

用于：

- 历史检索
- 复盘
- 对比
- 提取经验

### Engineering Pattern

提取可复用的方法，例如：

- Phase isolation
- POV / Camera separation
- Reference-role isolation
- Action continuity
- Prompt density
- Failure repair

### Approved Experience

只有经过验证并得到用户批准后，才能影响未来生成。

这种分层可以避免历史案例成为一个不受控制的“自动提示词库”。

---

# 11. Experience Governance

Experience Library 不是普通的 Prompt 收藏夹。

Experience 必须携带：

- Scope
- Applicability
- Exclusions
- Evidence
- Validation
- Model Context
- Traceability
- Approval Status

并区分：

- CANDIDATE
- VALIDATED
- APPROVED
- REVOKED
- SUPERSEDED
- STALE

尤其是：

```
approved_by_user: true
```

是 Active Experience 的重要授权条件。

---

# 12. QA 与 Regression

Skill 在输出 H3 Payload 前检查：

### Missing

用户明确要求的内容有没有丢失？

### Added

有没有加入用户没有授权的语义？

### Altered

有没有改变用户原本的意思？

### Contradicted

Prompt 内部有没有互相冲突？

### Structural

H3 Mode、字段、顺序、Reference Label、Speaker ID、Timing 是否符合要求？

### Purity

最终 Payload 是否混入了：

- Skill 内部规则
- QA 过程
- 实现细节
- 内部推理
- 编译器说明

---

# 13. 最小责任层修复

当 H3 生成出现问题时，不直接重写整个 Skill。

先确定问题属于哪个层：

```
Identity drift
→ Reference / Subject layer

Spatial relation flip
→ Blocking / Continuity

Posture collapse
→ Action / State

Timing error
→ Temporal

Missing transition
→ State Transition

Unwanted camera movement
→ Camera

Unwanted dialogue
→ Dialogue

Voice mismatch
→ Audio / Reference

Environment drift
→ Environment / Reference
```

然后：

```
Identify failure
→ Patch smallest responsible layer
→ Recompile
→ Semantic QA
→ Purity QA
```

这可以避免一个局部问题污染整个 Skill。

---

# 14. Prompt Library 与 Experience Library 分离

两者用途不同。

### Prompt Library

保存：

- Prompt
- 示例
- 实验结果
- 历史样本

### Experience Library

保存：

- 可复用工程规律
- 适用条件
- 排除条件
- 验证证据
- 模型上下文
- 用户批准状态

**Prompt 是资产。**

**Experience 是经过治理的知识。**

两者不能直接等价。

---

# 15. Repository Structure

当前仓库主要结构：

```
SKILL.md

references/
├── official/          # 官方 H3 Schema / 格式参考
├── compiler/          # 编译规则、语义边界、生产推理
├── temporal/          # 状态、Transition、Phase
├── camera/            # Camera Grammar
├── audio/             # Dialogue / Audio
├── qa/                # QA、失败修复、语义 Diff
├── library/           # Prompt / Experience / NSFW 知识层
└── visual-learning/   # User-Directed Visual Learning

tests/
├── cases.json
├── golden/
└── validation scripts
```

历史 NSFW 资料与当前 Compiler Rule 保持分离，以避免历史内容直接污染 Runtime。

---

# 16. 当前项目状态

当前项目属于：

**V1 Foundation / Compiler-first architecture**

当前 Regression 主要用于：

- 结构检查
- Schema 检查
- 语义边界
- Reference-role isolation
- Temporal / Phase isolation
- Prompt purity
- Experience governance
- Visual Learning rule surface

### 不做过度声明

本项目不会把静态 Regression 的通过结果描述成：

> “MiniMax H3 已经实际验证所有规则有效。”

真实 H3 生成实验需要单独记录证据。

因此：

```
Documented
≠
Runtime Wired
≠
Regression Tested
≠
H3 Experiment Validated
≠
User Approved
```

---

# 17. 适合谁？

这个项目适合：

- 使用 MiniMax H3 进行复杂视频生成的人；
- 需要稳定编写 Ref2VA / I2VA / FL2VA 等 Prompt 的用户；
- 经常处理多人物、多阶段、POV、Camera、Reference 的用户；
- 希望减少 Prompt 优化过程中语义丢失的人；
- 希望把实际生成经验整理成可治理 Experience 的用户；
- 希望从图片 / 视频中提取 H3 工程规律的人；
- 希望建立可回归、可维护 Prompt Skill 的开发者。

---

# 18. 设计哲学

这个项目最终追求的不是：

> **“让 AI 写得更多。”**

而是：

> **“让 AI 更准确地执行用户已经决定的事情。”**

因此项目始终坚持：

**Preserve before optimize.**

**Scope before generation.**

**Evidence before experience.**

**Validation before approval.**

**Approval before active reuse.**

以及最重要的一条：

> **补该补的，不该补的绝不补。**

---

## 官方 H3 参考

MiniMax H3 官方项目与当前模式说明应作为 H3 Schema / 模式要求的最高参考来源。

本仓库中的生产经验属于项目工程经验，不代表 MiniMax 官方行为保证。

