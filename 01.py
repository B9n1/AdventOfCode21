data = []
with open('01-input.txt') as file:
    data = file.readlines()

countIncreased = 0
for count, value in enumerate(data):
    if int(data[count]) > int(data[count-1]) and not count == 0:
        countIncreased += 1


print('Solution 1:', countIncreased)

countIncreased = 0
for count, value in enumerate(data):
    if int(data[count]) + int(data[count-1]) + int(data[count-2]) > int(data[count-1]) + int(data[count-2]) + int(data[count-3]) and count > 2:
        countIncreased += 1
print('Solution 2:', countIncreased)