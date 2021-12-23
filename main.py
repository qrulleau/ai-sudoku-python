import random

print("hello")

def writeGridSudoku():
    i = 0
    tableau = []
    while i < 9:
        tableau.append(random.randint(0, 9))
        i+=1
    print(tableau)

def mainTableau():
    i = 0
    mainGrid = []
    for i in range(9):
        pieceOfGrid = []
        for i in range(9):
            pieceOfGrid.append(random.randint(0, 9))
        mainGrid.append(pieceOfGrid)
    print(mainGrid)

mainTableau()