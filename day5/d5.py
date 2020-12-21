inst = []

with open("input.txt") as file:
    for line in file.readlines():
        inst.append(line.strip())

seatmap = {}
seats = []
for i in range(128):
    seats.append([0, 0, 0, 0, 0, 0, 0, 0])

maxseat = 0

for i in inst:
    rmin = 0
    rmax = 127
    cmin = 0
    cmax = 7
    r = 0
    c = 0
    m = 0
    for j in range(6):
        m = (rmax + rmin) // 2
        if i[j] == "B":
            rmin = m + 1
        elif i[j] == "F":
            rmax = m
    if i[6] == "B":
        r = rmax 
    elif i[6] == "F":
        r = rmin

    for j in range(7, 9):
        m = (cmax + cmin) // 2
        if i[j] == "R":
            cmin = m + 1
        elif i[j] == "L":
            cmax = m
    if i[9] == "R":
        c = cmax 
    elif i[9] == "L":
        c = cmin

    seatid = r*8 + c
    seats[r][c] = seatid
    seatmap[seatid] = 1
    if seatid > maxseat:
        maxseat = seatid

print(maxseat)


#part2
for i in range(len(seats)):
    for j in range(len(seats[i])):
        sid = i*8+j
        if seatmap.get(sid, 0) == 0:
            if seatmap.get(sid+1, 0) != 0 and seatmap.get(sid-1, 0) != 0 :
                print(i*8 + j)


