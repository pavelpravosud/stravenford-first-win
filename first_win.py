"""Stravenford Academy, Lesson 1.4 code track (optional, for coders).
Turn messy meeting notes into a summary, an action list and a follow-up email.
(c) 2026 Pavel Pravosud. MIT licence."""
import os
import sys
import pathlib

import anthropic

MODEL = "claude-sonnet-5-5"
BRIEF = """Goal: turn my meeting notes into 1) a 5-line summary, 2) an action list
with one line per action, an owner and a due date, 3) a follow-up email to the attendees.
Context: the attendees were in the meeting; keep the email friendly and professional.
Format: three sections with headings; the email under 150 words.
Rule: do not invent facts. If anything is unclear, list it under "Questions to check"."""


def main():
    notes_path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "sample_notes.txt")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set ANTHROPIC_API_KEY first (see README). Never paste the key into this file.")
    notes = notes_path.read_text(encoding="utf-8")
    client = anthropic.Anthropic()  # reads the key from the environment
    reply = client.messages.create(
        model=MODEL,
        max_tokens=4000,  # cost cap: thinking plus answer can never be longer than this
        system=BRIEF,
        messages=[{"role": "user", "content": f"My notes:\n\n{notes}"}],
    )
    text = "".join(block.text for block in reply.content if block.type == "text")
    out = notes_path.with_name("first_win_output.md")
    out.write_text(text, encoding="utf-8")
    print(text)
    print(f"\nSaved to {out.name}. Tokens used: {reply.usage.input_tokens} in, {reply.usage.output_tokens} out.")


if __name__ == "__main__":
    main()
