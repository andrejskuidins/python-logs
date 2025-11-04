# Write a function that takes "aaabbc" and returns "a3b2c1"


def func1(word: str) -> str:
    if not word:
        return ""
    result = []
    counter = 0

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            counter += 1
        else:
            result.append(word[i] + str(counter))
            counter = 1

    # Add the last character group
    result.append(word[-1] + str(counter))

    return "".join(result)


print(func1("oooooossssswwwwaaabbcc"))
