inst = []
with open("input.txt") as file:

    for line in file.readlines():
        inst.append(int(line))

inst = (sorted(inst))

#part 1
'''
for i in range(len(inst)):
    for j in range(len(inst)-1, i, -1):
        if inst[i] + inst[j] == 2020:
            print(inst[i] * inst[j])
'''

#part2
dic = {}

for i in range(len(inst)):
    for j in range(len(inst)-1, i, -1):
        s = inst[i] + inst[j]
        if s < 2020:
            dic[s] = [inst[i], inst[j]]

for i in range(len(inst)):
    g = dic.get(2020-inst[i], 0) 
    if g != 0:
        print(g[0] * g[1] * inst[i])
        

