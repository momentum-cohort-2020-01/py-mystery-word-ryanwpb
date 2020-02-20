import random


class Game():
    def __init__(self):
        self.player = Player()

    def get_list(self):
        with open('words.txt', 'r') as f:
            data = f.read()
            word_list = data.splitlines()
            random_word = random.choice(word_list)
            word_length = len(random_word)
            new_list = ['_'] * word_length
            print(new_list)


class Player():
    def __init__(self):
        pass


Game().get_list()
