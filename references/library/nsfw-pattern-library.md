# NSFW Prompt Pattern Library — Migrated from Legacy

## Purpose

This is the NSFW-focused production knowledge layer of the clean successor Skill.

The legacy project contained:
- NSFW prompt experiments;
- POV-specific prompt patterns;
- pose/action reference organization;
- camera/shot recipes;
- phase and timing experiments;
- reference-role experiments;
- successful and unverified prompt samples.

The successor does not copy explicit sexual prompt text verbatim. It migrates the reusable **prompt engineering structure and evidence metadata**.

## Legacy source inventory

Primary legacy sources audited:
- `PROJECT/ACTIVE-SKILL/h3-prompt-skill-current/references/poses/`
- `PROJECT/SKILL_OPTIMIZATION-技能优化/PW-OPT-001-优化skill--参考别人的github技能skill/GROK/`
- `PROJECT/WORKSPACE-工作区/PROMPT_WRITING-提示词编写/`
- `baseline/H3NSFW提示词技能skill第三版-V1-5-patch-optimize/references/poses/`
- `baseline/.../references/position-templates.md`
- `baseline/.../references/third-person-pov-guide.md`
- `baseline/.../references/v31-five-dim.md`
- `baseline/.../references/camera-lighting-shot.md`
- `references/experiences/01_镜头与摄影`
- `references/experiences/02_动作与运动`
- `references/experiences/03_阶段与时序`
- `references/experiences/04_人物与表演`
- `references/experiences/05_参考图与角色`
- `references/experiences/06_声音与对白`
- `references/experiences/07_场景与环境`
- `references/experiences/08_提示词结构`
- `references/experiences/09_综合经验`

## Migrated NSFW capability map

### 1. Adult action decomposition

NSFW actions must be represented as explicit observable state changes rather than vague labels.

Reusable structure:
`INITIAL STATE → CONTACT / TRIGGER → ACTION → INTERMEDIATE STATE → FINAL STATE`

The compiler must preserve the user's requested action chain while avoiding invented intermediate actions.

### 2. Position / body-state representation

Legacy position knowledge is migrated as a **body-state and spatial-relation compiler**, not as a literal explicit pose catalog.

Represent:
- subject identity;
- relative body orientation;
- support/contact surfaces;
- limb placement when explicitly requested;
- relative position between subjects;
- movement direction;
- resulting state.

Do not infer additional sexual activity from a body configuration.

### 3. POV and camera

Legacy NSFW material contained first-person and third-person variants.

Migrated rule:
- POV identity is independent from camera movement;
- first-person POV does not authorize camera motion;
- third-person placement does not authorize reframing;
- camera changes must be explicitly requested or justified by continuity repair.

### 4. Phase / sequence control

Legacy multi-step adult prompts are represented through:
- Phase A;
- explicit Transition;
- Phase B;
- state lock at each boundary.

A later action cannot appear before its prerequisite state is established.

### 5. Reference roles

Legacy reference workflows are normalized into:
- identity / appearance;
- environment;
- motion / choreography;
- camera / POV;
- voice timbre / delivery;
- visible text;
- endpoint frame.

Reference assets never contribute unrelated adult actions merely because those actions appear in the source material.

### 6. Dialogue and sound

Legacy adult prompt work is migrated into:
- speaker identity;
- exact user-provided dialogue;
- voice timbre / delivery;
- diegetic soundscape;
- non-diegetic music.

An audio reference assigned for voice characteristics does not supply dialogue or scene content.

### 7. Prompt density

Legacy experiments reinforce a core rule:

**Do not maximize prompt length. Maximize preservation of mandatory semantic constraints.**

For short H3 generations:
1. mandatory adult action/state;
2. mandatory transition;
3. mandatory dialogue/performance;
4. mandatory camera/POV;
5. continuity constraints;
6. only then optional descriptive detail.

### 8. Optimization behavior

Legacy prompt optimization is now compiled as:

`EXTRACT → PRESERVE → NORMALIZE → OPTIMIZE → RECOMPILE`

Optimization may improve:
- ordering;
- observability;
- temporal clarity;
- subject references;
- camera grammar;
- action continuity.

Optimization may not silently:
- remove required adult semantics;
- add new adult actions;
- add participants;
- add props;
- add camera movement;
- add duration;
- alter dialogue.

## Evidence status

Legacy material is divided into:
- **validated structural lesson** — safe to use as compiler behavior;
- **experience candidate** — requires explicit approval before becoming a default;
- **historical sample** — evidence only;
- **unverified prompt** — never treated as a rule.

A successful old prompt is not automatically a new Skill rule.

## Important distinction

The new Skill is NSFW-focused, but it is not a literal archive of explicit sexual prompt text.

Its job is to make the user's requested adult scene compile more faithfully and consistently into MiniMax H3, especially with:
- multi-subject scenes;
- POV;
- reference images;
- phase isolation;
- action continuity;
- dialogue;
- timing;
- camera control;
- prompt optimization.

## Core principle

**补该补的，不该补的绝不补。**

For NSFW prompts this is especially important: the compiler must preserve what the user actually specified without turning old examples into permission to invent more.
