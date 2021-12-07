import numpy as np
with open('07-input.txt') as file:
    data = file.readlines()
data = [x[:-1] for x in data]
crabs = np.array(data[0].split(','))
crabs = crabs.astype('int')

leastFuel = 99999999999999

for i in range(np.amax(crabs)):
    Fuel = 0
    for c in crabs:
        Fuel += abs(i-c)
    if Fuel < leastFuel:
        leastFuel = Fuel

print("Least Fuel Method One:", leastFuel)

leastFuel = 99999999999999

for i in range(np.amax(crabs)):
    Fuel = 0
    for c in crabs:
        for a in range(abs(i-c)):
            Fuel += a+1
    if Fuel < leastFuel:
        leastFuel = Fuel

print("Least Fuel Method Two:", leastFuel)
