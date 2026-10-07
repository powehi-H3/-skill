# User-Directed Visual Learning

## Purpose

The Visual Learning system extracts reusable H3 engineering evidence from user-supplied images and videos under an explicit user-defined learning scope.

It is **not** unrestricted media learning.

The governing principle is:

> The user decides WHAT to learn. The system decides HOW to observe, structure, test, and validate it.

## Mandatory gate

Every visual-learning task must establish a **Learning Scope** before extracting experience.

Minimum scope:

- TARGET — what element(s) to learn.
- SOURCE — which image/video/reference asset(s) are authoritative.
- RANGE — whole asset, phase, subject, body region, image region, or time interval when specified.
- EXCLUDE — elements that must not be learned or imported.
- PURPOSE — observe, compare, extract pattern, form H3 hypothesis, or support validation.

If the user does not specify a learning target, do not autonomously promote observations into Experience.

## Supported learning targets

Targets may include:

- appearance / identity
- pose / body state
- action
- action order / temporal sequence
- spatial relation
- environment / setting
- object / prop relation
- POV
- camera position / framing / movement
- transition
- first / last state
- audio / voice characteristics
- dialogue structure
- other explicitly named visual or audiovisual elements

These are extraction targets, not authorization to invent new story content.

## Image evidence

Images are primarily state evidence.

Extract only the requested target:

- visible state;
- spatial arrangement;
- pose/body state;
- reference-role attributes;
- composition/camera state;
- environment or object state.

Do not infer motion from a single image as fact. Mark motion-related conclusions as inference or hypothesis unless supported by multiple images or video.

For multiple images, distinguish:

- invariant elements;
- changed elements;
- uncertain elements;
- possible transition.

## Video evidence

Video is primarily transition and temporal evidence.

When action/sequence is requested, prefer:

INITIAL STATE → TRIGGER → ACTION → INTERMEDIATE STATE → FINAL STATE

When camera is requested, separately observe:

- POV;
- camera position;
- framing;
- camera motion;
- shot/transition behavior.

Do not merge camera observations into action experience unless the user selected both targets.

## Image + video evidence

When multiple media types are supplied, assign each asset a role before extraction.

Example:

- Picture 1 → identity/appearance
- Picture 2 → environment
- Video 1 → motion/temporal sequence
- Audio 1 → voice timbre/delivery

Do not transfer unrequested attributes across assets.

## Localized learning

Learning scope may be limited to:

- one subject;
- one body region;
- one image region;
- one video phase;
- one time interval;
- one shot;
- one camera behavior.

Localized scope is binding.

## Exclusion lock

An exclusion is a hard boundary for extraction.

Example:

TARGET: camera movement
EXCLUDE: action, appearance, environment, dialogue

The system must not turn observed but excluded content into an Experience candidate.

## Observation vs inference

Keep these levels separate:

- O1 — direct visual/audio observation.
- O2 — reliable structural inference from multiple evidence points.
- H1 — engineering hypothesis about reusable representation.
- V1 — H3 experiment validated.
- A1 — user-approved active Experience.

A lower level cannot be silently promoted to a higher level.

## Negative evidence

Record relevant non-events when the evidence supports them:

- no visible camera movement;
- no scene change;
- no extra subject;
- no extra object;
- no observed intermediate action.

Negative evidence is evidence, not a universal prohibition.

## Experience promotion

Visual evidence alone cannot become an active Experience.

Required progression:

CANDIDATE → VALIDATED → APPROVED

Only APPROVED + approval.approved_by_user: true may influence future H3 compilation.

## Experience boundaries

A visual experience may change:

- wording;
- structure;
- state representation;
- temporal organization;
- camera grammar;
- continuity;
- failure avoidance;
- applicability.

It may not silently change:

- user-requested WHAT;
- subject identity;
- participant count;
- adult semantic content;
- location;
- dialogue;
- props;
- duration;
- camera, if camera was outside the learning scope.

## Historical asset separation

Historical prompts, images, videos, and experiments remain source evidence.

Do not overwrite or promote historical assets merely because they were observed by the Visual Learning system.

Historical retrieval and Experience retrieval are separate operations.
