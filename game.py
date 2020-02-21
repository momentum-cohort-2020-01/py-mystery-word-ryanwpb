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
            print(new_list)
            choice = input("Please guess a letter \n")
            choice.lower()
            if choice.isalpha() and len(choice) == 1:
                if choice == int:
                    print("You must enter a letter a-z!")
                if choice in new_list:
                    print("Already guessed that letter.")
                elif choice in letters:
                    print("Correct there is", len(choice), choice)
                    index_position_list = self.get_index_pos(
                        letters, choice)  # This is a list
                    # print (len(index_position_list)) #Provides length of one if there's only one instance of it.
                    choice_list = len(index_position_list)*[choice, ]
                    # print(choice_list)
                    for (index, choice) in zip(index_position_list, choice_list):
                        new_list[index] = choice
                    # print(new_list)
                elif choice not in letters:
                    print("Try again.")
                    self.player.guesses_remaining -= 1
                    print("You have", self.player.guesses_remaining,
                          "Guesses Remaining")
                if self.player.guesses_remaining == 0:
                    print("Word Fuckery has Defeated YOU!!! \n")
                    restart = input("Care to play again? (y) or (n)")
                    if restart == "n":
                        self.playing = False
                    elif restart == "y":
                        self.start_game()

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
        self.guesses_remaining = 8


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
