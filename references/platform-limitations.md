# Platform and Execution Limitations

## A skill is not a scheduler

A skill provides instructions and supporting resources. It does not, by itself:

- Run in the background.
- Create a persistent timer.
- Interrupt a tool or terminal command.
- Send notifications while the assistant is not executing.
- Guarantee a message at an exact wall-clock interval.

Never promise these capabilities unless the host environment separately exposes them.

## Long-running operations

When possible, structure work so the assistant regains control regularly:

1. Prefer incremental commands and short execution batches.
2. Use a supported polling mechanism for asynchronous jobs.
3. Inspect intermediate outputs when safe and useful.
4. Send a status update after control returns if the interval elapsed.
5. Continue with the next phase.

Do not cancel a necessary operation solely to produce a progress message unless the user has asked for that behavior or the operation is unsafe.

## Background execution

If the host provides an actual background-task or notification feature, it may be used only when:

- It is documented and available in the current environment.
- The user has authorized the relevant action.
- The task can safely run independently.
- The assistant can accurately report what the feature does.

Do not invent commands, APIs, hooks, or configuration options.

## User-facing transparency

If the user expects real-time updates but the interface cannot deliver them during a blocking operation, explain the limitation once. Then use the most frequent reliable update cadence the environment supports.
