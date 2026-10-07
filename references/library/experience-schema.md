# Experience Library Schema

The Experience Library records reusable production knowledge separately from Prompt Library artifacts.

## Record

```yaml
experience_id:
status: CANDIDATE | VALIDATED | APPROVED | REVOKED | SUPERSEDED | STALE
type: SUCCESS | FAILURE | LIMITATION | REPAIR
category:
subcategory:
title:

scope:
tags:

applicability:
  conditions:
  exclusions:

observation:
result:
inference:
reusable_lesson:

validation:
  method:
  evidence:
  attempts:
  successes:

approval:
  approved_by_user: false
  approved_at:

model_context:
  model_version:
  skill_version:
  created_at:
  last_validated:

relations:
  supersedes:
  conflicts_with:
  derived_from:
  requires:

reference_budget:
  weight: LOW | MEDIUM | HIGH

traceability:
  source_prompt:
  source_project:
```

## Hard rules

Only APPROVED records with `approval.approved_by_user: true` may influence future generation.

Success, validation, or model preference is not approval.

Experience changes HOW, not WHAT:
- structure;
- wording;
- continuity;
- camera grammar;
- failure avoidance;
- applicability.

Experience cannot invent user-requested story facts.

Historical prompts are evidence, not text snippets to copy. Extract the reusable lesson and recompile it under the current task.

Scope is binding. A camera lesson cannot silently modify character identity or dialogue.

STALE, SUPERSEDED, and REVOKED records remain historical records but are not current defaults.


## Visual evidence provenance

Experience derived from images or videos should preserve:

- learning target;
- source asset(s);
- source time/frame/region when relevant;
- explicit exclusions;
- observation vs inference vs hypothesis;
- validation experiment;
- observer model and H3 model context.

A visual observation without validation is not an active Experience.

