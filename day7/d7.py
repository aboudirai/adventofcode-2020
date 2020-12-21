inst = []

with open('input.txt') as file:
    revdic = {}
    for line in file.readlines():
        info = line.strip().split('contain')
        bag = info[0][:-6]
        dic = {}
        temp = info[1][:-1]
        templist = temp.split(',')

        for i in range(0, len(templist)):
            if templist[i][1:3] == 'no':
                dic = None
                break

            num = int(templist[i][1])
            if num > 1:
                color = templist[i][3:-5]
            else:
                color = templist[i][3:-4]

            dic[color] = templist[i][1]


            if revdic.get(color, 0) == 0:  
                revdic[color] = [bag]
            else:
                revdic[color].append(bag)


        inst.append([bag, dic])




print(revdic)
#print(inst)
