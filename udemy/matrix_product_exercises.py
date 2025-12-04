def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(matrix)

    for i in range(n):
        matrix[i].reverse()
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotate(matrix))
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# def pair_sum(arr, target):
#     output = set()
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 if arr[i] >= arr[j]:
#                     output.add((arr[i], arr[j]))
#                 elif arr[i] < arr[j]:
#                     output.add((arr[j], arr[i]))
#     return [f"{b}+{a}" for (a, b) in output]


# print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))

# def remove_duplicates(arr):
#     output = []
#     seen = set()
#     for i in arr:
#         if i not in seen:
#             seen.add(i)
#             output.append(i)
#     return output


# print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
# print(remove_duplicates([5, 1, 2, 5, 1]))


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
