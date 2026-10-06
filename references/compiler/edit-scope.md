# Edit Scope

For a modification request, build a scope before rewriting.

Example:

User: "只把镜头改成 POV，其他不变。"

CHANGE:
- camera

PRESERVE:
- characters
- identity
- setting
- actions
- dialogue
- sound
- timing

If a change has a necessary dependency, update only the dependent expression and record it internally. Do not use dependency as an excuse to redesign unrelated content.

Deletion must propagate through all dependent references.
