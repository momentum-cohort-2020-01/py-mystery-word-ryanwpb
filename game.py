import random


class Game():
    def __init__(self):
        self.player = Player()
        self.playing = True
        self.start_game()

    def start_game(self):

        with open('words.txt', 'r') as f:
            data = f.read()
            word_list = data.splitlines()
            random_word = random.choice(word_list)
            word_length = len(random_word)
            new_list = ['_'] * word_length
            letters = list(random_word)
            print(new_list)
        while self.playing:
            choice = input("Please guess a letter \n")
            print(new_list)
            if choice.isalpha():
                choice.lower()
                break
            else:
                print("Use letters a-z only")


class Player():
    def __init__(self):
        pass


Game()


#    def get_list(self):
#         with open('words.txt', 'r') as f:
#             data = f.read()
#             word_list = data.splitlines()
#             random_word = random.choice(word_list)
#             word_length = len(random_word)
#             new_list = ['_'] * word_length
#             letters = list(random_word)
#             return letters
