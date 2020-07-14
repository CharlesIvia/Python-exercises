# LESSER OF TWO EVENS:

# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)

print(lesser_of_two_evens(8, 2))
print(lesser_of_two_evens(4, 16))
print(lesser_of_two_evens(2, 15))

#Alternative


def lesser_of_two_even(a, b):
    if (a % 2 == 0 and b % 2 == 0) and a < b:
        return a
    else:
        return b

print(lesser_of_two_even(8, 2))
print(lesser_of_two_even(4, 16))
print(lesser_of_two_even(8, 15))