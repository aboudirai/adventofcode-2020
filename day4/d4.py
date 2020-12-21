#part1
'''
inst = ""

with open("input.txt") as file:
    for line in file.readlines():
        if line == "\n":
            inst += line 
        inst += line.strip() + " "
    
    pp = inst.split("\n")
    count = 0
    for i in pp:
        p = i.split(" ")
        req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for j in p:
            code = j[:3] 
            if code in req:
                req.remove(code)
        
        if req == []:
            count+=1

            
print(count)

'''

#part2

inst = ""

with open("input.txt") as file:
    for line in file.readlines():
        if line == "\n":
            inst += line 
        inst += line.strip() + " "
    
    pp = inst.split("\n")
    count = 0
    for i in pp:
        p = i.split(" ")
        req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for j in p:
            code = j[:3] 
            if code in req:
                if code == "byr" and int(j[4:]) >= 1920 and int(j[4:]) <= 2002:
                    req.remove(code)
                if code == "iyr" and int(j[4:]) >= 2010 and int(j[4:]) <= 2020:
                    req.remove(code)
                if code == "eyr" and int(j[4:]) >= 2020 and int(j[4:]) <= 2030:
                    req.remove(code)
                if code == "hgt":
                    if j[-2:] == "cm":
                        if int(j[4:-2]) >= 150 and int(j[4:-2]) <= 193:   
                            req.remove(code)
                    if j[-2:] == "in":
                        if int(j[4:-2]) >= 59 and int(j[4:-2]) <= 76:   
                            req.remove(code)
                if code == "hcl":
                    if len(j[4:]) == 7:
                        valid = True
                        if j[4] != "#":
                            valid = False
                        for i in range(5, 11):
                            if j[i].lower() not in "abcdef0123456789":
                                valid = False
                        if valid:
                            req.remove(code)
                if code == "ecl" and j[4:] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    req.remove(code)
                if code == "pid" and len(j[4:]) == 9 and j[4:].isnumeric():
                    req.remove(code)
                if code == "cid":
                    req.remove(code)
        if req == []:
            count+=1

            
print(count)

