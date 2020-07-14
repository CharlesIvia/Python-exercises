# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name


def old_mac(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest

print(old_mac("charles"))


#Alternatively

def old_mc(name):
    first_part = name[:3]
    second_part = name[3:]

    return first_part.capitalize() + second_part.capitalize()

print(old_mc("gatsby"))