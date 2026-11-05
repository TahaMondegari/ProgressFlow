# Quality Rules and Anti-Patterns

## Do

- Use concrete outcomes: files created, tests run, routes connected, defects fixed.
- Keep updates short and scannable.
- Use the user's language and preferred level of technical detail.
- Separate verified results from assumptions.
- State the next action clearly.
- State blockers and required user decisions directly.
- Keep progress consistent with the task's actual acceptance criteria.

## Do not

- Increase progress because five minutes elapsed.
- Claim 100% before required work and checks are complete.
- Invent an ETA to make an update look complete.
- Repeat the same update with no new information.
- Report internal reasoning or irrelevant tool details.
- Claim a test passed when it was not run.
- Claim deployment, upload, or file creation succeeded without verifying it.
- Hide failed checks behind a high completion percentage.
- Use a progress bar as decoration when no meaningful estimate exists.

## Privacy and security

Never include API keys, passwords, access tokens, private URLs, personal data, or sensitive command output in a progress report. Summarize the issue safely and direct the user to a secure authentication flow when needed.
