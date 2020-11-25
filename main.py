class Position:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def __repr__(self):
        return '[% s, % s]' % (self.X, self.Y)
    def __eq__(self, other):
        return ((self.X, self.Y) == (other.X, other.Y))

def move():
    plyrMove = input()
    if plyrMove == 'right' and 0 <= plyrPos.X <= rmSize - 2:
        plyrPos.X += 1
    elif plyrMove == 'left' and 1 <= plyrPos.X <= rmSize - 1:
        plyrPos.X -= 1
    elif plyrMove == 'down' and 0 <= plyrPos.Y <= rmSize - 2:
        plyrPos.Y += 1
    elif plyrMove == 'up' and 1 <= plyrPos.Y <= rmSize - 1:
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
                print(' # ||', end='')
            else:
                print('   ||', end='')
            rmPos.X += 1
        print('')
        for x in range(rmSize):
            print('=====', end='')
        print('==')
        rmPos.X = 0
        rmPos.Y += 1

plyrPos = Position(1, 1)
rmSize = 4

while True:
    rmDraw()
    move()
