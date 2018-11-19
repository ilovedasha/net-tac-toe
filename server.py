from socket import socket
from threading import Thread
import pickle

HOST = '192.168.1.90'
PORT = 25566

server = socket()
server.bind((HOST, PORT))
server.listen(2)

player1, addr1 = server.accept()
print('Connection from:', str(addr1))

player2, addr2 = server.accept()
print('Connection from:', str(addr2))

player1.send('1'.encode())
player2.send('2'.encode())

def message(conn1, conn2):
    try:
        while True:
            move = conn1.recv(1024)
            conn2.send(move)
    except:
        conn1.close()

t1 = Thread(target=message, args=(player1, player2))
t2 = Thread(target=message, args=(player2, player1))

t1.start()
t2.start()
