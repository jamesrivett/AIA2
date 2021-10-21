import copy
from main import *

class node:
    # class vars
    state = []
    parent = []
    children = []
    lastMove = ""
    pathTo = []

    def __init__(self, state, last, path):
        self.state = state
        self.children = self.findChildren()
        self.lastMove = last
        if last == "":
            self.pathTo.append(state)
        else:
            self.pathTo.append(path)

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