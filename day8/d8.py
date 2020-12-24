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

print('part 1')
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

def findCorruptInst():
    print('part 2')
    for i in range(len(inst)):

        #flip instruction
        if inst[i][0] == 'nop':
            inst[i][0] = 'jmp'
        elif inst[i][0] == 'jmp':
            inst[i][0] = 'nop'
        
        if inst[i][0] != 'acc':
            acc = 0
            pc = 0
            visited = []
            while pc not in visited and pc < (len(inst)):
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
           
            #if fix caused correct termination
            if pc == len(inst):
                print(acc)
                return

        #replace instruction
        if inst[i][0] == 'nop':
            inst[i][0] = 'jmp'
        elif inst[i][0] == 'jmp':
            inst[i][0] = 'nop'


findCorruptInst()
