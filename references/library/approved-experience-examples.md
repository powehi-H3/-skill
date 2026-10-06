# Approved Experience Examples

This file contains deliberately small governance examples, not a prompt catalog.

## E-001 — Reference-role isolation

```yaml
experience_id: E-001
status: APPROVED
type: SUCCESS
category: reference
subcategory: role-isolation
title: Keep identity, environment, and voice references semantically separate
scope: Ref2VA
applicability:
  conditions:
    - multiple references have explicit roles
  exclusions:
    - a reference is explicitly assigned multiple roles by the user
observation: Separate role assignments reduce cross-reference contamination.
result: Identity, environment, and voice responsibilities remain isolated.
inference: Reference role locking is useful when several references are present.
reusable_lesson: Enforce explicit reference roles and import only the authorized semantic payload.
validation:
  method: offline-golden-regression
  evidence: tests/golden/pov-reference-role.expected.txt
  attempts: 1
  successes: 1
approval:
  approved_by_user: true
  approved_at: project-migration
model_context:
  model_version: MiniMax-H3
  skill_version: clean-successor
  created_at: project-migration
  last_validated: project-migration
reference_budget:
  weight: MEDIUM
traceability:
  source_project: legacy-migration
```

## E-002 — Smallest responsible repair

```yaml
experience_id: E-002
status: APPROVED
type: REPAIR
category: repair
subcategory: edit-scope
title: Camera-only changes should freeze unrelated semantics
scope: all H3 modes
applicability:
  conditions:
    - user explicitly requests a camera-only edit
  exclusions:
    - user also requests changes to subject action or setting
observation: Broad rewrites during camera edits can alter unrelated prompt semantics.
result: A narrow camera edit preserves subjects, setting, actions, dialogue, and sound.
inference: Edit scope should be locked before recompilation.
reusable_lesson: Patch the smallest responsible layer and recompile the applicable H3 payload.
validation:
  method: offline-golden-regression
  evidence: tests/golden/camera-only-repair.expected.txt
  attempts: 1
  successes: 1
approval:
  approved_by_user: true
  approved_at: project-migration
model_context:
  model_version: MiniMax-H3
  skill_version: clean-successor
  created_at: project-migration
  last_validated: project-migration
reference_budget:
  weight: HIGH
traceability:
  source_project: legacy-migration
```

These examples are governance fixtures. They do not authorize new story facts, cinematic defaults, or automatic promotion of future successful prompts.
