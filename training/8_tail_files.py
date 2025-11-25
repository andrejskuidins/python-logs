import sys
import time

with open(sys.argv[1], "rb") as f:
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)  # Wait briefly before checking again
            continue
        print(line)
