# SUMMER OF '69:
#     Return the sum of the numbers in the array, except ignore sections of
#      numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least
#      one 9). Return 0 for no numbers


def summer_69(lst):
    to_add = []
    added = 0
    for num in lst:
        if num < 6 or num > 9:
            to_add.append(num)
    for n in to_add:
        added += n
    return added

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))