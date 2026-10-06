# Mode Routing

## T2VA
Text-only generation. Use the supported text schema.

## I2VA
A starting image constrains the initial visual state. Describe motion from that state.

## FL2VA
First and last images constrain both endpoints. The description must form a plausible transition between them.

## L2VA
The last image constrains the endpoint. Describe a plausible preceding state and transition into the final image.

## Ref2VA
Reference assets provide explicitly assigned identity, environment, motion, voice, or other roles. Use the complete reference-based schema when applicable.

## Routing rule

Do not infer a mode from the mere presence of a file. Infer it from the user's requested workflow and asset roles.


## Routing precedence and structural lock

Mode selection is determined by the requested workflow and explicit asset roles, not by filename, slot number, or the mere presence of an attachment.

Once a mode is selected:
- use that mode's official outer schema;
- preserve the official field order and required alignment header;
- do not import another mode's outer fields;
- do not convert a base-mode request into Ref2VA merely because a reference is available;
- do not convert an I2VA/FL2VA/L2VA endpoint request into generic Ref2VA;
- do not add keyframe alignment language to T2VA;
- do not invent endpoint timing when the effective timing is unknown.

Reference content may still be semantically relevant inside the selected mode when the user's workflow authorizes it, but schema identity remains locked to the selected H3 mode.
