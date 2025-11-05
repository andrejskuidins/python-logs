# Check if a string like "([]{})" is properly balanced.

# class Stack:
#     def __init__(self) -> None:
#         self.stack = []

#     def push(self, element):
#         self.stack.append(element)

#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack.pop()

#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack[-1]

#     def isEmpty(self):
#         return len(self.stack) == 0

#     def size(self):
#         return len(self.stack)

from collections import deque

def func1(sentence: str) -> bool:
    myStack = deque()
    for i in sentence:
        if i in "([{":
            myStack.append(i)
        elif i in ")":
            if myStack.pop() != "(":
                return False
        elif i in "]":
            if myStack.pop() != "[":
                return False
        elif i in "}":
            if myStack.pop() != "{":
                return False
    return len(myStack) == 0  # isEmpty equivalent

print("([]{})")
print(func1("([]{})"))

print("{}()[]")
print(func1("{}()[]"))

print("[(({[({[]})]}))]")
print(func1("[(({[({[]})]}))]"))


