import copy
from main import *

class node:
    # class vars
    state = []
    parent = []
    children = []
    lastMove = ""
    pathTo = []

    def __init__(self, state, path):
        self.state = state
        self.children = self.findChildren()
        
        # append only self state if path is empty, path and self state if not
        if path == "":
            self.pathTo.append(state)
        else:
            self.pathTo.append(path)
            self.pathTo.append(state)

        if path != "":
            # find last move
            zeroOfSelf = findZero(self.state)
            zeroOfLast = findZero(self.pathTo[-1])
            diff = [zeroOfSelf[0] - zeroOfLast[0], zeroOfSelf[1] - zeroOfLast[1]]

            if diff == [1, 0]:
                self.lastMove = "down"
            if diff == [-1, 0]:
                self.lastMove = "up"
            if diff == [0, 1]:
                self.lastMove = "right"
            if diff == [0, -1]:
                self.lastMove = "left"



    def getPathTo(self):
        return self.pathTo

    # calculates poss moves and costs, DOES NOT RETURN sellf.children
    def findChildren(self):
        moves = possMoves(self.lastMove, self.state)
        kids = []

        # makes move, stores as child, then reverts
        for move in moves:
            if move == "up":
                up(self.state)
                temp = copy.deepcopy(self.state)
                kids.append([temp, totalDistance(self.state)])
                down(self.state)
            if move == "down":
                down(self.state)
                temp = copy.deepcopy(self.state)
                kids.append([temp, totalDistance(self.state)])
                up(self.state)
            if move == "left":
                left(self.state)
                temp = copy.deepcopy(self.state)
                kids.append([temp, totalDistance(self.state)])
                right(self.state)
            if move == "right":
                right(self.state)
                temp = copy.deepcopy(self.state)
                kids.append([temp, totalDistance(self.state)])
                left(self.state)

        return kids

    def findLowestChild(self):
        lowest = [[], 100000]

        for child in self.children:
            if child[1] < lowest[1]:
                lowest = child

        return lowest


    # RETURNS LIST OF CHILDREN
    def getChildren(self):
        return self.children