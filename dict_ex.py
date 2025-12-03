def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}


my_dict = {"a": 1, "b": 2, "c": 3}
print(reverse_dict(my_dict))


# def max_value_key(my_dict):
#     return max(my_dict, key=my_dict.get)

# my_dict = {"a": 5, "b": 9, "c": 2}
# print(max_value_key(my_dict))


# def merge_dicts(d1, d2):
#     d = d2.copy()
#     for i in d1:
#         d[i] = d2.get(i, 0) + d1[i]
#     return d

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 3, "c": 4, "d": 5}
# print(merge_dicts(dict1, dict2))


# def count_word_frequency(words):
#     d = {}
#     for i in words:
#         d[i] = d.get(i, 0) + 1
#     return d

# words = ["banana", "banana", "apple", "orange", "banana", "apple", "orange", "apple"]
# print(count_word_frequency(words))
