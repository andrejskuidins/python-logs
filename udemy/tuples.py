def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)


# def get_diagonal(t):
#     return tuple(t[i][i] for i in range(len(t)))


# input_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# output_tuple = get_diagonal(input_tuple)
# print(output_tuple)  # Expected output: (1, 5, 9)


# def concatenate_strings(input_tuple):
#     return " ".join(input_tuple)


# input_tuple = ("Hello", "World", "from", "Python")
# output_string = concatenate_strings(input_tuple)
# print(output_string + ".")  # Expected output: 'Hello World from Python'


# def tuple_elementwise_sum(t1, t2):
#     if len(t1) != len(t2):
#         raise ValueError("Input tuples must have the same length.")

#     result = tuple(a + b for a, b in zip(t1, t2))
#     return result


# def tuple_elementwise_sum(tuple1, tuple2):
#     return tuple(map(sum, zip(tuple1, tuple2)))


# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)
