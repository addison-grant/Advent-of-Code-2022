
backpacks = []

with open("puzzle1input.txt", "r") as f:
    backpack_buff = []
    for line in f:
        if line != "\n":
            backpack_buff.append(int(line))
        else:
            backpacks.append(backpack_buff)
            backpack_buff = []

calories = []
for bp  in backpacks:
    calories.append(sum(bp))

calories = sorted(calories)

print(sum(calories[-3:]))
