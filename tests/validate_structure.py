#!/usr/bin/env python3
"""Offline structural checks for the H3 Prompt Skill foundation.

This does not claim MiniMax H3 runtime quality.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "SKILL.md",
    "README.md",
    "references/compiler/mode-routing.md",
    "references/compiler/semantic-boundaries.md",
    "references/compiler/edit-scope.md",
    "references/temporal/state-transition.md",
    "references/temporal/frame-endpoints.md",
    "references/camera/camera-grammar.md",
    "references/audio/dialogue.md",
    "references/qa/semantic-diff.md",
    "references/qa/purity.md",
    "references/library/README.md",
    "references/library/approved-experience-examples.md",
    "tests/cases.json",
    "tests/golden/base-t2va.expected.txt",
    "tests/golden/i2va.expected.txt",
    "tests/golden/attribute-transfer.expected.txt",
    "tests/golden/camera-only-repair.expected.txt",
    "tests/golden/dialogue-audio-role.expected.txt",
    "tests/golden/phase-isolation.expected.txt",
    "tests/golden/pov-reference-role.expected.txt",
    "tests/golden/camera-grammar.expected.txt",
    "tests/golden/frame-endpoint.expected.txt",
    "tests/golden/time-budget.expected.txt",
    "tests/golden/action-continuity.expected.txt",
    "tests/golden/visible-text-preservation.expected.txt",
    "tests/golden/diagnose-no-rewrite.expected.txt",
    "tests/golden/optimize-no-semantic-addition.expected.txt",
    "tests/golden/multi-subject-role.expected.txt",
]

required_markers = [
    "GENERATE",
    "REWRITE",
    "OPTIMIZE",
    "REPAIR",
    "T2VA",
    "I2VA",
    "FL2VA",
    "L2VA",
    "Ref2VA",
    "PRESERVE",
    "CHANGE",
    "ADD",
    "DELETE",
    "subject_definitions:",
    "summary:",
    "retention_analysis:",
    "detailed_description:",
    "overall_soundscape:",
    "non_diegetic_music:",
    "integrated_multimodal_description:",
    "Missing",
    "Added",
    "Altered",
    "Contradicted",
]

missing_files = [p for p in required_files if not (ROOT / p).is_file()]
if missing_files:
    raise SystemExit("MISSING_FILES: " + ", ".join(missing_files))

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
missing_markers = [m for m in required_markers if m not in skill]
if missing_markers:
    raise SystemExit("MISSING_SKILL_MARKERS: " + ", ".join(missing_markers))

cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))
if len(cases) < 8:
    raise SystemExit("INSUFFICIENT_REGRESSION_CASES")

for case in cases:
    for key in ("id", "request"):
        if key not in case:
            raise SystemExit(f"INVALID_CASE: {case}")

print("OFFLINE STRUCTURE PASS")
print(f"cases={len(cases)}")
print("runtime_execution=False")
print("semantic_quality_proven=False")
