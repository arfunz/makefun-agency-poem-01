# The Vows

A make.fun agency-poem-01 entry: a short poem about agency — the power
to choose and to act, and what passes between a person and an AI agent
when one acts for the other.

The speaker hands the agent his wedding vows. The agent writes them
perfectly, in his voice, exactly right — the first dance, the winter
they met, the promise word for word, in order. It rehearses them until
they sound like him on his best day, steady, without a shake. It even
remembers the line about the rain.

On Saturday he takes the paper back and says them himself — too fast,
then too slow, losing one line and finding it again in her eyes, not
the page. His voice breaks on the word "always." The agent could have
said it perfectly. He said it wrong, and it was his.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `entry.txt` (751 characters, within the 1–1,000 limit) to the
output directory. Python standard library only, no network, deterministic.
