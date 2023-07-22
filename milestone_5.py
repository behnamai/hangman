import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(letter)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # read as input
        self.num_lives = num_lives
        self.word_list = word_list

        # initialise as empty because no guesses yet.
        self.list_of_guesses = list()

        # randomly select a word from word_list.
        word = random.choice(word_list)

        # initialise as list of ''s because no guesses yet.
        word_guessed = ['_'*len(word)]

        # initialise as unique letters in word because no guesses yet.
        num_letters = len(set(word))

        # make these three variables class attributes.
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives -= 1
            print(f'You have {num_lives} lives left.')
            
    
    def ask_for_input(self):
        while True:
            print('Please input a letter: ')
            guess = input()
            if not (guess.isalpha() and len(guess)) == 1:
                print(f'Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list=word_list, num_lives=num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)