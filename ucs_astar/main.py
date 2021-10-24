from typing import get_origin
import node
import random

def getChildren(node):
    zeroPos = node.getZeroPos()
    row = zeroPos[0]
    col = zeroPos[1]
    children = []

    if row == 0:
        children.append(node.getDown())
    if row == 1:
        children.append(node.getDown())
        children.append(node.getUp())
    if row == 2:
        children.append(node.getUp())
    if col == 0:
        children.append(node.getRight())
    if col == 1:
        children.append(node.getRight())
        children.append(node.getLeft())
    if col == 2:
        children.append(node.getLeft())

    return children


def scramble(node, amt):
    for i in range(amt):
        move = random.randint(0, 3)
        if move == 0:
            try:
                node.up()
            except Exception:
                i -= 1
        if move == 1:
            try:
                node.down()
            except Exception:
                i -= 1
        if move == 2:
            try:
                node.left()
            except Exception:
                i -= 1
        if move == 3:
            try:
                node.right()
            except Exception:
                i -= 1


def main():
    goal = node.node([[1, 2, 3],[8, 0, 4],[7, 6, 5]], [])
    init = node.node([[1, 2, 3],[8, 0, 4],[7, 6, 5]], [])
    allNodes = [init]
    visited = []

    scramble(init, 5)
    init.printState()

    for current in allNodes:
        children = getChildren(current)
        for child in children:
            child.printState()





if __name__ == "__main__":
    main()