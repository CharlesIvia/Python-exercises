# ALMOST THERE:
#     Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(n):
    return (n >= 90 and n <= 110) or (n >= 190 and n <= 210)

print(almost_there(211))
print(almost_there(90))
print(almost_there(150))


#Alternative


def almost(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(almost(211))
print(almost(90))
print(almost(150))
