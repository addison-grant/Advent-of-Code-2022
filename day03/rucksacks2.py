import string

# dictionary of priorities {"a": 1, "b": 2, ... }
priority_values = dict(zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1)))

priority_sum = 0
with open("rucksacks.in.txt", "r") as rucksacks:
    triple = []
    for i, r in enumerate(rucksacks):
        triple.append(r.strip())
        if len(triple) == 3:
            r1, r2, r3 = triple
            badge = (set(r1) & set(r2) & set(r3)).pop()
            priority_sum += priority_values[badge]
            print(badge + ", " + str(priority_sum))
            triple = []

print(priority_sum)
