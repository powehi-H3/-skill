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
