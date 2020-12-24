inst = []
PREAMBLE = 25

with open("input.txt") as file:
    for line in file.readlines():
        inst.append(int(line))

#-----------------
#part 1
hmap = {}
for i in range(len(inst)):
    if i < PREAMBLE:
        hmap[inst[i]] = 1
    elif hmap.get(inst[i], -1) == -1: #isnt already in map
        hmap[inst[i]] = 0

def findInvalid():
    isValid = False
    for i in range(PREAMBLE, len(inst)):
        val = inst[i]

        #checking for sum in previous 25
        isValid = False
        for j in range(i-PREAMBLE, i):
            if hmap.get(val-inst[j], -1) == 1:
                isValid = True

        #returning if invalid val found
        if not isValid:
            return inst[i]

        #shift 25 previous nums for current pos
        hmap[inst[i - PREAMBLE]] = 0
        hmap[inst[i]] = 1

invalid = findInvalid()
print('part 1')
print(invalid)


#------------
#part 2

invRange = [inst[0]]
s = sum(invRange) 
invMin = 0
invMax = 0
while s != invalid:
    if s < invalid:
        invMax += 1
        s += inst[invMax]
        invRange.append(inst[invMax])
    elif s > invalid:
        s -= inst[invMin]
        invMin += 1
        invRange = invRange[1:]

print('part 2')
print(min(invRange) + max(invRange))
    




