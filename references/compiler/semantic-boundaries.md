# Semantic Boundaries

## Four-way semantic diff

Every compiled prompt can be evaluated as:

- PRESERVED — explicitly authorized and retained.
- ADDED — not authorized by the user.
- ALTERED — meaning changed.
- DROPPED — explicitly authorized content missing.

## Safe transformation

A transformation is safe when it changes wording or structure while preserving the observable result requested by the user.

## Unsafe transformation

A transformation is unsafe when it adds:

- characters
- relationships
- locations
- props
- actions
- emotions
- camera choices
- lighting
- dialogue
- music
- duration
- narrative events

without authorization.

## Reference rule

Reference material is evidence about a user-specified attribute, not permission to import every attribute visible in the source.
