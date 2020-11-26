# for clear function
from os import system, name

#helpful when printing large matrices
import pprint

#to help with maze generation - currently not used
import random

# used to represent coordinates, i.e. entity position, room location. due to how draw function works, (0,0) is the top left corner of a grid, with right being +x and down being +y
class Position:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def __repr__(self):
        return '[% s, % s]' % (self.X, self.Y)
    #give True when two points are same
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

#set of commands to make entering commands easier - needs improvement
right = 'right', 'd'
left = 'left', 'a'
up = 'up', 'w'
down = 'down', 's'

#two matrices that record whether the player has encountered a wall
wallVseen = []
wallHseen = []

#initializes inner wall matrices based on room settings - need to incorporate with wallV and wallH
def wallInit():
    for x in range(rmSize - 1):
        wallHseen.append([])
    for row in wallHseen:
        for x in range(rmSize):
            row.append(0)

    for x in range(rmSize):
        wallVseen.append([])
    for row in wallVseen:
        for x in range(rmSize - 1):
            row.append(1) 

#marks walls surrounding player as seen if not done so already
def wallSeen():
    if 0 <= plyrPos.X <= rmSize - 2 and wallVseen[plyrPos.Y][plyrPos.X] == 0:
        wallVseen[plyrPos.Y][plyrPos.X] = 1
    if 1 <= plyrPos.X <= rmSize - 1 and wallVseen[plyrPos.Y][plyrPos.X - 1] == 0:
        wallVseen[plyrPos.Y][plyrPos.X - 1] = 1
    if 0 <= plyrPos.Y <= rmSize - 2 and wallHseen[plyrPos.Y][plyrPos.X] == 0:
        wallHseen[plyrPos.Y][plyrPos.X] = 1
    if 1 <= plyrPos.Y <= rmSize - 1 and wallHseen[plyrPos.Y - 1][plyrPos.X] == 0:
        wallHseen[plyrPos.Y - 1][plyrPos.X] = 1 

#moves player in desired direction if possible, i.e. if within game bounds, no wall
def move():
    plyrMove = input().lower()

    #move is only carried out if 1. the command specifies a direction, 2. if the move is within the bounds (does not exceed room size limit), and 3. if there is no inner wall blocking the movement
    if plyrMove in right and 0 <= plyrPos.X <= rmSize - 2 and wallV[plyrPos.Y][plyrPos.X] == 0:
        plyrPos.X += 1
    elif plyrMove in left and 1 <= plyrPos.X <= rmSize - 1 and wallV[plyrPos.Y][plyrPos.X - 1] == 0:
        plyrPos.X -= 1
    elif plyrMove in down and 0 <= plyrPos.Y <= rmSize - 2 and wallH[plyrPos.Y][plyrPos.X] == 0:
        plyrPos.Y += 1
    elif plyrMove in up and 1 <= plyrPos.Y <= rmSize - 1 and wallH[plyrPos.Y - 1][plyrPos.X] == 0:
        plyrPos.Y -= 1
    

#draws map on screen
def rmDraw():
    #checks if move has made any walls visible
    wallSeen()
    
    #rooms are drawn via the coordinate system
    rmPos = Position(0, 0)
    
    #prints top line of map
    for x in range(rmSize):
        print('=====', end='')
    print('==')
    
    #prints vertical inner walls
    for x in range(rmSize):
        print('||', end='')
        for x in range(rmSize):
            #prints player icon if player in cell, otherwise leaves blank space - can potentially be copied/turned into function for other entities
            if rmPos == plyrPos:
                print(' # ', end='')
            else:
                print('   ', end='')
            
            #prints inner wall based on presence and whether player has seen wall
            if rmPos.X < rmSize - 1:
                if wallVseen[rmPos.Y][rmPos.X] == 0:
                    print('!!', end='')
                elif wallV[rmPos.Y][rmPos.X] == 0:
                    print('  ', end='')
                else:
                    print('||', end='')
            
            #moves to next cell
            rmPos.X += 1
        
        #shifts from vertical to horizontal
        print('||')
        if rmPos.Y != rmSize - 1:
            print('==', end='')
        rmPos.X = 0
        
        #prints horizontal inner walls
        for x in range(rmSize):
            #prints inner wall based on presence and whether player has seen wall
            if rmPos.Y < rmSize - 1:
                if wallHseen[rmPos.Y][rmPos.X] == 0:
                    print('---', end='')
                elif wallH[rmPos.Y][rmPos.X] == 0:
                    print('   ', end='')
                else:
                    print('===', end='')
                #prints inner corner based on whether surrounding horizontal walls have been seen - just for aesthetics
                if rmPos.X < rmSize - 1:
                    if wallHseen[rmPos.Y][rmPos.X] == 0 and wallHseen[rmPos.Y][rmPos.X + 1] == 0:
                        print('--', end='')
                    else:
                        print('==', end='')
            
            #moves to next cell
            rmPos.X += 1
        
        #ends horizontal section, moves to next line
        print('==', end='')
        if rmPos.Y != rmSize - 1:
            print('')
        rmPos.X = 0
        rmPos.Y += 1

    #prints bottom line of map
    for x in range(rmSize):
        print('=====', end='')
    print('')

#maze exploration loop - clears screen, draws map, and prompts player for move
def maze():
    #need to base on condition!!!
    while True:
        clear()
        rmDraw()
        move()

#initial player and room conditions - will vary in full game
plyrPos = Position(0, 0)
rmSize = 5

#two matrices that record the presence of vertical and horizontal inner walls - will vary in full game, need to connect to wallInit
wallV = [[1, 0, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
wallH = [[0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0],]

wallInit()
maze()
