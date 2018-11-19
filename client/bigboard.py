from smallboard import *

class BigBoard(object):
    
    def __init__(self):
        self.it = [[SmallBoard() for j in range(3)] for i in range(3)]
        self.active = (-1, -1)
    
    def __getitem__(self, index):
        return self.it[index]
    
    def __setitem__(self, index, value):
        self.it[index] = value
    
    def show(self):
        x, y = 0, 0
        for row in self:
            for board in row:
                board.show(x, y)
                x += 135
            x = 0
            y += 135
            
    def makeActive(self, i, j):
        if self[i][j].clr:
            self.active = (-1, -1)
        else:
            self.active = (i, j)
            
    def showActive(self):
        fill(255, 255, 0, 75)
        if self.active == (-1, -1):
            rect(0, 0, 405, 405)
        else:
            i, j = self.active
            rect(j*135, i*135, 135, 135)
            
    def play(self, i, j, clr):
        flag = None
        if self.active == (-1, -1) or (i//3, j//3) == self.active:
            flag = self[i//3][j//3].play(i%3, j%3, clr)
        if flag:
            self.makeActive(i%3, j%3)
        return flag
    
    def winner(self):
        tie = all(self[i][j].clr for i in range(3) for j in range(3))
        win = check([[self[i][j].clr for j in range(3)] for i in range(3)])
        return win if win else (-1 if tie else 0)