import node
import random

def getChildren(node):
    zeroPos = node.getZeroPos()
    row = zeroPos[0]
    col = zeroPos[1]

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
        getChildren(current)





if __name__ == "__main__":
    main()