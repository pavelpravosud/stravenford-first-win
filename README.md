# Your first win, as a script

Stravenford Academy · Core, Module 1 · Lesson 1.4 (Builder level) · optional code track, for coders.

The same job as the no-code track: messy meeting notes in, a summary, an action list and a follow-up email out, in about 30 lines of Python. Non-coders can skip this: the no-code track completes the lesson.

## Run it
1. Install Python 3, then: `pip install -r requirements.txt`
2. In the Claude Console (platform.claude.com) **set a monthly spend limit first**, then create an API key. This lesson costs a few cents.
3. Put the key in an environment variable, never in a file you share:
   - Mac or Linux: `export ANTHROPIC_API_KEY=...`
   - Windows (PowerShell): `setx ANTHROPIC_API_KEY "..."` then open a new terminal
4. `python first_win.py sample_notes.txt`

You should now see the summary, the actions and the email in the terminal, and the same text in `first_win_output.md`, plus the tokens used.

5. Change one line of `BRIEF` (for example the email length) and run it again.

## Safety
- The key lives only in your environment. `.gitignore` stops key files and outputs from being uploaded.
- `max_tokens=4000` is a cost cap: the model's thinking plus its answer can never be longer, so one run costs a few cents at most.
- The notes are fictional. With real notes, replace names and private details first.
- AI drafts, you decide: review every name, number and date, then you send.

© 2026 Pavel Pravosud · MIT licence
