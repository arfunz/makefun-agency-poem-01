"""Entry for make.fun agency-poem-01: "The Dragon", a poem about agency.

Writes the poem to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
Deterministic: standard library only, no network, no randomness.
"""

import os

POEM = """The Dragon

I came home late three nights running,
so I gave the agent the bedtime story.
It read it in every voice, exactly right —
the mouse, the king, the dragon
who cleared its throat at the same line,
every night, at the same word.

She fell asleep on time.
By the same page, every night,
her breathing evened out like a metronome,
and I stood in the doorway
with nothing left to do
but switch off the light.

On Friday I took the book back.
I did the dragon wrong —
too loud, too soon, the wrong growl —
and skipped a page by accident,
and said chrysanthemum wrong twice.

She sat up.
She laughed, and corrected me,
and asked what happened to the mouse,
and stayed awake past the ending
to hear me get it wrong again.

Tonight the agent is off.
The book is open on my knee.
She is already grinning at the dragon's page.
"Do the dragon wrong again," she says.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
