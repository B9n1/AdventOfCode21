import numpy as np
with open('08-input.txt') as file:
    data = file.readlines()
data = [x[:-1] for x in data]


def sortString(str):
    return ''.join(sorted(str))


output = []
signal = []
for d in data:
    tmp = d.split("|")
    signal += tmp[0].split()
    output += tmp[1].split()

count = 0
values = {2, 3, 4, 7}
for o in output:
    if len(o) in values:
        count += 1

print(count)
sum = 0
for d in data:
    tmp = d.split("|")
    sig = tmp[0].split()
    out = tmp[1].split()
    num = ["", "", "", "", "", "", "", "", "", ""]
    #           a0 b1  c2  d3  e4  f5  g6
    segment = ["", "", "", "", "", "", ""]
    for s in sig:
        if len(s) == 2:
            num[1] = s
        if len(s) == 3:
            num[7] = s
        if len(s) == 4:
            num[4] = s
        if len(s) == 7:
            num[8] = s
    # Getting Segment a
    for i in num[7]:
        if i not in num[1]:
             segment[0] = i

    # Getting Segment g
    for s in sig:
        t = ""
        if len(s) == 6:
            for i in s:
                if i not in num[4]+segment[0]:
                    t += i
        if len(t) == 1:
            segment[6] = t

    # Getting Segment e

    for i in num[8]:
        if i not in num[4]+segment[0]+segment[6]:
            segment[4] = i

    # Getting Segment b
    for s in sig:
        t = ""
        if len(s) == 6:
            for i in s:
                if i not in num[1]+segment[0]+segment[6]+segment[4]:
                    t += i
        if len(t) == 1:
            segment[1] = t

    # Getting Segment d
        for i in num[4]:
            if i not in num[1] + segment[1]:
                segment[3] = i
    # Getting Segment f
    for s in sig:
        t = ""
        if len(s) == 6:
            for i in s:
                if i not in segment[0] + segment[1] + segment[3] + segment[4] + segment[6]:
                    t += i
        if len(t) == 1:
            segment[5] = t
    # Getting Segment c
    for i in num[1]:
        if i not in segment[5]:
            segment[2] = i

    ########################
    t = ""

    for o in out:
        o = sortString(o)
        if len(o) == 2:
            t += "1"
        elif len(o) == 3:
            t += "7"
        elif len(o) == 4:
            t += "4"
        elif len(o) == 7:
            t += "8"
        elif o == sortString(segment[0]+segment[1]+segment[2]+segment[4]+segment[5]+segment[6]):
            t += "0"
        elif o == sortString(segment[0]+segment[2]+segment[3]+segment[4]+segment[6]):
            t += "2"
        elif o == sortString(segment[0]+segment[2]+segment[3]+segment[5]+segment[6]):
            t += "3"
        elif o == sortString(segment[0]+segment[1]+segment[2]+segment[3]+segment[5]+segment[6]):
            t += "9"
        elif o == sortString(segment[0]+segment[1]+segment[4]+segment[3]+segment[5]+segment[6]):
            t += "6"
        else:
            t += "5"
    sum += int(t)


print(sum)


#for i in range(len(output)):