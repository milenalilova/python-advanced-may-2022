def get_children(matrix, row, col):
    possible_children_coordinates = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1]
    ]

    result = []

    for child_row, child_col in possible_children_coordinates:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])

    return result


size = int(input())
matrix = []

for _ in range(size):
    line = [int(x) for x in input().split()]
    matrix.append(line)

bombs = input().split()

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(',')]
    damage = matrix[row][col]

    if damage <= 0:
        continue

    matrix[row][col] = 0

    children = get_children(matrix, row, col)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= damage

active_cells = 0
sum_active_cells = 0

for row in matrix:
    for col in row:
        if col > 0:
            active_cells += 1
            sum_active_cells += col

print(f"Alive cells: {active_cells}")
print(f"Sum: {sum_active_cells}")

for row in matrix:
    print(*row, sep=' ')
