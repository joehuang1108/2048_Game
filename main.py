# 2048

import logic as l

if __name__ == '__main__':
    # this will start the game with the initial mat
    mat = l.start_game()
    for m in mat:
        print(m)

while(True):
    # ask for user input
    x = input("Press a command: ")

    if(x.upper() == 'W'):
        # call the move_up function
        mat, flag = l.move_up(mat)
        # get the current state
        status = l.get_current_state(mat)
        print(status)
        # check if game over
        if(status == 'GAME NOT OVER'):
            l.add_new_2(mat)
        else:
            break

    elif(x.upper() == 'S'):
        # call the move_down function
        mat, flag = l.move_down(mat)
        # get the current state
        status = l.get_current_state(mat)
        print(status)
        # check if game over
        if (status == 'GAME NOT OVER'):
            l.add_new_2(mat)
        else:
            break

    elif(x.upper() == 'A'):
        # call the move_left function
        mat, flag = l.move_left(mat)
        # get the current state
        status = l.get_current_state(mat)
        print(status)
        # check if game over
        if (status == 'GAME NOT OVER'):
            l.add_new_2(mat)
        else:
            break

    elif(x.upper() == 'D'):
        # call the move_right function
        mat, flag = l.move_right(mat)
        # get the current state
        status = l.get_current_state(mat)
        print(status)
        # check if game over
        if (status == 'GAME NOT OVER'):
            l.add_new_2(mat)
        else:
            break

    else:
        print("Invalid Key Pressed")

    for m in mat:
        print(m)

