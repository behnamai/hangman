import random
import string

word_list = ['apple', 'pear', 'orange', 'banana', 'melon']

print(word_list)

word = random.choice(word_list)

print(word)

input_accepted = False
while not input_accepted:
    print('Please input a letter: ')
    guess = input()
    if guess in string.ascii_letters and len(guess) == 1:
        print(f'Good guess! You guessed {guess}.')
        input_accepted = True
    else:
        print(f'Oops! That is not a valid input. You guessed {guess}.')