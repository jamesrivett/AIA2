import node



def main():
    goal = node.node([[1, 2, 3],[8, 0, 4],[7, 6, 5]], [])
    init = node.node([[1, 2, 3],[8, 0, 4],[7, 6, 5]], [])

    print(init.getState())
    init.right()
    print(init.getState())


def scramble(node):
    node.getState()



if __name__ == "__main__":
    main()