time = 0
ids = []

#For Part2
idPos = []
pos = 0

with open('input4.txt') as file:
    lines = file.readlines()
    time = int(lines[0])
    for i in lines[1].split(','):
        if i.strip().isnumeric():
            ids.append(int(i.strip()))
            idPos.append(pos)

        pos += 1

################################
#part 1
busId = -1
busTime = time
while busId < 0:
    for i in ids:
        if busTime % i == 0:
            busId = i
    busTime += 1 

print(( (busTime - 1) - time ) * busId)

#################################
#part 2
print(ids)
print(idPos)

firstId = 0
seqFound = False
currPos = 0
prevId = 1 

while not seqFound:
    currPos = firstId
    seqFound = True
    for pos in range(1, len(idPos)):
        currPos = firstId + idPos[pos]
        if currPos % ids[pos] != 0:
            seqFound = False
            break

    firstId += ids[0]

    if firstId >= prevId * 1000:
        print(firstId)
        prevId = firstId

print(firstId - ids[0])







