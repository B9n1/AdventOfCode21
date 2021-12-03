with open('03-input.txt') as file:
    data = file.readlines()
data = [x[:-1] for x in data]
gammaRate = ''
epsilonRate = ''

for count, value in enumerate(data[0]):
    zero = 0
    one = 0

    if count == len(data[0])-1:
        break
    for number in data:
        if int(number[count]) == 1:
            one += 1
        else:
            zero += 1

    if zero > one:
        gammaRate += '0'
        epsilonRate += '1'
    else:
        gammaRate += '1'
        epsilonRate += '0'

print("Power Consumption is: ", int(gammaRate, 2) * int(epsilonRate, 2))

OxygenGeneratorRating = data[:]
CO2ScrubberRating = data[:]

for count, value in enumerate(data[0]):
    elements = 0
    for i, number in enumerate(OxygenGeneratorRating):
        if bool(number.strip()):
            elements += 1
    if elements == 1:
        break
    zero = 0
    one = 0
    for number in OxygenGeneratorRating:
        if bool(number.strip()):
            if int(number[count]) == 1:
                one += 1
            if int(number[count]) == 0:
                zero += 1

    if zero > one:
        for i, number in enumerate(OxygenGeneratorRating):
            if bool(number.strip()):
                if int(number[count]) == 1:
                    OxygenGeneratorRating[i] = ""
    else:
        for i, number in enumerate(OxygenGeneratorRating):
            if bool(number.strip()):
                if int(number[count]) == 0:
                    OxygenGeneratorRating[i] = ""

for count, value in enumerate(data[0]):
    elements = 0
    for i, number in enumerate(CO2ScrubberRating):
        if bool(number.strip()):
            elements += 1
    if elements == 1:
        break
    zero = 0
    one = 0
    for number in CO2ScrubberRating:
        if bool(number.strip()):
            if int(number[count]) == 1:
                one += 1
            if int(number[count]) == 0:
                zero += 1

    if zero > one:
        for i, number in enumerate(CO2ScrubberRating):
            if bool(number.strip()):
                if int(number[count]) == 0:
                    CO2ScrubberRating[i] = ""
    else:
        for i, number in enumerate(CO2ScrubberRating):
            if bool(number.strip()):
                if int(number[count]) == 1:
                    CO2ScrubberRating[i] = ""



Solution1 = 0
Solution2 = 0
for i, number in enumerate(CO2ScrubberRating):
    if bool(number.strip()):
        Solution2 = int(CO2ScrubberRating[i], 2)
for i, number in enumerate(OxygenGeneratorRating):
    if bool(number.strip()):
        Solution1 = int(OxygenGeneratorRating[i], 2)
print("The life support rating of the submarine is: ", Solution2*Solution1)

