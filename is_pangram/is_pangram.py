#Write a Python function to check whether a string is pangram or not.

import string


def ispangram(text):
    words = text.replace(" ", "")
    words = set(words.lower())
    lst = list(string.ascii_lowercase)
    alphabet = set(lst)

    return words == alphabet

print(ispangram("The quick brown fox jumps over the lazy dog"))