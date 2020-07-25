#Write a Python function that checks whether a word or phrase is palindrome or not


def palindrome(word):
    text = word.replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False

print(palindrome("madam"))
print(palindrome("racecar"))
print(palindrome("nurses run"))