
import random

word_list = ['python', 'hangman', 'challenge', 'function']
chosen_word = random.choice(word_list)

hidden_letters = []

for letter in chosen_word:
    hidden_letters.append('_')

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

while wrong_guesses < max_wrong_guesses and '_' in hidden_letters:
    guess = input('Guess a letter: ')

    if len(guess) != 1 or not ('a' <= guess <= 'z'):
        print("Enter one letter.")
        continue

    if guess in guessed_letters:
        print("Already guessed.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for position, letter_in_word in enumerate(chosen_word):
            if letter_in_word == guess:
                hidden_letters[position] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess:", wrong_guesses)

if '_' not in hidden_letters:
    print("You won!", chosen_word)
else:
    print("You lost!", chosen_word)