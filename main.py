import random

#globals
goal = [[1, 2, 3],[8, 0, 4],[7, 6, 5]]
init = []

def fillInit():
    init = [[for i in range(3)] random.() for j in range(3)]
#main
def main():
    fillInit()
    for i in init:
        print(i)

if __name__ == "__main__":
    main()