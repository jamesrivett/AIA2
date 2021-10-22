import random

# globals
goal = [[1, 2, 3],[8, 0, 4],[7, 6, 5]]
init = [[1, 2, 3],[8, 0, 4],[7, 6, 5]]

# print current state and goal position
def printBoard(state):
    print("Current:    Goal:")
    for i in range(3):
        print(str(state[i]) + " | " + str(goal[i]))

# fills init list with distinct random values from 0 to 8
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

def scramble(amt, state):
    print("Scrambling board by " + str(amt) + " random moves")
    for i in range(amt):
        move = random.randint(0, 3)

        if move == 0:
            moveSuccess = up(state)
            if not moveSuccess: i += 1
        if move == 1:
            moveSuccess = down(state)
            if not moveSuccess: i += 1
        if move == 2:
            moveSuccess = left(state)
            if not moveSuccess: i += 1
        if move == 3:
            moveSuccess = right(state)
            if not moveSuccess: i += 1

# calculates num's distance to its goal position
def calculateDistance(num, state):
    numpos = []
    goalpos = []

    # calculate num's position in state array
    for i in range(3):
        for j in range(3):
            if state[i][j] == num:
                numpos = [i, j]

    # switch statement for goal positions
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

# calculate distance of all nums out of place
def totalDistance(state):
    sum = 0

    sum += calculateDistance(1, state)
    sum += calculateDistance(2, state)
    sum += calculateDistance(3, state)
    sum += calculateDistance(4, state)
    sum += calculateDistance(5, state)
    sum += calculateDistance(6, state)
    sum += calculateDistance(7, state)
    sum += calculateDistance(8, state)

    return sum

# returns false until state matches goal state
def goalState(state):
    isGoalState = True
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal [i][j]:
                isGoalState = False
    
    return isGoalState

# find position of zero
def findZero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zeropos = [i, j]
    return zeropos

# calculate possible moves
def possMoves(last, state):
    zeropos = []
    moves = []
    zeropos = findZero(state)
    print("last move: " + last)

    # calculate possible vertical moves
    if zeropos[0] == 0 and last != "up":
        moves.append("down")

    if zeropos[0] == 1:
        if last != "down":
            moves.append("up")
        if last != "up":
            moves.append("down")

    if zeropos[0] == 2 and last != "down":
        moves.append("up")


    # calculate possible horizontal moves
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

# calculate costs for moves
def moveCost(moves, state):
    costs = [[] for r in range(len(moves))]
    for i in range(len(moves)):
        if moves[i] == "up":
            up(state)
            costs[i].append("up")
            costs[i].append(totalDistance(state))
            down(state)

        if moves[i] == "down":
            down(state)
            costs[i].append("down")
            costs[i].append(totalDistance(state))
            up(state)
        if moves[i] == "left":
            left(state)
            costs[i].append("left")
            costs[i].append(totalDistance(state))
            right(state)

        if moves[i] == "right":
            right(state)
            costs[i].append("right")
            costs[i].append(totalDistance(state))
            left(state)

    return costs

# Make children 

# move functions ---------------------------------
def up(state):
    zeropos = findZero(state)
    row = zeropos[0]
    col = zeropos[1]
    if row == 0:
        print("can't move up from here!")
        return False

    temp = state[row - 1][col]
    state[row - 1][col] = state[row][col]
    state[row][col] = temp
    return True

def down(state):
    zeropos = findZero(state)
    row = zeropos[0]
    col = zeropos[1]
    if row == 2:
        print("can't move down from here!")
        return False

    temp = state[row + 1][col]
    state[row + 1][col] = state[row][col]
    state[row][col] = temp
    return True
    
def left(state):
    zeropos = findZero(state)
    row = zeropos[0]
    col = zeropos[1]
    if col == 0:
        print("can't move left from here!")
        return False

    temp = state[row][col - 1]
    state[row][col - 1] = state[row][col]
    state[row][col] = temp
    return True

def right(state):
    zeropos = findZero(state)
    row = zeropos[0]
    col = zeropos[1]
    if col == 2:
        print("can't move right from here!")
        return False

    temp = state[row][col + 1]
    state[row][col + 1] = state[row][col]
    state[row][col] = temp
    return True
# ------------------------------------------------

# Best First Search Function | Each funcion call is one step
def bfs(last, state):
    printBoard(state)
    lowestCost = 100
    lowestMove = "none"
    costs = moveCost(possMoves(last, state), state)

    # find move with lowest cost
    for i in range(len(costs)):
        if costs[i][1] < lowestCost:
            lowestCost = costs[i][1]
            lowestMove = costs[i][0]

    print("moving to: " + lowestMove)

    # make move with lowest cost
    if lowestMove == "up":
        up(state)
        return "up"
    if lowestMove == "down":
        down(state)
        return "down"
    if lowestMove == "left":
        left(state)
        return "left"
    if lowestMove == "right":
        right(state)
        return "right"
    
# main
def main():
    lastMove = ""
    scramble(20, init)
    printBoard(init)
    print("BEGIN")
    print("-----------------------------------")
    totalMoves = 0

    while not goalState(init):
        lastMove = bfs(lastMove, init)
        totalMoves += 1

    printBoard(init)
    print("-----------------------------------")
    print("Finished! Total Moves: " + str(totalMoves))
    print("-----------------------------------")


if __name__ == "__main__":
    main()