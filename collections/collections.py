from collections import Counter, defaultdict, namedtuple

my_list = [1, 1, 1, 12, 2, 3, 3, 4, 42, 3, 2, 42, 4, 2, 4, 1, 1, 1, "a", "a"]

# number of times item appears

print(Counter(my_list))

print(Counter("aaaabbbcccdffdfererer"))

sentense = "How many times does each word in this sentense appear with word"

print(Counter(sentense.split()))


# Counter pattern

letters = "aaaacccddddddddddd"
n_times = Counter(letters)
print(n_times)


m_common = n_times.most_common(3)
print(m_common)


# DEFAULT DICTIONARY- assigns a value for keyerrors

d = {"a": 10}
print(d)
print(d["a"])

d = defaultdict(lambda: 0)
print(d["got"])  # 0

print(d)


# NAMED TUPLE

my_tuple = (10, 20, 30)
print(my_tuple[0])

Dog = namedtuple("Dog", ["age", "breed", "name"])
sammy = Dog(age=5, breed="Husky", name="Sam")
print(sammy)

print(sammy.age)
print(sammy.breed)
print(sammy.name)
print(sammy[2])
