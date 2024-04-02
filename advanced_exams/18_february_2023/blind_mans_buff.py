def find_initial_position(rows, cols, matrix):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'B':
                return i, j


def is_inside(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def find_next_position(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


rows, cols = [int(x) for x in input().split()]

playground = [list(input().split()) for _ in range(rows)]
player_row, player_col = find_initial_position(rows, cols, playground)
playground[player_row][player_col] = '-'

touched_opponents = 0
moves = 0

while True:
    command = input()
    if command == 'Finish':
        break

    next_row, next_col = find_next_position(command, player_row, player_col)
    if not is_inside(next_row, next_col, rows, cols):
        continue
    if playground[next_row][next_col] == 'O':
        continue
    elif playground[next_row][next_col] == 'P':
        player_row, player_col = next_row, next_col
        moves += 1
        playground[player_row][player_col] = '-'
        touched_opponents += 1
        if touched_opponents == 3:
            break
    elif playground[next_row][next_col] == '-':
        player_row, player_col = next_row, next_col
        moves += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")
