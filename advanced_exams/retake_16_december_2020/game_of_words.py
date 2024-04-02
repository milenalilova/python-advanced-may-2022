def find_initial_position(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'P':
                return i, j


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


line = input()
size = int(input())
matrix = [list(input()) for _ in range(size)]
n = int(input())

current_row, current_col = find_initial_position(matrix, size)
matrix[current_row][current_col] = '-'

for _ in range(n):
    command = input()
    next_row, next_col = find_next_position(command, current_row, current_col)
    if not is_inside(next_row, next_col, size):
        line = line[:-1]
        continue
    current_row, current_col = next_row, next_col

    if matrix[current_row][current_col] == '-':
        pass
    else:
        line += matrix[current_row][current_col]
        matrix[current_row][current_col] = '-'

matrix[current_row][current_col] = 'P'

print(line)
for row in matrix:
    print(''.join(row))
