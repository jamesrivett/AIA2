import random

#globals
goal = [[1, 2, 3],[8, 0, 4],[7, 6, 5]]
init = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

#fills init list with distinct random values from 0 to 8
def fillInit():
    used = []
    for i in range(3):
        for j in range(3):
            while True:
                cont = False
                num = random.randint(0, 8)

                for element in used:
                    if element == num:
                        cont = True
                        break
                if cont == True: continue

                init[i][j] = num
                used.append(num)
                break

#calculates num's distance to its goal position
def calculateDistance(num):
    numpos = []
    goalpos = []

    #calculate num's position in init array
    for i in range(3):
        for j in range(3):
            if init[i][j] == num:
                numpos = [i, j]

    #switch statement for goal positions
    if num == 0:
        goalpos = [1, 1]
    if num == 1:
        goalpos = [0, 0]
    if num == 2:
        goalpos = [0, 1]
    if num == 3:
        goalpos = [0, 2]
    if num == 4:
        goalpos = [1, 2]
    if num == 5:
        goalpos = [2, 2]
    if num == 6:
        goalpos = [2, 1]
    if num == 7:
        goalpos = [2, 0]
    if num == 8:
        goalpos = [1, 0]

    distance = abs(numpos[0] - goalpos[0]) + abs(numpos[1] - goalpos[1])
    return distance

#calculate distance of all nums out of place
def totalDistance():
    sum = 0

    sum += calculateDistance(1)
    sum += calculateDistance(2)
    sum += calculateDistance(3)
    sum += calculateDistance(4)
    sum += calculateDistance(5)
    sum += calculateDistance(6)
    sum += calculateDistance(7)
    sum += calculateDistance(8)

    return sum

#returns false until init matches goal state
def goalState():
    isGoalState = True
    for i in range(3):
        for j in range(3):
            if init[i][j] != goal [i][j]:
                isGoalState = False
    
    return isGoalState

def possMoves():
    zeropos = []
    moves = []

    #find position of zero
    for i in range(3):
        for j in range(3):
            if init[i][j] == 0:
                zeropos = [i, j]

    #all moves possible if in middle
    if zeropos == [1, 1]:
        moves.append("up")
        moves.append("down")
        moves.append("left")
        moves.append("right")
        return moves

    #calculate possible vertical moves
    if zeropos[0] == 0:
        moves.append("down")
    if zeropos[0] == 1:
        moves.append("up")
        moves.append("down")
    if zeropos[0] == 2:
        moves.append("up")


    #calculate possible horizontal moves
    if zeropos[1] == 0:
        moves.append("right")
    if zeropos[1] == 1:
        moves.append("left")
        moves.append("right")
    if zeropos[1] == 2:
        moves.append("left")

    return moves


#main
def main():
    fillInit()
    for i in range(3):
        print(str(init[i]) + " " + str(goal[i]))
    print(totalDistance())
    print(goalState())
    print(possMoves())

if __name__ == "__main__":
    main()