import string

# dictionary of priorities {"a": 1, "b": 2, ... }
priority_values = dict(zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1)))

priority_sum = 0
with open("rucksacks.in.txt", "r") as rucksacks:
    for rucksack in rucksacks:
        rucksack = rucksack.strip()
        l = len(rucksack)
        left = set(rucksack[:l//2])
        right = set(rucksack[l//2:])
        misplaced = (left & right).pop()
        priority_sum += priority_values[misplaced]

print(priority_sum)
