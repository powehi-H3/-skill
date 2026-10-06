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

## Authority boundary

The project has three distinct authority levels:

1. **Official MiniMax H3 syntax and mode requirements** — authoritative for H3 schema and mode-specific formatting.
2. **Explicit user intent and reference-role assignments** — authoritative for the requested semantic payload.
3. **This Skill's compiler, QA, and approved-experience layers** — execution guidance that must not override the first two.

Production lessons in this repository are not MiniMax official behavior claims. They are implementation heuristics validated only to the extent stated by their regression evidence and approval metadata.

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


## Product philosophy

This project is the cleaned successor to an earlier H3 Skill implementation.

It deliberately keeps the earlier project's strongest production mechanisms:

- semantic addition gating;
- strict edit scope and preservation;
- state/transition isolation;
- reference-role locking;
- production reasoning and continuity geometry;
- smallest-responsible-layer repair;
- payload purity;
- Prompt Library / Experience Library separation;
- user-approved experience governance;
- static and golden regression.

It deliberately does **not** copy the previous project's large historical architecture, duplicated rule layers, or unvalidated sample catalogues into the runtime compiler.

The guiding rule is:

> **Compile the user's intent faithfully first. Optimize execution only where it is authorized and useful.**

Historical migration details are documented in `references/compiler/migration-map.md`.
