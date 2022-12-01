
backpacks = []

with open("puzzle1input.txt", "r") as f:
    backpack_buffer = []
    for line in f:
        if line != "\n":
            backpack_buffer.append(int(line))
        else:
            backpacks.append(backpack_buffer)
            backpack_buffer = []

calories = []
for backpack in backpacks:
    calories.append(sum(backpack))

calories = sorted(calories)

print(sum(calories[-3:]))
