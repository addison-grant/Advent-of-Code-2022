
"""
Rules:

A is Rock.     Choosing gives 1 point.
B is Paper.    Choosing gives 2 points.
C is Scissors. Choosing gives 3 points.

Rock beats Scissors
Paper beats Rock
Scissors beats Paper

Strategy guide:

X means lose.
Y means draw.
Z means win

Winning a match gives 6 points.
"""

points = 0
with open("input_2a.txt", "r") as f:
    for line in f:
        p1, p2 = map(lambda x: x.strip(), line.split(" "))
        choice_points = 0
        win_points = 0

        if p2 == "X":  # lose
            if p1 == "A":
                p2 = "C"
            elif p1 == "B":
                p2 = "A"
            else: # p1 == "C"
                p2 = "B"
        elif p2 == "Y": # draw
            win_points = 3
            p2 = p1
        elif p2 == "Z": # win
            win_points = 6
            if p1 == "A":
                p2 = "B"
            elif p1 == "B":
                p2 = "C"
            else: # p1 == "C"
                p2 = "A"
        
        if p2 == "A":
            choice_points = 1
        elif p2 == "B":
            choice_points = 2
        else: # p2 == C
            choice_points = 3

        points += choice_points + win_points

print(points)
