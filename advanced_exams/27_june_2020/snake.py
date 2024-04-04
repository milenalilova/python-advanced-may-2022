def find_initial_state(matrix, size):
    coord_list = []
    start_row, start_col = None, None
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'S':
                start_row, start_col = i, j
            elif matrix[i][j] == 'B':
                coord_list.append([i, j])
    return start_row, start_col, coord_list


def find_next_position(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
matrix = [list(input()) for _ in range(size)]

food_eaten = 0
has_won = False
is_out = False

snake_row, snake_col, burrows_coordinates = find_initial_state(matrix, size)


while True:
    if food_eaten >= 10:
        has_won = True
        break

    command = input()
    matrix[snake_row][snake_col] = '.'
    next_row, next_col = find_next_position(command, snake_row, snake_col)
    if not is_inside(next_row, next_col, size):
        is_out = True
        break
    if matrix[next_row][next_col] == '*':
        food_eaten += 1
    elif [next_row, next_col] in burrows_coordinates:
        matrix[next_row][next_col] = '.'
        burrows_coordinates.remove([next_row, next_col])
        next_row, next_col = burrows_coordinates[0]
    elif matrix[next_row][next_col] == '-':
        pass
    snake_row, snake_col = next_row, next_col
    matrix[snake_row][snake_col] = 'S'

if has_won:
    print("You won! You fed the snake.")
if is_out:
    print("Game over!")
print(f"Food eaten: {food_eaten}")

for row in matrix:
    print(*row, sep='')
