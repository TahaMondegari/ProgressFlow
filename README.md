# ProgressFlow

A lightweight, modular Claude Code skill for transparent progress reporting during substantial work.

## What it does

- Starts substantial tasks with a clear milestone plan.
- Sends status updates at least every five minutes while execution is active and the interface permits.
- Shows a truthful completion percentage and a matching 10-cell progress bar.
- Provides a realistic ETA or explicitly says when one is not yet reliable.
- Reports completed work, the next action, blockers, pauses, and scope changes.
- Prevents fabricated progress, false completion claims, and misleading time estimates.

## Installation

For the complete installation, usage, customization, and troubleshooting guide, see [INSTALLATION.md](INSTALLATION.md).


### Claude Code — personal skill

Copy the `progress-flow` directory into:

```text
~/.claude/skills/progress-flow/
```

### Claude Code — project skill

Copy the directory into your repository:

```text
.claude/skills/progress-flow/
```

Then invoke it by asking Claude to use the `progress-flow` skill, or let Claude select it when the task description matches its metadata.

## Repository structure

```text
progress-flow/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
│   ├── eta-estimation.md
│   ├── platform-limitations.md
│   ├── progress-method.md
│   └── quality-rules.md
├── examples/
│   └── update-examples.md
└── scripts/
    └── progress_bar.py
```

The main skill file stays short and delegates specialized guidance to references. The optional script generates a consistent text progress bar; it does not run a timer or send messages.

## Important limitation

This skill cannot create an autonomous five-minute timer or interrupt a blocked model/tool call. It instructs Claude to update as soon as execution control returns and to use real background-notification features only when the host environment actually provides them.

## Design principles

- Truth over optimistic percentages.
- Useful updates over noisy updates.
- Milestones over elapsed-time guessing.
- Explicit uncertainty over fabricated ETAs.
- Low coupling: each reference covers one concern.
- Human-quality output: natural wording, purposeful filenames, and no redundant comments.
- No mandatory external dependencies.

## Validation

Run:

```bash
python scripts/progress_bar.py 65
```

Expected output:

```text
Progress: 65% [██████▌░░░]
```

The script uses only the Python standard library.
# ProgressFlow
