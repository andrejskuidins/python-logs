def best_scores(lst):
    max1, max2 = 0, 0
    for i in lst:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max2 = i
    return max1, max2


myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(best_scores(myList))  # 90 87

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


# def max_product(arr):
#     arr.sort()
#     return arr[-2] * arr[-1]


# def max_product(arr):
#     max1, max2 = 0, 0
#     for i in arr:
#         print(max1, max2)
#         if i > max1:
#             max2 = max1
#             max1 = i
#         elif i > max2 and i != max1:
#             max2 = i
#     return max1, max2


# print(max_product([1, 7, 3, 4, 9, 5]))
# print(max_product([1, 7, 3, 4, 9, 5, 1, 10]))
