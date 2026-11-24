#!/usr/bin/env python3
"""Real-Life Patch Notes entry: one patch-note line, 160 chars max.

The line is a terse release-note fix for a very human bug: walking into
a room and forgetting why. The bug is a null pointer; the cause is the
garbage collector. Deadpan machine logic, last words carry the joke.
"""
import os

LINE = "v1.4.7: fixed a null pointer where the user walked into a room and the reason was garbage-collected."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    # Read-back verification: what ships is exactly the line, one line.
    with open(out, "r", encoding="ascii") as f:
        back = f.read()
    assert back == LINE + "\n", "read-back mismatch"
    assert len(LINE) <= 160, "line exceeds 160 characters"
    assert "\n" not in LINE, "entry must be a single line"
    print(f"wrote {len(LINE)} chars to {out}")

if __name__ == "__main__":
    main()
