class node:
    state = []
    cost = 0
    totalCost = 0
    pathTo = []
    zeroPos = []

    def __init__(self, state, path):
        self.state = state
        pathTo = path
        pathTo.append(self)
        self.zeroPos = self.getZeroPos()
        self.cost = self.calcCost() 
        self.totalCost = self.calcTotalCost()   


    def getState(self):
        return self.state

    def getCost(self):
        return self.cost

    def getTotalCost(self):
        return self.totalCost

    def getPathTo(self):
        return self.pathTo

    def getZeroPos(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    zeropos = [i, j]
        return zeropos

    def calcCost(self):
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
        def totalDistance(self):
            sum = 0

            sum += calculateDistance(1, self.state)
            sum += calculateDistance(2, self.state)
            sum += calculateDistance(3, self.state)
            sum += calculateDistance(4, self.state)
            sum += calculateDistance(5, self.state)
            sum += calculateDistance(6, self.state)
            sum += calculateDistance(7, self.state)
            sum += calculateDistance(8, self.state)

            return sum
        dist = totalDistance(self)
        return dist

    def calcTotalCost(self):
        sum = 0
        for n in self.pathTo:
            print(n.getCost())
            sum += n.getCost()
        return sum

    # movement functions
    def up(self):
        row = self.zeroPos[0]
        col = self.zeroPos[1]
        if row == 0:
            raise Exception("can't move up from here!")
        temp = self.state[row - 1][col]
        self.state[row - 1][col] = self.state[row][col]
        self.state[row][col] = temp
    def down(self):
        row = self.zeroPos[0]
        col = self.zeroPos[1]
        if row == 0:
            raise Exception("can't move up from here!")
        temp = self.state[row + 1][col]
        self.state[row + 1][col] = self.state[row][col]
        self.state[row][col] = temp
    def left(self):
        row = self.zeroPos[0]
        col = self.zeroPos[1]
        if row == 0:
            raise Exception("can't move up from here!")
        temp = self.state[row][col - 1]
        self.state[row][col - 1] = self.state[row][col]
        self.state[row][col] = temp
    def right(self):
        row = self.zeroPos[0]
        col = self.zeroPos[1]
        if row == 0:
            raise Exception("can't move up from here!")
        temp = self.state[row][col + 1]
        self.state[row][col + 1] = self.state[row][col]
        self.state[row][col] = temp

    # returns result of movement functions
    def getUp(self):
        try:
            self.up()
            temp = self.state
            self.down()
            return node(temp, self.pathTo)
        except Exception as e:
            raise e
    def getDown(self):
        try:
            self.down()
            temp = self.state
            self.up()
            return node(temp, self.pathTo)
        except Exception as e:
            raise e
    def getLeft(self):
        try:
            self.left()
            temp = self.state
            self.right()
            return node(temp, self.pathTo)
        except Exception as e:
            raise e
    def getRight(self):
        try:
            self.up()
            temp = self.state
            self.down()
            return node(temp, self.pathTo)
        except Exception as e:
            raise e