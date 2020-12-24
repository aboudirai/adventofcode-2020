inst = []

with open("input.txt") as file:
    for line in file.readlines():
        temp = line.split(' ')
        val = temp[1]
        if val[0] == '-':
            val = int(val[1:]) * -1
        else:
            val = int(val[1:])

        inst.append([temp[0], val])

#-----------------
#part 1

acc = 0
pc = 0
visited = []

while pc not in visited:
    visited.append(pc)
    op = inst[pc][0]
    val = inst[pc][1]
    if op == 'acc':
        acc += val
        pc += 1
    elif op == 'jmp':
        pc += val
    else:
        pc += 1

print(acc)

#------------
#part 2

acc = 0
pc = 0
visited = []
insts = []
jmpnnop = 0
while pc not in visited:
    visited.append(pc)
    insts.append(inst)
    op = inst[pc][0]
    val = inst[pc][1]
    if op == 'acc':
        acc += val
        pc += 1
    elif op == 'jmp':
        pc += val
        jmpnnop += 1
    else:
        pc += 1
        jmpnnop += 1


print(jmpnnop)
print(len(insts))
