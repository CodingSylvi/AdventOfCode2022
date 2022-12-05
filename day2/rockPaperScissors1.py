def calculateOutcome(opponent, me):
    # rock = 1
    # paper = 2
    # scissors = 3

    if opponent == me:
        return 3 #draw

    elif opponent==1 and me==3: # rock defeats scissors
        return 0 # you lost
    elif opponent==3 and me==2: # scissors defeats paper
        return 0 # you lost
    elif opponent==2 and me==1: # paper defeats rock
        return 0 # you lost

    elif me==1 and opponent==3: # rock defeats scissors
        return 6 # you won
    elif me==3 and opponent==2: # scissors defeats paper
        return 6 # you won
    elif me==2 and opponent==1: # paper defeats rock
        return 6 # you won


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
    
    if round[1] == "X": # rock
        me = 1
    elif round[1] == "Y": # paper
        me = 2
    elif round[1] == "Z": # scissors
        me = 3

    outcome = calculateOutcome(opponent, me)
    scores.append(me+outcome)

totalScore = 0
for s in scores:
    totalScore += s

print("total score = " + str(totalScore))

