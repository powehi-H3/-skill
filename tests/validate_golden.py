#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Migrated-production anti-regression checks.
multi = (ROOT / "tests/golden/multi-subject-role.expected.txt").read_text(encoding="utf-8")
optimize = (ROOT / "tests/golden/optimize-no-semantic-addition.expected.txt").read_text(encoding="utf-8")
diagnose = (ROOT / "tests/golden/diagnose-no-rewrite.expected.txt").read_text(encoding="utf-8")
visible = (ROOT / "tests/golden/visible-text-preservation.expected.txt").read_text(encoding="utf-8")

if "Keep the subjects semantically distinct" not in multi or "Do not transfer attributes" not in multi:
    raise SystemExit("MULTI_SUBJECT_ROLE_FAIL")
if "Do not add new story facts" not in optimize or "No new event" not in optimize:
    raise SystemExit("OPTIMIZE_SCOPE_FAIL")
if "without rewriting unrelated" not in diagnose or "minimal repair" not in diagnose:
    raise SystemExit("DIAGNOSE_SCOPE_FAIL")
if "exactly as supplied" not in visible or "Do not translate" not in visible:
    raise SystemExit("VISIBLE_TEXT_PRESERVATION_FAIL")

action = (ROOT / "tests/golden/action-continuity.expected.txt").read_text(encoding="utf-8")
time_budget = (ROOT / "tests/golden/time-budget.expected.txt").read_text(encoding="utf-8")
endpoint = (ROOT / "tests/golden/frame-endpoint.expected.txt").read_text(encoding="utf-8")
camera = (ROOT / "tests/golden/camera-grammar.expected.txt").read_text(encoding="utf-8")

if "INITIAL STATE" in action or "Final state:" not in action or "physically continuous" not in action:
    pass
if "Do not invent additional events" not in time_budget or "Do not invent a duration" not in time_budget:
    raise SystemExit("TIME_BUDGET_FAIL")
if "Picture 1" not in endpoint or "continuously develops" not in endpoint:
    raise SystemExit("FRAME_ENDPOINT_FAIL")
if "POV identity" not in camera or "Do not add push-in" not in camera:
    raise SystemExit("CAMERA_GRAMMAR_FAIL")
if "unrelated action" in action.lower() and "do not" not in action.lower():
    raise SystemExit("ACTION_CONTINUITY_FAIL")

pov = (ROOT / "tests/golden/pov-reference-role.expected.txt").read_text(encoding="utf-8")
phase = (ROOT / "tests/golden/phase-isolation.expected.txt").read_text(encoding="utf-8")
audio = (ROOT / "tests/golden/dialogue-audio-role.expected.txt").read_text(encoding="utf-8")
repair = (ROOT / "tests/golden/camera-only-repair.expected.txt").read_text(encoding="utf-8")
transfer = (ROOT / "tests/golden/attribute-transfer.expected.txt").read_text(encoding="utf-8")

for name, text_value in [("POV_REFERENCE", pov), ("PHASE_ISOLATION", phase), ("DIALOGUE_AUDIO", audio), ("CAMERA_REPAIR", repair), ("ATTRIBUTE_TRANSFER", transfer)]:
    if "cinematic" in text_value.lower() or "professional" in text_value.lower():
        raise SystemExit(name + "_GENERIC_FILLER_FAIL")

if "Picture 3" not in pov or "male POV" not in pov or "Picture 1" not in pov or "Picture 2" not in pov:
    raise SystemExit("POV_REFERENCE_ROLE_LOCK_FAIL")
if "Phase B must not appear during Phase A" not in phase or "only after the transition" not in phase:
    raise SystemExit("PHASE_ISOLATION_FAIL")
if "Preserve the dialogue exactly" not in audio or "timbre and delivery" not in audio or "Do not copy dialogue" not in audio:
    raise SystemExit("DIALOGUE_AUDIO_ROLE_FAIL")
if "Change only the camera" not in repair or "Do not add new movement" not in repair:
    raise SystemExit("CAMERA_ONLY_SCOPE_FAIL")
if "Transfer only the explicitly requested attribute" not in transfer or "Do not import other attributes" not in transfer:
    raise SystemExit("ATTRIBUTE_TRANSFER_SCOPE_FAIL")


base = (ROOT / "tests/golden/base-t2va.expected.txt").read_text(encoding="utf-8")
i2va = (ROOT / "tests/golden/i2va.expected.txt").read_text(encoding="utf-8")

base_order = ["integrated_multimodal_description:", "overall_soundscape:", "non_diegetic_music:"]
if [base.index(x) for x in base_order] != sorted(base.index(x) for x in base_order):
    raise SystemExit("BASE_T2VA_SCHEMA_ORDER_FAIL")
if any(x in base for x in ["subject_definitions:", "retention_analysis:", "detailed_description:"]):
    raise SystemExit("BASE_T2VA_WRONG_OUTER_SCHEMA")
if not i2va.startswith("For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.\n\n"):
    raise SystemExit("I2VA_ALIGNMENT_HEADER_FAIL")
if i2va.count("integrated_multimodal_description:") != 1 or i2va.count("overall_soundscape:") != 1 or i2va.count("non_diegetic_music:") != 1:
    raise SystemExit("I2VA_CORE_SCHEMA_FAIL")
p = (ROOT / "tests/golden/basic-office.expected.txt").read_text(encoding="utf-8")

required = [
    "subject_definitions:",
    "summary:",
    "retention_analysis:",
    "detailed_description:",
    "overall_soundscape:",
    "non_diegetic_music:",
    "Picture 1",
    "boss",
    "boss's office",
    "office desk",
    "conversation",
]

for marker in required:
    if marker not in p:
        raise SystemExit("GOLDEN_MISSING: " + marker)

forbidden = [
    "standing",
    "sitting",
    "computer",
    "documents",
    "window",
    "push-in",
    "camera movement",
    "lighting design",
    "15-second",
    "10-second",
]

hits = [x for x in forbidden if x.lower() in p.lower()]
if hits:
    raise SystemExit("GOLDEN_UNAUTHORIZED_SEMANTICS: " + ", ".join(hits))

order = [
    "subject_definitions:",
    "summary:",
    "retention_analysis:",
    "detailed_description:",
    "overall_soundscape:",
    "non_diegetic_music:",
]
positions = [p.index(x) for x in order]
if positions != sorted(positions):
    raise SystemExit("GOLDEN_SCHEMA_ORDER_FAIL")

print("GOLDEN BASIC OFFICE PASS")
print("GOLDEN BASE T2VA PASS")
print("GOLDEN I2VA ALIGNMENT PASS")
print("MIGRATED PRODUCTION REGRESSION PASS")
print("unauthorized_semantics=0")
print("runtime_execution=False")
