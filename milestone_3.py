import random

word_list = ['apple', 'pear', 'orange', 'banana', 'melon']
word = random.choice(word_list)
print(word)

def check_guess(guess):
    ''' Checks whether the guess is in the random word. '''
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    ''' Asks for user input and validates it. '''
    while True:
        print('Please input a letter: ')
        guess = input()
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print(f'Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()