import numpy as np

with open('06-input.txt') as file:
    data = file.readlines()
data = [x[:-1] for x in data]
fish = np.array(data[0].split(','))
fish = fish.astype('int')
# This was to slow and used too much Memory
"""""
for day in range(80):
    for count, f in enumerate(fish):
        if fish[count] == 0:
            fish = np.append(fish, 8)
            fish[count] = 7
        fish[count] -= 1
    print("After ", day + 1, "day(s)", fish)

print(len(fish))

for day in range(256):
    fish = np.append(fish, np.full(np.count_nonzero(fish == 0), 9))
    fish = np.where(fish == 0, 7, fish)
    fish -= 1
    print("Day", day + 1)
"""""
# But funny, it is so simple if you think about it
fishState = np.array(
    [np.count_nonzero(fish == 0),
     np.count_nonzero(fish == 1),
     np.count_nonzero(fish == 2),
     np.count_nonzero(fish == 3),
     np.count_nonzero(fish == 4),
     np.count_nonzero(fish == 5),
     np.count_nonzero(fish == 6),
     np.count_nonzero(fish == 7),
     np.count_nonzero(fish == 8),
     ])
for day in range(256):
    tmp = fishState[0]
    fishState = [fishState[1], fishState[2], fishState[3], fishState[4], fishState[5], fishState[6], fishState[7] + fishState[0], fishState[8], fishState[0]]
    if day == 79 or day == 255:
        print("Fish population on Day", day+1, ":", np.sum(fishState))


