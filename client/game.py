import pickle
from bigboard import *
from os import environ
from random import choice
from string import ascii_letters as letters
from socket import socket
from threading import Thread

class Game(object):

    def __init__(self):
        self.board = BigBoard()
        self.winner = 0
        self.turn = 1
        self.loading = True
        self.host = environ['HOST']
        self.port = int(environ['PORT'])

    def connect(self):
        secret = Game.getSecret()
        print("Your secret is: " + secret)
        self.client = socket()
        self.client.connect((self.host, self.port))
        self.client.send(secret.encode())
        self.player = int(self.client.recv(1024).decode())
        self.receiver = Thread(target=self.receive, args=())
        self.receiver.start()
        self.loading = False

    def receive(self):
        try:
            while not self.winner:
                i, j = pickle.loads(self.client.recv(1024))
                self.board.play(i, j, self.turn)
                self.winner = self.board.winner()
                self.turn = 3 - self.turn
        finally:
            self.client.close()

    @staticmethod
    def getSecret(secretLen=16):
        secret = environ.get("SECRET", None)
        if secret is None:
            secret = ''.join(choice(letters) for _ in range(secretLen))
        else:
            error = "Secret has to be exactly " + str(secretLen) + " symbols!"
            assert len(secret) == secretLen, error
        return secret

    def play(self, i, j):
        if self.board.play(i, j, self.turn):
            self.client.send(pickle.dumps((i, j)))
            self.winnder = self.board.winner()
            self.turn = 3 - self.turn

