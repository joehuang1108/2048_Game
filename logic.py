
# This is the file that contains all the logic in the game
# 4 x 4 grid with directions to move up, down, left, or right

import random

# Make a function that initializes a game/grid at the start
def start_game():
    # [0] [0] [0] [0]
    # [0] [0] [0] [0]
    # [0] [0] [0] [0]
    # [0] [0] [0] [0]
    mat = []
    for i in range(4):
        mat.append([0] * 4)

    add_new_2(mat)
    return mat

# choose a random row and column to add a 2
def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    # check empty before assigning
    print("about to add a 2")
    print("Testing this to be pushed")
    mat[r][c] = 2