inst = {}
revdic = {}
with open('input.txt') as file:
    for line in file.readlines():
        info = line.strip().split('contain')
        bag = info[0][:-6]
        temp = info[1][:-1]
        templist = temp.split(',')
        dic = {}

        for i in range(0, len(templist)):
            if templist[i][1:3] == 'no':
                dic = None
                break

            num = int(templist[i][1])
            if num > 1:
                color = templist[i][3:-5]
            else:
                color = templist[i][3:-4]

            dic[color] = int(templist[i][1])


            if revdic.get(color, 0) == 0:  
                revdic[color] = [bag]
            else:
                revdic[color].append(bag)


        inst[bag] = dic

#part 1

count = 0
colors = []

def getParentBag(bag, colors):
    temp = revdic.get(bag, 0)
    if temp == 0:
        return

    for i in temp:
        if i not in colors:
            colors.append(i)
            getParentBag(i, colors)


getParentBag('shiny gold', colors)
print(len(colors))


#-------------------

#part 2

def getSubBag(bag):
    if inst[bag] is None:
        return 0 

    total = 0 
    for i in inst[bag].keys():
        total += (inst[bag][i] + (inst[bag][i] * getSubBag(i)))
    
    return total


print(getSubBag('shiny gold'))
