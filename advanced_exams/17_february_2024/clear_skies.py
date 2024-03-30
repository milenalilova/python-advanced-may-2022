def get_next_position(row, col, command):
    next_row = 0
    next_col = 0

    if command == 'up':
        next_row, next_col = row - 1, col

    elif command == 'down':
        next_row, next_col = row + 1, col

    elif command == 'left':
        next_row, next_col = row, col - 1

    elif command == 'right':
        next_row, next_col = row, col + 1

    return next_row, next_col


n = int(input())

matrix = [[x for x in input()] for x in range(n)]

jet_armor = 300
enemies = 4
jet_row = 0
jet_col = 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] == 'J':
            jet_row = r
            jet_col = c

while True:
    command = input()

    next_row, next_col = get_next_position(jet_row, jet_col, command)

    if matrix[next_row][next_col] == '-':
        matrix[jet_row][jet_col] = '-'
        jet_row, jet_col = next_row, next_col
        matrix[jet_row][jet_col] = 'J'
        continue

    elif matrix[next_row][next_col] == 'E':
        enemies -= 1
        if enemies > 0:
            jet_armor -= 100

    elif matrix[next_row][next_col] == 'R':
        jet_armor = 300

    matrix[jet_row][jet_col] = '-'
    jet_row, jet_col = next_row, next_col
    matrix[jet_row][jet_col] = 'J'

    if jet_armor == 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_row}, {jet_col}]!")
        break

    if enemies == 0:
        print("Mission accomplished, you neutralized the aerial threat!")
        break

for row in matrix:
    print(*row, sep='')
