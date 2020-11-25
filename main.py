# for clear function
from os import system, name

import pprint

# used to represent coordinates, i.e. entity position, room location. due to how draw function works, (0,0) is the top left corner of a grid, with right being +x and down being +y
class Position:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def __repr__(self):
        return '[% s, % s]' % (self.X, self.Y)
    def __eq__(self, other):
        return ((self.X, self.Y) == (other.X, other.Y))


# clears console 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def move():
    plyrMove = input()
    if plyrMove == 'right' and 0 <= plyrPos.X <= rmSize - 2 and wallV[plyrPos.Y][plyrPos.X] == 0:
        plyrPos.X += 1
    elif plyrMove == 'left' and 1 <= plyrPos.X <= rmSize - 1 and wallV[plyrPos.Y][plyrPos.X - 1] == 0:
        plyrPos.X -= 1
    elif plyrMove == 'down' and 0 <= plyrPos.Y <= rmSize - 2 and wallH[plyrPos.Y][plyrPos.X] == 0:
        plyrPos.Y += 1
    elif plyrMove == 'up' and 1 <= plyrPos.Y <= rmSize - 1 and wallH[plyrPos.Y - 1][plyrPos.X] == 0:
        plyrPos.Y -= 1

def rmDraw():
    rmPos = Position(0, 0)
    for x in range(rmSize):
        print('=====', end='')
    print('==')
    for x in range(rmSize):
        print('||', end='')
        for x in range(rmSize):
            if rmPos == plyrPos:
                print(' # ', end='')
            else:
                print('   ', end='')
            if rmPos.X < rmSize - 1:
                if wallV[rmPos.Y][rmPos.X] == 0:
                    print('  ', end='')
                else:
                    print('||', end='')
            rmPos.X += 1
        print('||\n==', end='')
        wallHcheck = 0
        for x in range(rmSize):
            if rmPos.Y < rmSize - 1:
                if wallH[rmPos.Y][wallHcheck] == 0:
                    print('   ', end='')
                else:
                    print('===', end='')
                wallHcheck += 1
            else:
                print('===', end='')
            print('==', end='')
        print('')
        rmPos.X = 0
        rmPos.Y += 1

plyrPos = Position(0, 0)
rmSize = 5

wallH = [[0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0],]
wallV = [[1, 0, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]

def game():
    while True:
        rmDraw()
        move()
        clear()

game()
