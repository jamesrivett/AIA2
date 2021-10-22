class node:
    state = []
    cost = 0
    pathTo = []

    def __init__(self, state, path):
        self.state = state
        pathTo = path
        pathTo.append(self)
    
    def getState(self):
        return self.state

    def getCost(self):
        return self.cost

    def getPathTo(self):
        return self.pathTo