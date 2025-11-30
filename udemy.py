# def missing_number2(arr, n):
#     total = n * (n + 1) // 2
#     sum_arr = sum(arr)
#     missing = total - sum_arr
#     return missing

# print(missing_number2([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11))
# print(missing_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 11], 11))
# print(missing_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))


# def return_pairs(arr, target):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):  # Start j after i
#             if arr[i] + arr[j] == target:
#                 return i, j


# print(return_pairs([11, 7, 4, 3, 2], 6))
# print(return_pairs([3, 2, 4], 6))
# print(return_pairs([2, 7, 11, 15], 9))
# print(return_pairs([3, 3], 6))


def max_product(arr):
    arr.sort()
    return arr[-2] * arr[-1]


print(max_product([1, 7, 3, 4, 9, 5]))
