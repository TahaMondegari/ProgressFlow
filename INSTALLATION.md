# ProgressFlow — Installation & Usage

A practical guide to installing, configuring, and using **ProgressFlow** with Claude Code.

## Overview

ProgressFlow is a lightweight skill that guides Claude through clear, honest status reporting during substantial, multi-step tasks.

It encourages Claude to:

- Establish a milestone-based plan before substantial work begins.
- Share a concise progress update at least every five minutes while actively working, when the environment allows.
- Report a completion percentage based on verifiable work.
- Display a consistent progress bar.
- Provide a realistic estimated time of arrival (ETA), or explicitly state when an estimate is not reliable.
- Explain completed work, the next step, and any blocker.
- Finish with a truthful handoff that distinguishes completed work from anything not verified.

The skill also promotes professional implementation habits: natural writing, purposeful filenames, minimal necessary comments, and a final quality review.

> **Important:** A Claude Code skill provides instructions and supporting resources. It is not a background scheduler. It cannot independently interrupt a blocked tool call or guarantee a message at an exact five-minute interval. Claude reports as soon as execution control returns, subject to the capabilities of the host environment.

---

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
- A project or user-level Claude Code skills directory
- No additional Python packages or external runtime dependencies

The optional progress-bar utility requires Python 3.9 or later and uses only the Python standard library.

## Installation

Choose one installation method.

### Option A — Install for a single project

Use this method when the skill should be available only inside one repository.

1. Download this repository or the ZIP archive.
2. Extract the `progress-flow` directory.
3. Copy the directory into your target project's `.claude/skills/` folder.
4. Confirm that `SKILL.md` is located at the following path:

```text
your-project/
└── .claude/
    └── skills/
        └── progress-flow/
            ├── SKILL.md
            ├── README.md
            ├── LICENSE
            ├── references/
            ├── examples/
            └── scripts/
```

If `.claude/skills/` does not exist, create it.

### Option B — Install for your user account

Use this method to make the skill available across your Claude Code projects.

Copy the complete `progress-flow` directory to:

```text
~/.claude/skills/progress-flow/
```

On Windows, the home directory is typically:

```text
%USERPROFILE%\.claude\skills\progress-flow\
```

Create the `skills` directory if it does not already exist.

### Option C — Install from a GitHub clone

Clone the repository:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

Then copy the `progress-flow` folder into either:

```text
your-project/.claude/skills/
```

or your user-level skills directory:

```text
~/.claude/skills/
```

Replace `USERNAME/REPOSITORY` with the actual GitHub owner and repository name.

---

## Using the skill

Start or reopen Claude Code in the relevant project.

When beginning a substantial task, ask Claude to use the skill:

```text
Use the progress-flow skill for this task. Keep me informed with
truthful progress updates, a progress bar, and a realistic ETA.
```

You can also make the expected behavior explicit in your request:

```text
Build the requested feature. First define the milestones, then provide
progress updates at least every five minutes while actively working.
Use verified completion percentages and never invent an ETA.
```

For short tasks, Claude should avoid unnecessary status messages. The skill is intended for substantial work such as:

- Building a website or application
- Implementing a multi-step feature
- Debugging a complex issue
- Refactoring a codebase
- Running a longer testing and verification process
- Preparing and packaging project deliverables

## Progress update format

A typical update looks like this:

```text
Progress: 50% · ETA: about 10–15 minutes

[█████░░░░░]

Completed: Main page structure and API integration.
Next: Finish form validation and test the primary user flow.
```

The percentage represents completed scope, not elapsed time. The ETA is an estimate, not a guarantee.

## How progress is measured

Claude is instructed to divide the task into meaningful milestones and assign weights based on the actual scope.

For example:

| Milestone | Weight |
|---|---:|
| Inspect requirements and project structure | 10% |
| Implement the main interface | 30% |
| Implement application behavior | 25% |
| Test and resolve issues | 20% |
| Package and hand off the result | 15% |
| **Total** | **100%** |

These weights are illustrative. Claude should adapt them to the task instead of applying the same distribution to every project.

A milestone should count as complete only after its acceptance criteria have been met. If the requirements change, Claude should revise the plan and recalculate progress against the new scope.

## Optional progress-bar utility

The package includes a small Python script for rendering a consistent 10-cell progress bar.

Run it from the skill directory:

```bash
python scripts/progress_bar.py 65
```

Example output:

```text
Progress: 65% [███████░░░]
```

You can customize the label:

```bash
python scripts/progress_bar.py 80 --label "Build"
```

The script only formats a percentage. It does not track project state, create timers, or send messages.

## Customization

The skill is intentionally modular:

| File | Purpose |
|---|---|
| `SKILL.md` | Main behavior and rules |
| `references/progress-method.md` | Milestone planning and progress calculation |
| `references/eta-estimation.md` | ETA estimation and uncertainty |
| `references/platform-limitations.md` | Execution and notification limitations |
| `references/quality-rules.md` | Accuracy, privacy, and reporting standards |
| `examples/update-examples.md` | Example user-facing updates |
| `scripts/progress_bar.py` | Optional progress-bar formatter |

To change the update cadence, edit the five-minute rule in `SKILL.md` and keep related references consistent.

## Troubleshooting

### Claude does not use the skill

- Confirm that the folder is named `progress-flow`.
- Confirm that `SKILL.md` is directly inside that folder.
- Check that the skill is in the correct project-level or user-level directory.
- Restart or reopen the Claude Code session if the skill is not detected.
- Explicitly ask Claude to use `progress-flow`.

### Updates are delayed during a long command

Some commands block the assistant until they finish. The skill cannot interrupt those operations. Claude should send the update as soon as control returns and, where practical, use shorter execution steps or supported polling.

### The percentage does not change

Progress should change only when verifiable work is completed. Time passing alone is not a reason to increase the percentage.

### The ETA is unavailable

An honest `ETA: not yet reliable` is preferable to a fabricated estimate. Once the remaining work and execution pace become clearer, Claude can provide a range.

---

## Design principles

**Accuracy first.** Never fabricate progress, test results, or completion claims.

**Low noise.** Updates should be short, relevant, and useful.

**Human-quality output.** Write naturally, use meaningful filenames, and avoid redundant comments.

**Modular by design.** Keep the main skill concise and place detailed guidance in focused reference files.

**Transparent limitations.** Never promise background notifications or exact timing unless the environment genuinely supports them.

## License

This project is released under the [MIT License](LICENSE).
