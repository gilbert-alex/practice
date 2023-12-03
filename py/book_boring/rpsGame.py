# A rock, paper, scissors game.
# Practice with functions and global variables

import random, sys

# Counters
wins = 0
losses = 0
ties = 0
counter_moves = 0
counter_games = 0

def rps():
    print("Rock, Paper, Scissors.")
    a = ''
    while a != 'q':
        displayStats()
        a = playerChoice(counter_moves)
        b = computerChoice(counter_moves)
        result(a, b)
        check()

# prints cumulative results of games
def displayStats():
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

# asks user for move
def playerChoice(counter_moves):
    while True:
        playerMove = input('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit. ')
        playerMove = playerMove.lower()
        if playerMove == 'q':
            sys.exit()
        elif playerMove in ['r', 'p', 's']:
            break
        else:
            print("Type r, p, s, or q.")
    displayMove(counter_moves, playerMove)
    return playerMove

# determines computer's move
def computerChoice(counter_moves):
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerChoice = 'r'
    if randomNumber == 2:
        computerChoice = 'p'
    if randomNumber == 3:
        computerChoice = 's'
    displayMove(counter_moves, computerChoice)
    return computerChoice

# determines winner of each game
def result(a, b):
    global wins, losses, ties, counter_games
    if a == b:
        print("It's a tie!")
        ties += 1
    elif (a == 'r' and b == 's') or (a == 'p' and b == 'r') or (a == 's' and b == 'p'):
        print("User wins!")
        wins += 1   
    else:
        print("Computer wins!")
        losses += 1
    counter_games += 1

# Informative text for GUI
def displayMove(x, a):
    global counter_moves
    if x % 2 == 0: # player move
        if a == 'r':
            print(f"ROCK versus...", end = ' ')
        elif a == 'p':
            print(f"PAPER versus...", end = ' ')
        elif a == 's':
            print(f"SCISSORS versus...", end = ' ')
    else:   # computer move
        if a == 'r':
            print("ROCK.")
        elif a == 'p':
            print("PAPER.")
        elif a == 's':
            print("SCISSORS.")
    counter_moves += 1

# check to make sure stats are incrementing correctly
def check():
    global counter_games, wins, losses, ties
    if counter_games != wins + losses + ties:
        print("Error in counter. Exiting.")
        sys.exit()

rps()