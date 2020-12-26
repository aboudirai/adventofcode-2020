inst = []

with open("input.txt") as file:
    for line in file.readlines():
        inst.append(int(line))
    
    inst = [0] + inst
    inst.append(max(inst) + 3)
    inst.sort()

#-----------------
#part 1

ones = 0
threes = 0

for i in range(len(inst) - 1):
    if inst[i+1] - inst[i] == 1:
        ones += 1
    elif inst[i+1] - inst[i] == 3:
        threes += 1

print('part 1')
print(ones * threes)

#------------
#part 2
def dpPath(dp):
    for i in range(len(inst)):
        dp.append(0)
    dp[0] = 1

    for i in range(len(inst)-1):
        val = inst[i]

        if (val + 1) in inst:
            dp[inst.index(val + 1)] += dp[i]
        if (val + 2) in inst:
            dp[inst.index(val + 2)] += dp[i]
        if (val + 3) in inst:
            dp[inst.index(val + 3)] += dp[i]

dp = []
dpPath(dp)
print('part 2')
print(dp[-1])




