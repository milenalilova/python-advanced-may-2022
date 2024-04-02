from math import floor


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


def adjust_position(row, col, size):
    if row < 0:
        row = size - 1
    if row >= size:
        row = 0
    if col < 0:
        col = size - 1
    if col >= size:
        col = 0
    return row, col


size = int(input())
matrix = [list(input().split()) for _ in range(size)]
current_row, current_col = find_initial_position(matrix, size)
commands_list = ["up", "down", "left", "right"]
path_coordinates = [[current_row, current_col]]
coins = 0

while True:
    command = input()
    if command not in commands_list:
        continue
    next_row, next_col = find_next_position(command, current_row, current_col)

    if not is_inside(next_row, next_col, size):
        next_row, next_col = adjust_position(next_row, next_col, size)

    current_row, current_col = next_row, next_col

    if matrix[current_row][current_col] == 'X':
        path_coordinates.append([current_row, current_col])
        coins = floor(coins * 0.5)
        print(f"Game over! You've collected {coins} coins.")
        break

    elif matrix[current_row][current_col].isdigit():
        if [current_row, current_col] not in path_coordinates:
            coins += int(matrix[current_row][current_col])
    path_coordinates.append([current_row, current_col])

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print("Your path:")
for coord in path_coordinates:
    print(coord)
