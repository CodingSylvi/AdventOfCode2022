def newCycle(cycles, X):
    if cycles==20 or cycles==60 or cycles==100 or cycles==140 or cycles==180 or cycles==220:
        return cycles*X
    else:
        return 0

filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()
f.close()

X = 1
cycles = 0
sumSignalStrengths = 0

for line in lines:
    parts = line.split(" ")
    if line.strip() == "noop":
        cycles += 1
        if cycles==20 or cycles==60 or cycles==100 or cycles==140 or cycles==180 or cycles==220:
            sumSignalStrengths += cycles*X
    elif parts[0] == "addx":
        cycles += 1
        if cycles==20 or cycles==60 or cycles==100 or cycles==140 or cycles==180 or cycles==220:
            sumSignalStrengths += cycles*X

        cycles += 1
        if cycles==20 or cycles==60 or cycles==100 or cycles==140 or cycles==180 or cycles==220:
            sumSignalStrengths += cycles*X
        X = X + int(parts[1])

print("sum of the six signal strengts = " + str(sumSignalStrengths))
