def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_outside(rows, cols, santa_row, santa_col):
    if santa_row < 0:
        return rows - 1, santa_col
    elif santa_col < 0:
        return santa_row, cols - 1
    elif santa_row > rows - 1:
        return 0, santa_col
    elif santa_col > cols - 1:
        return santa_row, 0
    else:
        return santa_row, santa_col


def check_for_item(matrix, row, col, christmas_items):
    if matrix[row][col] == 'D':
        christmas_items['Christmas decorations'] += 1
    elif matrix[row][col] == 'G':
        christmas_items['Gifts'] += 1
    elif matrix[row][col] == 'C':
        christmas_items['Cookies'] += 1
    return christmas_items


rows, cols = [int(x) for x in input().split(', ')]

matrix = []
total_items = 0
santa_row, santa_col = 0, 0
walk_end = False

christmas_items = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0
}

for row in range(rows):
    row_elements = input().split(' ')
    for col in range(cols):
        if row_elements[col] == 'Y':
            santa_row, santa_col = row, col
        if row_elements[col] != '.' and row_elements[col] != 'Y':
            total_items += 1

    matrix.append(row_elements)

matrix[santa_row][santa_col] = 'x'

while True:
    command = input()
    if command == 'End':
        matrix[santa_row][santa_col] = 'Y'
        break

    command_parts = command.split('-')
    direction = command_parts[0]
    steps = int(command_parts[1])

    for step in range(steps):
        santa_row, santa_col = get_next_pos(direction, santa_row, santa_col)
        if is_outside:
            santa_row, santa_col = is_outside(rows, cols, santa_row, santa_col)
            check_for_item(matrix, santa_row, santa_col, christmas_items)
            matrix[santa_row][santa_col] = 'x'
            if sum(christmas_items.values()) == total_items:
                matrix[santa_row][santa_col] = 'Y'
                walk_end = True
                break
    if walk_end:
        break

if walk_end:
    print('Merry Christmas!')

print("You've collected:")
for key, value in christmas_items.items():
    print(f'- {value} {key}')

for row in matrix:
    print(*row)
