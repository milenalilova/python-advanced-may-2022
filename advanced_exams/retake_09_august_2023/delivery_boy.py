def get_initial_position(rows, cols, matrix):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'B':
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


def is_inside(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


rows, cols = [int(x) for x in input().split()]
neighborhood = [list(input()) for _ in range(rows)]

initial_row, initial_col = get_initial_position(rows, cols, neighborhood)
boy_row, boy_col = get_initial_position(rows, cols, neighborhood)

while True:
    command = input()

    next_row, next_col = find_next_position(command, boy_row, boy_col)

    if not is_inside(next_row, next_col, rows, cols):
        neighborhood[initial_row][initial_col] = ' '
        print("The delivery is late. Order is canceled.")
        break

    if neighborhood[next_row][next_col] == '*':
        continue

    if neighborhood[next_row][next_col] == 'A':
        neighborhood[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        neighborhood[boy_row][boy_col] = 'P'
        neighborhood[initial_row][initial_col] = 'B'
        print("Pizza is delivered on time! Next order...")
        break

    if neighborhood[next_row][next_col] == 'P':
        neighborhood[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        neighborhood[next_row][next_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
        continue

    if not neighborhood[boy_row][boy_col] == 'R':
        neighborhood[boy_row][boy_col] = '.'
    boy_row, boy_col = next_row, next_col
    neighborhood[boy_row][boy_col] = '.'

for row in neighborhood:
    print(*row, sep='')
