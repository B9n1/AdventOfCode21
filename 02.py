data = []
with open('02-input.txt') as file:
    data = file.readlines()

horizontal = 0
depth = 0

for count, value in enumerate(data):
    values = data[count].split()
    if values[0] == "forward":
        horizontal += int(values[1])
    if values[0] == "up":
        depth -= int(values[1])
    if values[0] == "down":
        depth += int(values[1])

print("Solution 1:", depth * horizontal)

horizontal = 0
depth = 0
aim = 0

for count, value in enumerate(data):
    values = data[count].split()
    if values[0] == "forward":
        horizontal += int(values[1])
        depth += aim * int(values[1])
    if values[0] == "up":
        aim -= int(values[1])
    if values[0] == "down":
        aim += int(values[1])

print("Solution 2:", depth * horizontal)