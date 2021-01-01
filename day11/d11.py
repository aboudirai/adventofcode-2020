inst = []

with open("input.txt") as file:
    for line in file.readlines():
        temp = []
        for i in line.strip():
            temp.append(i)
        inst.append(temp)

#-----------------
#part 1
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
    if edges[RIGHT]: #right
        if inst[y][x+1] == '#':
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

        print('loop')
        print(occCount)
        print(inst)
        print(vals)

    print()
    print(occCount)
main()

#------------
#part 2
