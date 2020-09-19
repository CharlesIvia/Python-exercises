#A =P(1 + r/n)**nt


def compound_interest():
    p = float(input("How much do you want to save? "))
    t = float(input("How many years do you want to invest? "))
    r = 0.08
    n = 12
    nt = n*t
    return p*((1 + (r/n))**nt)

print(compound_interest())