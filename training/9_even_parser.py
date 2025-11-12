# Input example:
# "INFO Starting service"
# "ERROR Disk full"
# Count how many times each level appears.


from collections import Counter


def counter(input_lines):
    levels = [line.split()[0] for line in input_lines]
    report = Counter(levels)
    sorted_alpha = sorted(report.items())
    sorted_count = sorted(report.items(), key=lambda x: x[1], reverse=True)
    return sorted_alpha, sorted_count


var = [
    "INFO Starting service",
    "ERROR Disk full",
    "INFO Status service",
    "INFO Stopping service",
    "ERROR Memory low",
]

print(counter(var))
