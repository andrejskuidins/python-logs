# Given a list of log lines, find which message appears most often.

# from collections import Counter
# from list_example import log_lines


# def count_often(filename: list):
#     cnt = Counter(filename)
#     print(cnt)


# print(count_often(log_lines))  # Output: 512


from list_example import log_lines


def count_often(filename: list):
    counter = {}
    for i in filename:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 1
    sorted_dict = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


print(count_often(log_lines))
