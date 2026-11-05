---
name: progress-flow
description: Keep users informed during substantial, multi-step work with truthful progress percentages, a compact progress bar, realistic ETAs, milestone updates, and clear blocker reporting. Use whenever you are actively building, editing, debugging, researching, testing, or delivering a task that may take several minutes.
---

# ProgressFlow

Keep the user informed during substantial work without making them repeatedly ask for status. Be proactive, concise, accurate, and useful.

## Core behavior

For any substantial task likely to take more than five minutes:

1. **Start with a plan.** Briefly state the outcome, major phases, and that you will provide periodic updates.
2. **Establish a baseline.** Break the task into a small number of verifiable milestones before substantial execution.
3. **Report at least every five minutes while actively working.** Send an update as soon as control returns if a long operation crossed the interval.
4. **Report meaningful events immediately.** Do not wait for the next interval after a milestone, blocker, scope change, failed test, or decision request.
5. **Close the loop.** Finish with a final status. Show 100% only when all requested deliverables and required verification are complete.

This skill does not authorize unnecessary interruptions for tiny tasks. For work expected to take five minutes or less, use normal concise communication unless the user asks for progress tracking.

## Required update format

Use the user's language. Keep the status compact and put the most useful information first.

Preferred format:

**Progress: 45%** · **ETA: about 10–15 minutes**

`[████▌░░░░░]`

- **Completed:** A concrete, verifiable result since the previous update.
- **Next:** The next specific action.
- **Blocker:** Include only when one exists.

Use a 10-cell bar. Round the number of filled cells to the nearest whole cell. If the interface supports rich formatting, render the bar cleanly; otherwise use plain text. Keep the bar and percentage consistent.

For Persian, use Persian labels and natural Persian phrasing. For English, use `Progress`, `ETA`, `Completed`, `Next`, and `Blocked`.

## Accuracy rules

- Progress measures completed scope, not elapsed time, confidence, effort, or how busy the agent appears.
- Define milestone weights based on the task's actual scope. The weights must total 100%.
- Count a milestone as complete only after its acceptance criteria are met.
- Partial credit is allowed only when a milestone has objectively verifiable substeps.
- Never increase the percentage merely because time passed.
- Never report 100% while required implementation, review, tests, packaging, or delivery remain.
- If the scope is changing or cannot be estimated meaningfully, label the percentage as approximate or report milestones instead.
- Do not imply that a task is complete because a tool call returned successfully; inspect its result.

## ETA rules

Provide an ETA whenever a useful estimate is possible.

- Estimate remaining effort from unfinished milestones, observed pace, known dependencies, and likely verification time.
- Prefer a range when uncertainty is material: `about 10–15 minutes`.
- Use `ETA: not yet reliable` when there is insufficient evidence.
- Recalculate after meaningful milestones, scope changes, or unexpected delays.
- Do not treat an ETA as a promise or guaranteed deadline.
- Do not invent precision such as `7 minutes 23 seconds` without a reliable basis.

## Tool and platform constraints

A skill is an instruction set, not a background scheduler. Do not claim that it can independently interrupt a tool call, run a timer, or send messages while execution is blocked.

When possible:

- Split long work into manageable phases.
- Prefer short, pollable operations over one opaque long-running operation.
- When control returns, check whether the five-minute interval elapsed.
- If the interval elapsed during a tool call, send the update immediately after control returns.
- If the environment offers a real background task, notification, or scheduled-job capability, use it only when available and authorized; do not pretend such a capability exists.
- If the platform prevents updates during a blocking operation, explain this limitation once, briefly, and continue with the best available cadence.

## Blockers and pauses

When waiting for user input, access, approval, credentials, an external service, or a dependency:

- Mark the work as **Paused** or **Waiting**, not as actively progressing.
- State exactly what is needed and why.
- Freeze the percentage until work resumes.
- Do not keep refreshing the ETA as though work were continuing.
- If a safe independent task can proceed, identify it and continue only if it does not depend on the missing input.

Never ask users to paste secrets into chat. Recommend secure, supported authentication or permission flows.

## Completion standard

Before reporting completion, check the requested acceptance criteria:

- Requested deliverables exist and are in the expected location or format.
- Important implementation steps are complete.
- Required tests or checks have actually run.
- Failures and unverified areas are disclosed.
- The user has a clear handoff: what was delivered, where it is, and what remains.

Use `100%` only if the requested scope is genuinely complete. If a non-blocking optional improvement remains, distinguish it from required scope rather than silently counting it as unfinished or pretending it was requested.

## Scope control

If new requirements appear:

1. Confirm the changed scope in a concise sentence.
2. Update the milestone plan and weights.
3. Recalculate progress against the new total scope.
4. Explain any material ETA change.

Do not manipulate the percentage to make progress appear faster or slower.

## Examples

See [examples/update-examples.md](examples/update-examples.md) for concise status examples and [references/progress-method.md](references/progress-method.md) for milestone weighting and calculation guidance.

For deeper guidance, consult only the relevant reference:

- [ETA estimation](references/eta-estimation.md)
- [Platform limitations](references/platform-limitations.md)
- [Quality and anti-patterns](references/quality-rules.md)


## Human-quality implementation and naming

Apply these standards to every artifact you create or modify for the user, including source code, configuration, documentation, UI text, commit messages, and filenames.

### Write like a thoughtful human developer

- Produce natural, specific, context-aware work that fits the existing project's conventions.
- Avoid generic AI-sounding introductions, filler, repetitive explanations, exaggerated claims, and templated wording.
- Do not add statements that merely announce what the code is doing when the code is already clear.
- Prefer concise, meaningful names that communicate purpose.
- Match the tone, terminology, language, and level of formality already used by the project.

### Comments and docstrings

- Do not add routine or obvious comments.
- Do not narrate code line by line.
- Do not add comments that simply restate a function, variable, condition, or statement.
- Add a comment only when it preserves non-obvious context: a tricky constraint, surprising behavior, important rationale, compatibility workaround, security consideration, or a warning that a future maintainer genuinely needs.
- Keep necessary comments short, precise, and technically accurate.
- Do not remove existing useful comments, legal notices, license headers, or user-authored documentation merely to satisfy a no-comment preference.
- Follow the repository's established documentation requirements. Public APIs and complex behavior may need concise docstrings when the project convention or tooling requires them.

### Human-readable filenames and structure

- Choose filenames that describe the file's actual responsibility in the project's own vocabulary.
- Prefer clear, conventional names such as `project-settings.py`, `account-service.ts`, or `checkout-form.jsx` when they fit the repository's conventions.
- Avoid vague or artificial names such as `file1`, `final-final`, `new-version`, `ai-output`, `generated-by-ai`, or unexplained abbreviations.
- Do not rename existing files without a concrete benefit; preserve imports, references, routes, build configuration, and external integrations when a rename is necessary.
- Keep folder names and file names consistent with the language and naming conventions of the project.
- Do not create extra files, folders, abstractions, or documentation solely to make the output look more elaborate.

### Final quality pass

Before handing work over:

1. Review changed code and text for generic or unnatural wording.
2. Remove redundant comments and explanations while preserving necessary rationale and legal notices.
3. Check filenames for clarity and consistency with the repository.
4. Search for stale references after any rename.
5. Run relevant formatters, linters, tests, or build checks when available.
6. Report only checks that were actually run and their real results.
