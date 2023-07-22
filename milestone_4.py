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
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
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

        # initialise as list of '_'s because no guesses yet.
        word_guessed = ['_'*len(self.word)]

        # initialise as unique letters in word because no guesses yet.
        num_letters = len(set(self.word))

        # make these three variables class attributes.
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        