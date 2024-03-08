def is_outside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_children(matrix, row, col):
    possible_children = [
        [row + 1, col],
        [row - 1, col],
        [row, col + 1],
        [row, col - 1],
        [row - 1, col - 1],
        [row - 1, col + 1],
        [row + 1, col + 1],
        [row + 1, col - 1],
    ]

    result = []
    # counter = 0
    for child_row, child_col in possible_children:
        if is_outside(child_row, child_col, size):
            result.append([child_row, child_col])

    return result


size = int(input())
num = int(input())
matrix = []

for row in range(size):
    matrix.append([])
    for col in range(size):
        matrix[row].append(None)

for _ in range(num):
    coordinates = eval(input())
    bomb_row, bomb_col = coordinates

    matrix[bomb_row][bomb_col] = '*'
for row in range(len(matrix)):
    for col in range(len(matrix)):
        counter = 0
        if matrix[row][col] == None:
            cells = get_children(matrix, row, col)
            for cell_row, cell_col in cells:
                if matrix[cell_row][cell_col] == '*':
                    counter += 1
            if counter > 0:
                matrix[row][col] = counter
                counter = 0
            else:
                matrix[row][col] = 0

for el in matrix:
    print(' '.join([str(x) for x in el]))
