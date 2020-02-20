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
            letters = list(random_word.lower())
            print(letters)
        while self.playing:
            choice = input("Please guess a letter \n")
            choice.lower()
            if choice in letters:
                print(choice, "is correct!")
                print(letters)
            elif choice not in letters:
                print("Try again.")
                print(letters)
            if choice.isalpha():
                choice.lower()
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
