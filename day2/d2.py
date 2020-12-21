#part 1
'''
inst = []
valids = 0
with open("input.txt") as file:
    for line in file.readlines():
        inp = line.split(" ")
        r = inp[0].split("-")
        l = inp[1][0]
        p = inp[2].strip()

        count = 0
        for i in p:
            if i == l:
                count+=1

        if count >= int(r[0]) and count <= int(r[1]):
            valids += 1 


print(valids)
'''
#Part 2

inst = []
valids = 0
with open("input.txt") as file:
    for line in file.readlines():
        inp = line.split(" ")
        r = inp[0].split("-")
        l = inp[1][0]
        p = inp[2].strip()
        
        temp = 0
        if p[int(r[0]) - 1] == l:
            temp += 1
        if p[int(r[1]) - 1] == l: 
            temp += 1

        if temp == 1:
            valids += 1
print(valids)






