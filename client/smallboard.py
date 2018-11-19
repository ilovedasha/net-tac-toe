
def check(total):
    for i in range(3):
        if total[i][0] == total[i][1] == total[i][2] != 0:
            return total[i][0]
        if total[0][i] == total[1][i] == total[2][i] != 0:
            return total[0][i]
    if total[0][0] == total[1][1] == total[2][2] != 0:
        return total[1][1]
    if total[2][0] == total[1][1] == total[0][2] != 0:
        return total[1][1]
    return 0

def myFill(clr, alfa=255):
    if clr == 0:
        noFill()
    elif clr == 1:
        fill(255, 0, 0, alfa)
    elif clr == 2:
        fill(0, 0, 255, alfa)

class SmallBoard(object):
    
    def __init__(self):
        self.clr = 0
        self.it = [[0, 0, 0], 
                   [0, 0, 0],
                   [0, 0, 0]]
        
    def __getitem__(self, index):
        return self.it[index]
    
    def __setitem__(self, index, value):
        self.it[index] = value
        
    def show(self, x, y):
        if self.clr > 0:
            myFill(self.clr, 100)
            rect(x, y, 135, 135)
        for row in self:
            for c in row:
                myFill(c)
                rect(x+5, y+5, 35, 35, 5)
                x += 45
            x -= 135
            y += 45
    
    def update(self):
        if self.clr: return self.clr
        self.clr = check(self)
        if not self.clr and not self.free(): self.clr = -1
        return self.clr
        
    def free(self):
        return [(i, j) for i in range(3) for j in range(3) if not self[i][j]]
    
    def play(self, i, j, clr):
        if self.clr or self[i][j]: 
            return False
        self[i][j] = clr
        self.update()
        return True