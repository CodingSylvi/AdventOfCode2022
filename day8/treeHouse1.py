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

visibilityMap = []
for row in range(rowCount):
    columnList = []
    for column in range(columnCount):
        columnList.append(False)
    visibilityMap.append(columnList)

for row in range(rowCount):
    for column in range(columnCount):

        if row==0 or row==rowCount-1 or column==0 or column==columnCount-1:
            visibilityMap[row][column] = True
            continue

        # to the left
        visibleLeft = True
        for left in range(column-1, -1, -1):
            if map[row][left] >= map[row][column]:
                visibleLeft = False
        
        # to the right
        visibleRight = True
        for right in range(column+1, columnCount):
            if map[row][right] >= map[row][column]:
                visibleRight = False

        # to the top
        visibleTop = True
        for top in range(row-1, -1, -1):
            if map[top][column] >= map[row][column]:
                visibleTop = False

        # to the bottom
        visibleBottom = True
        for bottom in range(row+1, rowCount):
            if map[bottom][column] >= map[row][column]:
                visibleBottom = False

        if visibleLeft or visibleRight or visibleTop or visibleBottom:
            visibilityMap[row][column] = True

visibleCount = 0
for row in range(rowCount):
    for column in range(columnCount):
        if visibilityMap[row][column] == True:
            visibleCount += 1

print(str(visibleCount) + " trees are visible")
        