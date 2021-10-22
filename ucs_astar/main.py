import node

def getChildren(node):
    zeroPos = node.getZeroPos()
    row = zeroPos[0]
    col = zeroPos[1]




def main():
    goal = node.node([[1, 2, 3],[8, 0, 4],[7, 6, 5]], [])
    init = node.node([[1, 2, 3],[8, 0, 4],[7, 6, 5]], [])
    allNodes = [init]
    visited = []

    for current in allNodes:
        getChildren(current)





if __name__ == "__main__":
    main()