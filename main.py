# 2048

import logic


mat = logic.start_game()
for x in mat:
    print(x)

print("")

mat2, temp = logic.move_left(mat)
logic.add_new_2(mat2)
logic.add_new_2(mat2)
logic.add_new_2(mat2)
mat2, temp = logic.move_left(mat2)
mat2, temp = logic.move_right(mat2)
for x in mat2:
    print(x)
