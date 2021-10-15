import random
import time

#globals
goal = [[1, 2, 3],[8, 0, 4],[7, 6, 5]]
init = [[1, 2, 3],[8, 0, 4],[7, 6, 5]]

#print current state and goal position
def printBoard():
    print("Current:    Goal:")
    for i in range(3):
        print(str(init[i]) + " | " + str(goal[i]))

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

def scramble(amt):
    print("Scrambling board by " + str(amt) + " random moves")
    for i in range(amt):
        move = random.randint(0, 3)

        if move == 0:
            moveSuccess = up()
            if not moveSuccess: i += 1
        if move == 1:
            moveSuccess = down()
            if not moveSuccess: i += 1
        if move == 2:
            moveSuccess = left()
            if not moveSuccess: i += 1
        if move == 3:
            moveSuccess = right()
            if not moveSuccess: i += 1

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

#find position of zero
def findZero():
    for i in range(3):
        for j in range(3):
            if init[i][j] == 0:
                zeropos = [i, j]
    return zeropos

#calculate possible moves
def possMoves(last):
    zeropos = []
    moves = []
    zeropos = findZero()
    print("last move: " + last)

    #calculate possible vertical moves
    if zeropos[0] == 0 and last != "up":
        moves.append("down")

    if zeropos[0] == 1:
        if last != "down":
            moves.append("up")
        if last != "up":
            moves.append("down")

    if zeropos[0] == 2 and last != "down":
        moves.append("up")


    #calculate possible horizontal moves
    if zeropos[1] == 0 and last != "left":
        moves.append("right")

    if zeropos[1] == 1:
        if  last != "right":
            moves.append("left")
        if  last != "left":
            moves.append("right")

    if zeropos[1] == 2 and last != "right":
        moves.append("left")

    print("possible moves: " + str(moves))
    return moves

#calculate costs for moves
def moveCost(moves):
    costs = [[] for r in range(len(moves))]
    for i in range(len(moves)):
        if moves[i] == "up":
            up()
            costs[i].append("up")
            costs[i].append(totalDistance())
            down()

        if moves[i] == "down":
            down()
            costs[i].append("down")
            costs[i].append(totalDistance())
            up()
        if moves[i] == "left":
            left()
            costs[i].append("left")
            costs[i].append(totalDistance())
            right()

        if moves[i] == "right":
            right()
            costs[i].append("right")
            costs[i].append(totalDistance())
            left()

    return costs

#move functions {
def up():
    zeropos = findZero()
    row = zeropos[0]
    col = zeropos[1]
    if row == 0:
        print("can't move up from here!")
        return False

    temp = init[row - 1][col]
    init[row - 1][col] = init[row][col]
    init[row][col] = temp
    return True

def down():
    zeropos = findZero()
    row = zeropos[0]
    col = zeropos[1]
    if row == 2:
        print("can't move down from here!")
        return False

    temp = init[row + 1][col]
    init[row + 1][col] = init[row][col]
    init[row][col] = temp
    return True
    
def left():
    zeropos = findZero()
    row = zeropos[0]
    col = zeropos[1]
    if col == 0:
        print("can't move left from here!")
        return False

    temp = init[row][col - 1]
    init[row][col - 1] = init[row][col]
    init[row][col] = temp
    return True

def right():
    zeropos = findZero()
    row = zeropos[0]
    col = zeropos[1]
    if col == 2:
        print("can't move right from here!")
        return False

    temp = init[row][col + 1]
    init[row][col + 1] = init[row][col]
    init[row][col] = temp
    return True
# }

#Best First Search Function | Each funcion call is one step
def bfs(last):
    printBoard()
    lowestCost = 100
    lowestMove = "none"
    costs = moveCost(possMoves(last))

    #find move with lowest cost
    for i in range(len(costs)):
        if costs[i][1] < lowestCost:
            lowestCost = costs[i][1]
            lowestMove = costs[i][0]

    print("moving to: " + lowestMove)

    #make move with lowest cost
    if lowestMove == "up":
        up()
        return "up"
    if lowestMove == "down":
        down()
        return "down"
    if lowestMove == "left":
        left()
        return "left"
    if lowestMove == "right":
        right()
        return "right"
        

#main
def main():
    lastMove = ""
    scramble(20)
    print("BEGIN")
    print("-----------------------------------")
    totalMoves = 0

    while not goalState():
        lastMove = bfs(lastMove)
        totalMoves += 1

    print("Finished! Total Moves: " + str(totalMoves))

if __name__ == "__main__":
    main()