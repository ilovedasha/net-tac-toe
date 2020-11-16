#!/usr/bin/python3
from socket import socket
from threading import Thread
from time import sleep
import sys

def message(conn1, conn2):
    try:
        while True:
            move = conn1.recv(1024)
            conn2.send(move)
            sleep(0.2)
    except:
        conn1.close()


if __name__ == '__main__':

    HOST = '0.0.0.0' if len(sys.argv) < 2 else sys.argv[1]
    PORT = 31001     if len(sys.argv) < 3 else int(sys.argv[2])

    server = socket()
    server.bind((HOST, PORT))
    server.listen(2)

    print(f"Serving on {HOST}:{PORT}")
    pool = {}

    while True:
        player1, addr1 = server.accept()
        player1.settimeout(600)
        print('Connection from:', str(addr1))
        secret = player1.recv(1024).decode()
        print('Secret:', secret)
        if len(secret) != 16:
            print('Invalid secret format')
            continue
        if secret in pool:
            print("Found a match")
            player2 = pool.pop(secret)
            player1.send('1'.encode())
            player2.send('2'.encode())
            t1 = Thread(target=message, args=(player1, player2))
            t2 = Thread(target=message, args=(player2, player1))
            t1.start()
            t2.start()
        else:
            print("Added to the pool")
            pool[secret] = player1
        sleep(0.2)


