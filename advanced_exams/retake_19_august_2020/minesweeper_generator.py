def is_inside(a_row, a_col, matrix):
    return 0 <= a_row < len(matrix) and 0 <= a_col < len(matrix)


def count_bombs_near_cell(a_row, a_col, matrix):
    counter = 0

    directions = {
        "right": lambda r, c: (r, c + 1),
        "left": lambda r, c: (r, c - 1),
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c),
        "up left": lambda r, c: (r - 1, c - 1),
        "up right": lambda r, c: (r - 1, c + 1),
        "down left": lambda r, c: (r + 1, c - 1),
        "down right": lambda r, c: (r + 1, c + 1),
    }
    for key in directions:
        row, col = directions[key](a_row, a_col)
        if is_inside(row, col, matrix):
            if matrix[row][col] == "*":
                counter += 1
    return counter


size = int(input())
bombs_count = int(input())

field = [[0] * size for _ in range(size)]

for coord in range(bombs_count):
    coordinates = input()
    row, col = eval(coordinates)
    field[row][col] = '*'

for i in range(size):
    for j in range(size):
        if field[i][j] != '*':
            field[i][j] = count_bombs_near_cell(i, j, field)

for row in field:
    print(*row, sep=' ')
