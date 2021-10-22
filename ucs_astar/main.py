import node



def main():
    goal = node.node([[1, 2, 3],[8, 0, 4],[7, 6, 5]], [])
    init = node.node([[1, 2, 3],[8, 0, 4],[7, 6, 5]], [])

    n0 = init.getUp()
    n1 = n0.getRight()
    n2 = n1.getDown()
    print(init.calcTotalCost())


def scramble(node):
    node.getState()



if __name__ == "__main__":
    main()