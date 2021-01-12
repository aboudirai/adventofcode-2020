inst = []
with open('input.txt') as file:
    for line in file.readlines():
        inst.append(line.strip())


################################
#part 1

dirs = {}
dirs[0] = 'N'
dirs[1] = 'E'
dirs[2] = 'S'
dirs[3] = 'W'

d = 1

vert = 0
horz = 0

for i in inst:
    code = i[0]
    mag = int(i[1:])
    
    rot = 0
    
    if code in 'RL':
        rot = mag // 90 #int division to get number of rotations
        if code == 'R':
            d = (d + rot) % 4
        elif code == 'L':
            d = (d - rot) % 4
    elif code == 'F':
        code = dirs[d]

    #cardinal directions
    if code == 'N':
        vert += mag
    elif code == 'S':
        vert -= mag
    elif code == 'E':
        horz += mag
    elif code == 'W':
        horz -= mag

print('part 1')
print(abs(horz) + abs(vert))

#################################
#part 2
d = 1

vert = 0
horz = 0
wvert = 10
whorz = 1

for i in inst:
    code = i[0]
    mag = int(i[1:])
    
    rot = 0
    
    if code in 'RL':
        rot = mag // 90 #int division to get number of rotations
        if rot == 180:
            wvert *= -1
            whorz *= -1
        elif code == 'R':
            if wvert > 0:
                if whorz > 0:
                    temp = whorz
                    whorz = wvert
                    wvert = -1 * temp
                else:
                    temp = whorz
                    whorz = wvert
                    wvert = -1 * temp
            else:
                if whorz > 0:
                    temp = whorz
                    whorz = wvert
                    wvert = -1 * temp
                else:
                    temp = whorz
                    whorz = wvert
                    wvert = -1 * temp
        elif code == 'L':
            if wvert > 0:
                if whorz > 0:
                    temp = whorz
                    whorz = -1 * wvert
                    wvert = temp
                else:
                    temp = whorz
                    whorz = -1 * wvert
                    wvert = temp
            else:
                if whorz > 0:
                    temp = whorz
                    whorz = -1 * wvert
                    wvert = temp
                else:
                    temp = whorz
                    whorz = -1 * wvert
                    wvert = temp
    elif code == 'F':
        vert += (mag * wvert)
        horz += (mag * whorz)
    elif code == 'N':
        wvert += mag
    elif code == 'S':
        wvert -= mag
    elif code == 'E':
        whorz += mag
    elif code == 'W':
        whorz -= mag


print('part 2')
print(abs(horz) + abs(vert))


