def check_same_frequency(l1, l2):
    def compare(lst):
        d = {}
        for i in lst:
            d[i] = d.get(i, 0) + 1
        return d

    return compare(l1) == compare(l2)


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))


# def filter_dict(d, cond):
#     return {k: v for k, v in d.items() if cond(k, v)}


# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
# print(filtered_dict)


# def reverse_dict(my_dict):
#     return {v: k for k, v in my_dict.items()}


# my_dict = {"a": 1, "b": 2, "c": 3}
# print(reverse_dict(my_dict))


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
