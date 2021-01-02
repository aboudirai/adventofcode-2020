inst = []

with open("input.txt") as file:
    for line in file.readlines():
        temp = []
        for i in line.strip():
            temp.append(i)
        inst.append(temp)

#-----------------------------------
#part 1

#checks if arrays are equal
def isEquals(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False
    return True


#returns 1 if no occupied seats, 2 if four or more, else 0
def checkVacancy(x, y):
    occ = 0

    edges = []
    edges.append(x < len(inst[0]) - 1)
    edges.append(x > 0)
    edges.append(y < len(inst) - 1)
    edges.append(y > 0)

    #constants
    RIGHT = 0
    LEFT = 1
    BOTTOM = 2
    TOP = 3

    #check for occupancy
    if edges[RIGHT]:
        if inst[y][x+1] == '#': #right
            occ += 1
        if edges[TOP] and inst[y-1][x+1] == '#': #top right
            occ += 1
        if edges[BOTTOM] and inst[y+1][x+1] == '#': #bottom right
            occ += 1
    if edges[LEFT]:
        if inst[y][x-1] == '#': #left
            occ += 1
        if edges[TOP] and inst[y-1][x-1] == '#': #top left 
            occ += 1
        if edges[BOTTOM] and inst[y+1][x-1] == '#': #bottom left 
            occ += 1
    if edges[TOP]:
        if inst[y-1][x] == '#': #top
            occ += 1
    if edges[BOTTOM]:
        if inst[y+1][x] == '#': #bottom
            occ += 1

    if occ == 0:
        return 1
    elif occ > 3:
        return 2
    else:
        return 0


def checkAllVacancies(a):
    arr = []
    for i in range(len(a)):
        arr.append([])
        for j in range(len(a[0])):
            arr[i].append(checkVacancy(j, i))

    return arr


def main():
    val = -1
    occCount = 0
    isEq = False
    while not isEq:
        isEq = True
        vals = checkAllVacancies(inst)
        for y in range(len(inst)):
            for x in range(len(inst[0])):
                val = vals[y][x]
                curr = inst[y][x]
                if curr == 'L' and val == 1:
                    inst[y][x] = '#'
                    occCount += 1
                    isEq = False
                if curr == '#' and val == 2:
                    inst[y][x] = 'L'
                    occCount -= 1
                    isEq = False


    print(occCount)


print('part 1')
main()

#-----------------------------------
#part 2


#returns 1 if no occupied seats, 2 if four or more, else 0
def checkVacancy2(x, y):
    occ = 0

    edges.append(x < len(inst[0]) - 1)
    edges.append(x > 0)
    edges.append(y < len(inst) - 1)
    edges.append(y > 0)


    #check for occupancy

    x1 = x
    y1 = y
    y2 = y
    rightFound = False
    toprightFound = False
    botrightFound = False
    while (x1 <= len(inst[0]) - 1) and ((y2 <= len(inst) - 1) or (y1 >= 0)):

        #right
        if inst[y][x1] == '#' and not rightFound:
            occ += 1
            rightFound = True
        elif inst[y][x1] == 'L':
            rightFound = True
    
        #topright
        if (y1 > 0) and inst[y1][x1] == '#' and not toprightFound:
            occ += 1
            toprightFound = True
        elif (tempY > 0) and inst[y1][x1] == 'L':
            toprightFound = True
    
        #botright
        if (y2 < len(inst) - 1) and inst[y2][x1] == '#' and not botrightFound:
            occ += 1
            botrightFound = True
        elif (y2 < len(inst) - 1) and inst[y2][x1] == 'L':
            botrightFound = True
        
        x1+=1
        y1-=1
        y2+=1


    x1 = x
    y1 = y
    y2 = y 
    leftFound = False
    topleftFound = False
    botleftFound = False
    while (x1 >= 0 and ((y2 <= len(inst) - 1) or (y1 >= 0)):

        #left
        if inst[y][x1] == '#' and not leftFound: #left
            occ += 1
            leftFound = True
        elif inst[y][x1] == 'L':
            leftFound = True
    
        #topleft
        if (y1 >= 0) and inst[y1][x1] == '#' and not topleftFound:
            occ += 1
            topleftFound = True
        elif (y1 >= 0) and inst[y1][x1] == 'L':
            topleftFound = True
    
        #botleft
        if (y2 <= len(inst) - 1) and inst[y2][x1] == '#' and not botleftFound:
            occ += 1
            botleftFound = True
        elif (y2 <= len(inst) - 1) and inst[y2][x1] == 'L':
            botleftFound = True
        
        x1-=1
        y1-=1
        y2+=1


    y1 = y 
    while y1 >= 0:
        if inst[y1][x] == '#': #top
            occ += 1
            break
        elif inst[y1][x] == 'L':
            break

        y1-=1


    y1 = y 
    while y1 <= len(inst) - 1:
        if inst[y1][x] == '#': #bottom
            occ += 1
            break
        elif inst[y1][x] == '#': #bottom
            break

        y1+=1


    if occ == 0:
        return 1
    elif occ > 4: #now five or more
        return 2
    else:
        return 0








