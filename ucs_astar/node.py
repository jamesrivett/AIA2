class node:
    state = []
    cost = 0
    pathTo = []
    zeroPos = []

    def __init__(self, state, path):
        self.state = state
        pathTo = path
        pathTo.append(self)
        self.zeroPos = self.getZeroPos()
    


    def getState(self):
        return self.state

    def getCost(self):
        return self.cost

    def getPathTo(self):
        return self.pathTo

    def getZeroPos(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    zeropos = [i, j]
        return zeropos


    # movement functions
    def up(self):
        row = self.zeroPos[0]
        col = self.zeroPos[1]
        if row == 0:
            print("can't move up from here!")
            return False
        temp = self.state[row - 1][col]
        self.state[row - 1][col] = self.state[row][col]
        self.state[row][col] = temp
    def down(self):
        row = self.zeroPos[0]
        col = self.zeroPos[1]
        if row == 0:
            print("can't move up from here!")
            return False
        temp = self.state[row + 1][col]
        self.state[row + 1][col] = self.state[row][col]
        self.state[row][col] = temp
    def left(self):
        row = self.zeroPos[0]
        col = self.zeroPos[1]
        if row == 0:
            print("can't move up from here!")
            return False
        temp = self.state[row][col - 1]
        self.state[row][col - 1] = self.state[row][col]
        self.state[row][col] = temp
    def right(self):
        row = self.zeroPos[0]
        col = self.zeroPos[1]
        if row == 0:
            print("can't move up from here!")
            return False
        temp = self.state[row][col + 1]
        self.state[row][col + 1] = self.state[row][col]
        self.state[row][col] = temp


    # returns result of movement functions
    def geUp(self):
        pass
    def getDown(self):
        pass
    def getLeft(self):
        pass
    def getRight(self):
        pass