# Reverse Words in a Sentence
# Input: "site reliability engineer" → Output: "engineer reliability site


def reverse2(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])

print(reverse2("site reliability engineer"))