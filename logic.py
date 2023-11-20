
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

    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    mat[r][c] = 2

def get_current_state(mat):
    # write a condition when it's won or not
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 2048):
                return 'WON'
            if (mat[i][j] == 0):
                return 'GAME NOT OVER'

    # no cell is empty,
    # BUT any moves in left, right, up, or down
    # cells will get merged and creates an empty cell and game is not over
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i][j + 1] or mat[i][j] == mat[i + 1][j]):
                return 'GAME NOT OVER'

    # checking last row
    for j in range(3):
        if(mat[3][j] == mat[3][j + 1]):
            return 'GAME NOT OVER'

    # checking last column
    for i in range(3):
        if (mat[i][3] == mat[i + 1][3]):
            return 'GAME NOT OVER'

    return 'LOST'





# function to compress the grid
# after every step before and after merging cells
def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)

    # loop to traverse through the rows
    # and move every cell as left as possible
    for i in range(4):
        pos = 0
        for j in range(4):
            if(mat[i][j] != 0):
                new_mat[i][pos] = mat[i][j]

                if(j != pos):
                    changed = True
                pos += 1

    return new_mat, changed

# function to merge the cells in matrix before compressing
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            # this checks if the elements are same and not zero
            if(mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
                changed = True

    return mat, changed

# function to reverse the matrix
def reverse(mat):
    # 2-D array
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        # 0 1 2 3
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

    # 0 0 0 0
    # 0 0 0 0
    # 0 0 0 0
    # 2 2 2 2

    # 0 0 0 2
    # 0 0 0 2
    # 0 0 0 2
    # 0 0 0 2

# function to update matrix if we move left
def move_left(mat):
    # first compress the mat
    new_mat, changed1 = compress(mat)
    # second merge the cells
    new_mat, changed2 = merge(new_mat)

    changed = changed1 or changed2
    # compress again after merging
    new_mat, temp = compress(new_mat)

    return new_mat, changed


# function to update matrix if we move right
def move_right(mat):
    # first reverse the matrix
    new_mat = reverse(mat)
    # second move left
    new_mat, changed = move_left(new_mat)
    # reverse again
    new_mat = reverse(new_mat)
    return new_mat, changed

    # 4 2 2 2 --> 0 4 2 4
    # 2 2 2 4
    # 4 2 4 0
    # 0 4 2 4

def move_up(mat):
    # first transpose the matrix
    new_mat = transpose(mat)
    # second move left
    new_mat, changed = move_left(new_mat)

    # transpose again to get result
    new_mat = transpose(mat)
    return new_mat, changed

