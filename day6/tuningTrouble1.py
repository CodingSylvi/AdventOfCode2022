def shiftWindow(buffer, characters):
    bufferList = list(buffer)
    for i in range(0,len(buffer)-1):
        bufferList[i] = bufferList[i+1]

    bufferList[len(buffer)-1] = line[characters-1]
    newBuffer = "".join(bufferList)
    return newBuffer

filename = "input.txt"
with open(filename) as f:
    line = f.readline()
f.close()

bufferSize = 4
buffer = line[:bufferSize]

characters = bufferSize
for i in range(len(line)-bufferSize):
    bufferList = list(buffer)
    marker = True
    for bl1 in bufferList:
        smallList = bufferList.copy()
        smallList.remove(bl1)
        for bl2 in smallList:
            if bl1==bl2:
                marker = False
    if marker:
        print("the first start-of-packet marker is " + buffer + " at " + str(characters))
        break
    characters += 1
        
    buffer = shiftWindow(buffer, characters)
