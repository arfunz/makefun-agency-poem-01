#!/usr/bin/env python3
"""The Vows -- a poem about agency.

Writes the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set, following the kit's local-run convention). Python standard
library only, no network, deterministic: every run writes exactly the
same bytes.
"""

import os
import sys
from pathlib import Path

POEM = '''The Vows

I gave the agent my wedding vows.
It wrote them in my voice, exactly right —
the first dance, the winter we met,
the promise, word for word, in order.

It rehearsed them until they sounded like me
on my best day, steady, without a shake.
It even remembered the line about the rain.

I asked her once in the kitchen,
the words all wrong, and she said yes anyway.
That was the whole of it. That was the vow.

It chose the song, it wrote the toast,
it told my brother where to stand.
It knew the order of everything
except the shaking in my hands.

On Saturday I took the paper back.
I stood at the altar and said them myself —
too fast, then too slow. I lost one line
and found it again in her eyes, not the page.

My voice broke on the word "always."
She laughed, once, quietly, and nodded.
The agent could have said it perfectly.

I said it wrong, and it was mine.
'''

EXPECTED_CHARS = 875


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    # Post-write check: the written file must hold exactly the approved
    # poem, within the competition's 1-1,000 character limit.
    written = target.read_text(encoding="utf-8")
    if written != POEM:
        print("error: written entry.txt differs from the poem", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 1000 or len(written) != EXPECTED_CHARS:
        print(
            f"error: entry is {len(written)} characters, "
            f"expected {EXPECTED_CHARS} (limit 1-1000)",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {target} ({len(POEM)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
