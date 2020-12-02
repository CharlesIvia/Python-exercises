import os
import re

with open("extracted_content/Instructions.txt") as f:
    content = f.read()
    print(content)

pattern = r"\d{3}-\d{3}-\d{4}"

test_string = "Phone number is 123-123-1234"

result = re.findall(pattern, test_string)
print(result)


def search(file, pattern=r"\d{3}-\d{3}-\d{4}"):
    f = open(file, "r")
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return " "


results = []

path = os.getcwd() + "\\extracted_content"
for folder, sub_folderrs, files in os.walk(path):
    for f in files:
        full_path = folder + "\\" + f
        results.append(search(full_path))
    print(results)

for r in results:
    if r != " ":
        print(r.group())
