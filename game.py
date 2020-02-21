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
        while self.playing:
            print(letters)
            choice = input("Please guess a letter \n")
            choice.lower()
            if choice in letters:
                print(choice, "is correct!")
                index_pos_list = self.get_index_pos(letters, choice)
                print(letters)
                print(index_pos_list)
            elif choice not in letters:
                print("Try again.")
                print(letters)
            if choice.isalpha():
                choice.lower()
            else:
                print("Use letters a-z only")

    def get_index_pos(self, letters, choice):
        index_pos_list = []
        index_pos = 0
        while True:
            try:
                index_pos = letters.index(choice, index_pos)
                index_pos_list.append(index_pos)
                index_pos += 1
            except:
                break
            return index_pos_list


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
