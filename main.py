import random

#globals
goal = [[1, 2, 3],[8, 0, 4],[7, 6, 5]]
init = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

def fillInit():
    used = []
    for i in range(3):
        for j in range(3):
            while True:
                cont = False
                num = random.randint(0, 8)
                print(used)
                print(num)

                for element in used:
                    if element == num:
                        cont = True
                        break
                if cont == True: continue

                init[i][j] = num
                used.append(num)
                break

#main
def main():
    fillInit()
    for i in init:
        print(i)

if __name__ == "__main__":
    main()