# Given a list of log lines, find which message appears most often.

from collections import Counter
from list_example import log_lines

def count_often(filename: list):
    cnt = Counter(filename)
    print(cnt)

print(count_often(log_lines))  # Output: 512
