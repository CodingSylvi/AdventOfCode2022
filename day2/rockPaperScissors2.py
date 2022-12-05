def calculateMove(opponent, outcome):
    ret = 0
    if outcome == 3: # draw
        ret = opponent
    elif outcome == 0: # lose
        if opponent == 1: # if rock -> scissors
            ret = 3
        elif opponent == 2: # if paper -> rock
            ret = 1
        elif opponent == 3: # if scissors -> paper
            ret = 2
    elif outcome == 6: # win
        if opponent == 1: # if rock -> paper
            ret = 2
        elif opponent == 2: # if paper -> scissors
            ret = 3
        elif opponent == 3: # if scissors -> rock
            ret = 1
    return ret


filename = "input.txt"
with open(filename) as f:
    rounds = f.readlines()
f.close()

scores = []

for r in rounds:

    opponent = 0
    me = 0
    outcome = 0
    score = 0

    round = r.split()

    if round[0] == "A": # rock
        opponent = 1
    elif round[0] == "B": # paper
        opponent = 2
    elif round[0] == "C": # scissors
        opponent = 3
    
    if round[1] == "X": # lose
        outcome = 0
    elif round[1] == "Y": # draw
        outcome = 3
    elif round[1] == "Z": # win
        outcome = 6

    me = calculateMove(opponent, outcome)
    scores.append(me + outcome)

totalScore = 0
for s in scores:
    totalScore += s

print("total score = " + str(totalScore))
