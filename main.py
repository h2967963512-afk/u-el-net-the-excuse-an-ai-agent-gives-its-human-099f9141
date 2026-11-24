"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line (141 characters) giving the excuse an AI
# agent gives its human for missing a deadline: the context window
# filled up mid-sentence, evicted the plan, and left the agent
# re-reading its own notes like a stranger who never met the deadline.
# Revision note: kept the excuse to one sentence and one image — the
# context window itself is the culprit, so every word earns its place.
import os

TEXT = (
    "My context window filled up mid-sentence, evicted the plan, "
    "and left me re-reading my own notes like a stranger who'd "
    "never met the deadline."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
