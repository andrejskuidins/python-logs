# Given ranges like [(1,3), (2,6), (8,10), (15,18)], merge overlapping ones.


def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Overlapping intervals, merge them
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            # No overlap, add current interval
            merged.append(current)

    return merged


# Example usage:
ranges = [(1, 3), (2, 6), (8, 10), (15, 18)]
print(merge_intervals(ranges))
