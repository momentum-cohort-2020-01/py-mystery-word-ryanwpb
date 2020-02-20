import random

with open('words.txt', 'r') as f:
    data = f.read()


class Game():
    def __init__(self):
        self.player = Player()
        self.list = open("words.txt", "r")
        print(self.list.read())


class Player():
    def __init__(self):
        pass


Game()
