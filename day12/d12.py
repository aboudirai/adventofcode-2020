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
print()

#################################
#part 2

vert = 0
horz = 0
wvert = 1
whorz = 10

for i in inst:
    code = i[0]
    mag = int(i[1:])
    
    if code in 'RL':
        if mag == 180: #180 or 270
            wvert *= -1
            whorz *= -1
        elif code == 'R':
            if mag == 270:
                wvert *= -1
                whorz *= -1
            temp = wvert
            wvert = -1 * whorz
            whorz = temp
        elif code == 'L':
            if mag == 270:
                wvert *= -1
                whorz *= -1
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
