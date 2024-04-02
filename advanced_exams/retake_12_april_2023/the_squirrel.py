def find_initial_position(size, matrix):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 's':
                return i, j


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def find_next_position(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


def handle_next_position(row, col, matrix, value):
    condition = False
    if matrix[row][col] == 'h':
        value += 1
        matrix[row][col] = '*'
    elif matrix[row][col] == 't':
        condition = True
    return condition, value


size = int(input())
commands = input().split(', ')

field = [list(input()) for _ in range(size)]

squirrel_row, squirrel_col = find_initial_position(size, field)
field[squirrel_row][squirrel_col] = '*'

is_trapped = False
hazelnuts = 0

for command in commands:
    next_row, next_col = find_next_position(command, squirrel_row, squirrel_col)
    if not is_inside(next_row, next_col, size):
        print('The squirrel is out of the field.')
        break
    squirrel_row, squirrel_col = next_row, next_col
    is_trapped, hazelnuts = handle_next_position(squirrel_row, squirrel_col, field, hazelnuts)
    if is_trapped:
        print('Unfortunately, the squirrel stepped on a trap...')
        break
    if hazelnuts == 3:
        print('Good job! You have collected all hazelnuts!')
        break
else:
    print('There are more hazelnuts to collect.')
print(f'Hazelnuts collected: {hazelnuts}')
