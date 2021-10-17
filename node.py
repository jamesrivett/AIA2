from main import *

class node:
    # class vars
    state = []
    parent = []
    children = []

    def __init__(self, state, last):
        self.state = state
        self.findChildren()

    def findChildren(self):
        moves = possMoves("left", self.state)

        # makes move, stores as child, then reverts
        for move in moves:
            if move == "up":
                up(self.state)
                self.children.append([self.state, totalDistance(self.state)])
                down(self.state)
            if move == "down":
                down(self.state)
                self.children.append([self.state, totalDistance(self.state)])
                up(self.state)
            if move == "left":
                left(self.state)
                self.children.append([self.state, totalDistance(self.state)])
                right(self.state)
            if move == "right":
                right(self.state)
                self.children.append([self.state, totalDistance(self.state)])
                left(self.state)

