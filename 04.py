import numpy as np
with open('04-input.txt') as file:
    data = file.readlines()

numbers = data[0].split(',')
data.pop(0)
data = [x[:-1] for x in data]

class player:
    def __init__(self, board):
        self.board = board
        self.count = 0

    def removeNumber(self, number):
        if number in self.board:
            self.board[self.board == number] = -1
            self.count += 1

    def getScore(self, number):
        self.board = self.board.astype('int')
        #print(self.board)
        #print(number)
        #print(self.count)
        #print(int(self.board.sum())+self.count)
        result = (int(self.board.sum())+self.count) * int(number)

        return int(result)

    def scannRowAmdCollums(self):
        colums =[]
        for value in range(len(self.board)):
            colums.append(self.board[:, value])

        if self.checkBingo(colums) or self.checkBingo(self.board):
            return True
        else:
            return False

    def checkBingo(self, array):

        for ary in array:
            rowElement = 0
            for value in ary:
                if int(value) == -1:
                    rowElement += 1
                    if rowElement == len(ary):
                        return True

        return False

boards =[]
for i, value in enumerate(data):
    arr = [ x.strip() for x in data[i].strip('[]').split(' ')]
    while("" in arr) :
        arr.remove("")
    boards.append(arr)
num = int(len(boards) / 6)
bestRound = 99
bestScore = 0
worstRound = 0
worstScore = 0

for b in range(num):
    ary = [boards[1], boards[2], boards[3], boards[4], boards[5]]
    for i in range(6):
        if len(boards) >= 0:
            boards.pop(0)
    ary = np.array(ary)
    p = player(ary)
    #print(p.board)
    for i, n in enumerate(numbers):
        p.removeNumber(n)
        if p.scannRowAmdCollums():
            print("Board: ", b+1, " Needed Rounds: ", i+1, " Scored: ", p.getScore(n))
            if i < bestRound:
                bestRound = i
                bestScore = p.getScore(n)
            if i > worstRound:
                worstRound = i
                worstScore = p.getScore(n)
            break

print("Best Round Amount: ", bestRound, " Best Score: ", bestScore)
print("Worst Round Amount: ", worstRound, " Worst Score: ", worstScore)

