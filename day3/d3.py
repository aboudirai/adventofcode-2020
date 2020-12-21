#Part1

inst = []

with open("input.txt") as file:
    for line in file.readlines():
        inst.append(line.strip())


t = 0
j = 0
i = 0
print(len(inst[0]))
while i < len(inst) - 1:
    j+=3
    j %= len(inst[0])
    i+=1
    
    if inst[i][j] == '#':
        t += 1
#print(t)



#Part2

inst = []

with open("input.txt") as file:
    for line in file.readlines():
        inst.append(line.strip())

def treeDiag(r, d):
    t = 0
    j = 0
    i = 0
    print(len(inst[0]))
    while i < len(inst) - 1:
        j+=r
        j %= len(inst[0])
        i+=d
        
        if inst[i][j] == '#':
            t += 1

    return t

p = 1

slopes = [[1,1],[3,1], [5,1], [7,1], [1,2]]

for i in slopes:
    p *= treeDiag(i[0], i[1])

print(p)
