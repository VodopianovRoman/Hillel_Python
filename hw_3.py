# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from the console,
# the computer makes a decision randomly.

# import random
#
# lis_options = ['rock', 'scissors', 'paper']
#
# def game():
#     """Create a function for playing 'rock, scissors, paper'.
#     A string should come to the function."""
#     player = input('Enter one of the options: rock, scissors, paper.')
#     enemy_program = random.choice(lis_options)
#     if player == 'rock' and enemy_program == 'scissors':
#         print('You are a winner in life!')
#     elif player == 'scissors' and enemy_program == 'paper':
#         print('You are a winner in life!')
#     elif player == 'paper' and enemy_program == 'rock':
#         print('You are a winner in life!')
#     else:
#         print('Buddy, try again!')
#
# game()

# 2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days
# at any given time.
# Do you have enough toilet paper(TP) to make it through?
# Although the number of squares per roll of TP varies significantly, we'll assume
# each roll has 500 sheets,
# and the average person uses 57 sheets per day.

# Create a function that will receive a dictionary with two key/values:
# "people" ⁠— Number of people in the household.
# "tp" ⁠— Number of rolls.
# Return a statement telling the user if they need to buy more TP!

# def stock_tp(**kwargs):
#     # print(kwargs)
#     for i in kwargs:
#         # print(i, kwargs[i])
#         if i == 'people':
#             one_day_need = kwargs[i] * 57
#         else:
#             all_tips = kwargs[i] * 500
#     stock = all_tips / one_day_need
#     if stock >= 14:
#         print('Congratulations, you will survive the quarantine and be clean!')
#     else:
#         print('Buddy, you need to buy more goods, otherwise you will be dirty :-(')
#
#
# stock_tp(people = int(input('Enter the number of people who will live:')), tp = int(input('Enter the number of rolls of TP you have:')))


# 3) Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Example:
# encrypt("banana") ➞ "0n0n0b"
# encrypt("karaca") ➞ "0c0r0k"
# encrypt("burak") ➞ "k0r3b"
# encrypt("alpaca") ➞ "0c0pl0"



# **4)Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns
# whether the game is a win
# for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix,
# and "E" represents an empty spot.
# Example:
# tic_tac_toe([
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]) ➞ "X"
#
# tic_tac_toe([
#     ["O", "O", "O"],
#     ["O", "X", "X"],
#     ["E", "X", "X"]
# ]) ➞ "O"
#
# tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ]) ➞ "Draw"

