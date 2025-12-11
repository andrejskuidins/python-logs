def capitalizeFirst(arr):
    if len(arr) == 0:
        return []
    return list(arr[0].capitalize()) + capitalizeFirst(arr[1:])


print(capitalizeFirst(["car", "taco", "banana"]))  # ['Car','Taco','Banana']

# def flatten(arr):
#     print(arr)
#     if type(arr) == type(int):
#         return arr
#     return flatten(arr[1:])


# print(flatten([1, 2, 3, [4, 5]]))  # [1, 2, 3, 4, 5]
# print(flatten([1, [2, [3, 4], [[5]]]]))  # [1, 2, 3, 4, 5]
# print(flatten([[1], [2], [3]]))  # [1, 2, 3]
# print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))  # [1, 2, 3]

# def isOdd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True


# def someRecursive(arr, cb):
#     if len(arr) == 0:
#         return True
#     if len(arr) == 1:
#         return cb(arr[0])
#     if cb(arr[0]):
#         return True
#     return someRecursive(arr[1:], cb)


# print(someRecursive([1, 2, 3, 4], isOdd))  # true
# print(someRecursive([4, 6, 8, 9], isOdd))  # true
# print(someRecursive([4, 6, 8], isOdd))  # false


# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if len(strng) == 1:
#         return True
#     if strng[0] == strng[-1]:
#         return isPalindrome(strng[1:-1])
#     return False


# print(isPalindrome("awesome"))  # false
# print(isPalindrome("foobar"))  # false
# print(isPalindrome("tacocat"))  # true
# print(isPalindrome("amanaplanacanalpanama"))  # true
# print(isPalindrome("amanaplanacanalpandemonium"))  # false

# def reverse(strng):
#     if len(strng) == 0:
#         return ""
#     return strng[-1] + reverse(strng[:-1])


# print(reverse("python"))  # 'nohtyp'
# print(reverse("appmillers"))  # 'srellimppa'

# def fib(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return num
#     return fib(num - 1) + fib(num - 2)


# # 0 1 1 2 3 5 8 13 21 34 55
# print(fib(4))  # 3
# print(fib(10))  # 55
# print(fib(28))  # 317811
# print(fib(35))  # 9227465

# 0, 1, 1, 2, 3, 5, 8, ..

# def recursiveRange(num):
#     if num == 0:
#         return 1
#     if num == 1:
#         return num
#     return num + recursiveRange(num - 1)


# print(recursiveRange(6))  # 21
# print(recursiveRange(10))  # 55

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])


# print(productOfArray([1, 2, 3]))  # 6
# print(productOfArray([1, 2, 3, 10]))  # 60


# def factorial(num):
#     if num == 0:
#         return 1
#     if num == 1:
#         return num
#     return num * factorial(num - 1)


# print(factorial(1))  # 1
# print(factorial(2))  # 2
# print(factorial(4))  # 24
# print(factorial(7))  # 5040


# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     if exponent == 1:
#         return base
#     return base * power(base, exponent - 1)


# print(power(2, 0))  # 1
# print(power(2, 2))  # 4
# print(power(2, 4))  # 16
# print(power(2, 5))  # 16
