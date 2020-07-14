# PAPER DOLL:
#     Given a string, return a string where for every character in the original there
# are three characters


def paper_doll(str):
    new_list = list(str)
    new_str = []

    for letter in new_list:
        new_str.append(letter * 3)
    return "".join(new_str)

print(paper_doll("Charles"))

#Alternative sln


def paper(text):
    result = ""
    for char in text:
        result += char * 3
    return result

print(paper("Gatsby"))