from threading import Thread
from socket import socket
from bigboard import *
import pickle

board = BigBoard()
winner = 0
turn = 1
loading = True

HOST = '95.67.90.19'
PORT = 25566

def setup():
    global waiter, client
    size(405, 445)
    textAlign(CENTER, CENTER)
    textSize(30)
    client = socket()
    client.connect((HOST, PORT))
    waiter = Thread(target=wait, args=())
    waiter.start()
    
def draw():
    background(255)
    if loading:
        fill(0)
        text("Loading...", width/2, height/2)
    else:
        if not winner: 
            board.showActive()
        board.show()
        grid()
        bottom()
    
def mousePressed():
    global winner, turn
    if loading or turn != player: return
    i, j = mouseY, mouseX
    if i > 405: return
    i, j = i//45, j//45
    flag = board.play(i, j, turn)
    if flag: 
        client.send(pickle.dumps((i, j)))
        winner = board.winner()
        turn = 3 - turn
    
def grid():
    strokeWeight(3)
    line(135, 0, 135, 405)
    line(270, 0, 270, 405)
    line(0, 135, 405, 135)
    line(0, 270, 405, 270)
    strokeWeight(1)
    
def bottom():
    myFill(player, 153)
    ellipse(30, 425, 30, 30)
    myFill(turn)
    if winner:
        redraw()
        myFill(3-turn)
        if winner == 1:
            text("Red wins!", 202, 425)
        elif winner == 2:
            text("Blue wins!", 202, 425)
        elif winner == -1:
            fill(0)
            text("It's a tie!", 202, 425)
        noLoop()
    elif turn == 1:
        text("Red's turn", 202, 425)
    else:
        text("Blue's turn", 202, 425)

def wait():
    global player, loading, receiver
    player = int(client.recv(1024).decode())
    receiver = Thread(target=receive, args=())
    receiver.start()
    loading = False

def receive():
    global winner, turn
    while not winner:
        i, j = pickle.loads(client.recv(1024))
        board.play(i, j, turn)
        winner = board.winner()
        turn = 3 - turn
    client.close()
    