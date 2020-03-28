# vim: ft=python
from game import Game
from smallboard import myFill

game = Game()

def setup():
    size(405, 445)
    textAlign(CENTER, CENTER)
    textSize(30)
    
def draw():
    background(255)
    if game.loading:
        fill(0)
        text("Waiting...", width/2, height/2)
        if frameCount > 1:
            game.connect()
    else:
        if not game.winner: 
            game.board.showActive()
        game.board.show()
        grid()
        bottom()
    
def mousePressed():
    if game.loading or game.turn != game.player: 
        return
    i, j = mouseY, mouseX
    if i > 405: return
    i, j = i//45, j//45
    game.play(i, j)
    
def grid():
    strokeWeight(3)
    line(135, 0, 135, 405)
    line(270, 0, 270, 405)
    line(0, 135, 405, 135)
    line(0, 270, 405, 270)
    strokeWeight(1)
    
def bottom():
    myFill(game.player, 153)
    ellipse(30, 425, 30, 30)
    myFill(game.turn)
    if game.winner:
        redraw()
        myFill(3-game.turn)
        if game.winner == 1:
            text("Red wins!", 202, 425)
        elif game.winner == 2:
            text("Blue wins!", 202, 425)
        elif game.winner == -1:
            fill(0)
            text("It's a tie!", 202, 425)
        noLoop()
    elif game.turn == 1:
        text("Red's turn", 202, 425)
    else:
        text("Blue's turn", 202, 425)

