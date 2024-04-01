def get_initial_state(rows, cols, matrix):
    cheese = 0
    start_row = None
    start_col = None

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'M':
                start_row, start_col = i, j
            elif matrix[i][j] == 'C':
                cheese += 1
    return start_row, start_col, cheese


def find_next_position(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


def is_inside(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


rows, cols = [int(x) for x in input().split(',')]
cupboard = [list(input()) for _ in range(rows)]

mouse_row, mouse_col, cheese = get_initial_state(rows, cols, cupboard)
cupboard[mouse_row][mouse_col] = '*'

command = input()

while command != 'danger':
    next_row, next_col = find_next_position(command, mouse_row, mouse_col)
    if not is_inside(next_row, next_col, rows, cols):
        last_row, last_col = mouse_row, mouse_col
        cupboard[last_row][last_col] = 'M'
        print("No more cheese for tonight!")
        break

    if cupboard[next_row][next_col] == 'C':
        cheese -= 1
        mouse_row, mouse_col = next_row, next_col
        cupboard[mouse_row][mouse_col] = '*'
        if cheese == 0:
            cupboard[mouse_row][mouse_col] = 'M'
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif cupboard[next_row][next_col] == 'T':
        mouse_row, mouse_col = next_row, next_col
        cupboard[mouse_row][mouse_col] = 'M'
        print("Mouse is trapped!")
        break

    elif cupboard[next_row][next_col] == '*':
        mouse_row, mouse_col = next_row, next_col

    elif cupboard[next_row][next_col] == '@':
        pass

    command = input()

else:
    cupboard[mouse_row][mouse_col] = 'M'
    print("Mouse will come back later!")

for row in cupboard:
    print(*row, sep='')
