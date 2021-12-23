import random



def printSudoku(array):
    for line in array:
        for i in range(9):
            if i % 3 == 0:
                print("|", end="")
            print(line[i], end="")
        print("|")

def lineOfMain():
    line = []
    for i in range(9):
        line.append(random.randint(0, 9))
    return line

def mainArray():
    i = 0
    mainGrid = []
    for i in range(9):
        mainGrid.append(lineOfMain())
    printSudoku(mainGrid)





mainArray()