
"""
Rules:

A & X are Rock.     Choosing gives 1 point.
B & Y are Paper.    Choosing gives 2 points.
C & Z are Scissors. Choosing gives 3 points.

Rock beats Scissors
Paper beats Rock
Scissors beats Paper

Winning a match gives 6 points.
"""

points = 0
with open("input_2a.txt", "r") as f:
    for line in f:
        p1, p2 = map(lambda x: x.strip(), line.split(" "))
        # print("'" + p1 + "'" + " vs. " + "'" + p2 + "'")
        choice_points = 0
        win_points = 0
        
        if p2 == "X":
            choice_points = 1
            if p1 == "C":
                win_points = 6
            elif p1 == "A":
                win_points = 3
            # print(True)
        elif p2 == "Y":
            choice_points = 2
            if p1 == "A":
                win_points = 6
            elif p1 == "B":
                win_points = 3
            # print(True)
        elif p2 == "Z":
            choice_points = 3
            if p1 == "B":
                win_points = 6
            elif p1 == "C":
                win_points = 3
            # print(True)
        
        points += choice_points + win_points
        # print(points)

print(points)
