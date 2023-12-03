# A guess the number game.

import random

# ask user for range
rangeUpper = int(input("You want to guess a number from 1 to: "))

# seed random number
secretNumber = random.randint(1, rangeUpper)

# ask user for how many guesses are allowed
guessesTotal = int(input("How many guesses do you want? "))

print(f"I am thinking of a number between 1 and {rangeUpper}.")
# Ask the player to guess guessesTotal times.
for guessesTaken in range(1, guessesTotal + 1):
    guess = int(input('Take a guess. '))

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break   # this condition is the correct guess.

if guess == secretNumber:
    print(f'Good job! You guessed my number in {guessesTaken} guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
