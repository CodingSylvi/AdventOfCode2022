filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()
f.close()

map = []
for line in lines:
    lineList = list(line.strip())
    map.append(lineList)

rowCount = len(map)
columnCount = len(map[0])

scenicScore = []
for row in range(rowCount):
    columnList = []
    for column in range(columnCount):
        columnList.append(0)
    scenicScore.append(columnList)

for row in range(rowCount):
    for column in range(columnCount):

        # to the left
        scoreLeft = 0
        for left in range(column-1, -1, -1):
            scoreLeft += 1
            if map[row][left] >= map[row][column]:
                break
        
        # to the right
        scoreRight = 0
        for right in range(column+1, columnCount):
            scoreRight += 1
            if map[row][right] >= map[row][column]:
                break

        # to the top
        scoreTop = 0
        for top in range(row-1, -1, -1):
            scoreTop += 1
            if map[top][column] >= map[row][column]:
                break

        # to the bottom
        scoreBottom = 0
        for bottom in range(row+1, rowCount):
            scoreBottom += 1
            if map[bottom][column] >= map[row][column]:
                break

        scenicScore[row][column] = scoreLeft * scoreRight * scoreTop * scoreBottom

highestScore = 0
for row in range(rowCount):
    for column in range(columnCount):
        if scenicScore[row][column] > highestScore:
            highestScore = scenicScore[row][column]

print("the highest scenic score is " + str(highestScore))
        