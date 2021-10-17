from main import *

class node:
    # class vars
    state = []
    parent = []
    children = []
    lastMove = ""

    def __init__(self, state, last):
        self.state = state
        self.children = self.findChildren()
        self.lastMove = last

    # calculates poss moves and costs, DOES NOT RETURN LIST OF CHILDREN
    def findChildren(self):
        moves = possMoves(self.lastMove, self.state)

        # makes move, stores as child, then reverts
        for move in moves:
            kids = []
            if move == "up":
                up(self.state)
                kids.append([self.state, totalDistance(self.state)])
                down(self.state)
            if move == "down":
                down(self.state)
                kids.append([self.state, totalDistance(self.state)])
                up(self.state)
            if move == "left":
                left(self.state)
                kids.append([self.state, totalDistance(self.state)])
                right(self.state)
            if move == "right":
                right(self.state)
                kids.append([self.state, totalDistance(self.state)])
                left(self.state)

        return kids

    # RETURNS LIST OF CHILDREN
    def getChildren(self):
        return self.children