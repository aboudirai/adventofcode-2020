inst = []

with open("input.txt") as file:
    group = []
    for line in file.readlines():
        if line == "\n":
            inst.append(group)
            group = []
        else:
            group.append(line.strip())
    inst.append(group)

#part 1
qsum = 0
for i in inst:
    qmap = {}
    qcurr = 0
    for j in i:
        if qmap.get(j, 0) == 0:
            qcurr += 1
            qmap[j] = 1

    qsum += qcurr

qsum = 0
for i in inst:
    qmap = {}
    qcurr = 0
    for j in i:
        for k in j:
            if qmap.get(k, 0) == 0:
                qmap[k] = 1
            else:
                qmap[k] += 1
       
    for j in qmap.keys():
        if qmap[j] == len(i):
            qcurr += 1

    qsum += qcurr

print(qsum)
