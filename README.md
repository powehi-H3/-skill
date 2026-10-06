# MiniMax H3 Prompt Skill

A clean, compiler-first Skill for writing and repairing MiniMax H3 prompts.

## Design goal

Turn a user's request into a paste-ready H3 prompt without inventing scene semantics.

The project separates:

- **Compiler Core** — execution rules.
- **References** — detailed H3 syntax and production knowledge.
- **Prompt Library** — validated prompt examples.
- **Experience Library** — explicitly user-approved production lessons.
- **Regression** — tests for semantic preservation and structural correctness.

## Core principle

**Complete compilation does not mean filling every blank.**

If the user did not specify a camera, action, prop, lighting setup, dialogue content, duration, or other semantic detail, the Skill must not invent it merely to make the prompt look complete.

## Current status

V1 foundation. Offline/static regression only. Real MiniMax H3 generation is not claimed or simulated.

## Repository structure

```
SKILL.md
references/
  official/
  compiler/
  camera/
  temporal/
  audio/
  editing/
  qa/
  library/
tests/
```
