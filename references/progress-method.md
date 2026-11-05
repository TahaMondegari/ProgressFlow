# Progress Measurement

## 1. Define the scope

Translate the request into 3–7 meaningful milestones. Avoid both extremes:

- Too few milestones hide important unfinished work.
- Too many milestones create administrative overhead and noisy updates.

Each milestone needs an observable completion condition.

Example for a small web application:

| Milestone | Weight | Acceptance condition |
|---|---:|---|
| Understand requirements and inspect project | 10% | Relevant files and constraints reviewed |
| Implement core structure and UI | 30% | Main requested screens/components exist |
| Implement behavior and integration | 25% | Required flows work in the available environment |
| Test and fix issues | 20% | Relevant checks run; failures addressed or disclosed |
| Package and hand off | 15% | Deliverables saved and locations verified |
| **Total** | **100%** | |

Adapt weights to the actual task. Do not reuse this table blindly.

## 2. Calculate progress

For completed milestones:

`progress = sum(weight of completed milestones)`

For a milestone with verifiable substeps, partial credit may be calculated from those substeps. Do not award arbitrary partial credit based on time spent.

Round to a whole percentage for display. Keep the internal calculation more precise if useful.

## 3. Calculate the bar

Use 10 cells. The filled-cell count is:

`round(progress_percent / 10)`

Examples:

- 0% → `[░░░░░░░░░░]`
- 20% → `[██░░░░░░░░]`
- 50% → `[█████░░░░░]`
- 80% → `[████████░░]`
- 100% → `[██████████]`

The optional `scripts/progress_bar.py` helper produces the same format.

## 4. Update cadence

Track the time of the last user-visible update using the host's available clock/context. While actively working, do not allow more than five minutes to pass without a status update when the interface permits.

Also send updates on events:

- A milestone is completed.
- A new blocker is found.
- A test or external dependency fails.
- The scope or ETA materially changes.
- User input is needed.

Do not send repetitive messages when no work is happening or when the user is already waiting on a clearly stated dependency.

## 5. Avoid false precision

If a task is open-ended, exploratory, or dependent on uncertain external systems, prefer:

`Progress: approximately 40% · ETA: not yet reliable`

Then state the completed milestones and the next decision or experiment.

A progress percentage is a communication aid, not a claim that every task has a perfectly measurable amount of work.
