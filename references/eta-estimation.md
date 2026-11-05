# ETA Estimation

## Estimate from remaining work

Estimate each unfinished milestone separately when practical:

`ETA = remaining implementation + verification + packaging + known wait time`

Use observed pace from the current task where available. Use prior experience only as a rough prior, not as evidence that a specific task will finish at an exact time.

## Prefer ranges

Use a range when complexity or external dependencies create uncertainty:

- `ETA: about 5–10 minutes`
- `ETA: about 30–45 minutes`

Use a single estimate only when the remaining work is small and predictable.

## Confidence language

- **Reliable:** remaining steps are known and execution pace is stable.
- **Tentative:** some implementation or testing uncertainty remains.
- **Not yet reliable:** requirements, dependencies, or failure causes are still unknown.

Do not show a confidence score unless it helps the user make a decision.

## Re-estimation triggers

Recalculate when:

- A milestone takes materially longer than expected.
- A test reveals additional work.
- A dependency is unavailable.
- The user changes the requirements.
- A large unknown is resolved.

Explain a significant ETA increase briefly and factually. Never conceal a delay by repeatedly moving the estimate without explanation.

## Paused work

When blocked, say `ETA: paused / not estimable until ...` and identify the dependency. Do not count external waiting as active progress.
