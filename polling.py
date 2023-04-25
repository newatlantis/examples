#!/usr/bin/env python3

# Example of a Python while loop that iterates X times or times out, whichever comes first

import sys
import time
USAGE = 'polling.py ITERATIONS TIMEOUT_SECS'
SLEEP_SECS = 5


def secs_since(start_secs):
    return (time.time() - start_secs)


if len(sys.argv) != 3:
    print(f"usage: {USAGE}", file=sys.stderr)
    exit(1)

iterations = int(sys.argv[1])
timeout_secs = float(sys.argv[2])

count = 0
start = time.time()
while count < iterations and secs_since(start) < timeout_secs:
    count += 1
    print(f"Iteration {count} - sleeping for {SLEEP_SECS} seconds...")
    time.sleep(SLEEP_SECS)

if count == iterations:
    print(f">> Exited after {iterations} iterations.")
else:
    print(f">> Timed out.")
