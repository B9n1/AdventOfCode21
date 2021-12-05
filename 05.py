import numpy as np

for part in range(2):
    with open('05-input.txt') as file:
        data = file.readlines()
    data = [x[:-1] for x in data]
    diagram = np.zeros((1000, 1000))
    diagram = diagram.astype('int')
    lineFrom = []
    lineTo = []
    for values in data:
        ary = values.split('->')
        lineFrom.append(ary[0].split(','))
        lineTo.append(ary[1].split(','))

    for i, FROM in enumerate(lineFrom):
        TOX = int(lineTo[i][0])
        TOY = int(lineTo[i][1])
        FROMX = int(FROM[0])
        FROMY = int(FROM[1])
        if TOX == FROMX:
            diagram[TOY][TOX] += 1
            dif = TOY - FROMY
            for y in range(abs(dif)):
                u = int(dif / abs(dif))
                diagram[FROMY + y * u][TOX] += 1
        elif TOY == FROMY:
            diagram[TOY][TOX] += 1
            dif = TOX - FROMX
            for x in range(abs(dif)):
                u = int(dif/abs(dif))
                diagram[FROMY][FROMX + x * u] += 1
        elif part == 1:
            diagram[TOY][TOX] += 1
            dify = TOY - FROMY
            difx = TOX - FROMX
            ux = int(difx / abs(difx))
            uy = int(dify / abs(dify))
            for i in range(abs(dify)):
                diagram[FROMY + i * uy][FROMX + i * ux] += 1

    count = np.count_nonzero(diagram > 1)
    print("Solution ", part+1, " : ", count)
