def find_initial_position(matrix, rows, cols):
    items_count = 0
    start_row, start_col = None, None
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'Y':
                start_row, start_col = i, j
            elif matrix[i][j] == 'D':
                items_count += 1
            elif matrix[i][j] == 'G':
                items_count += 1
            elif matrix[i][j] == 'C':
                items_count += 1
    return start_row, start_col, items_count


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


def adjust_position(row, col, rows, cols):
    if row < 0:
        row = rows - 1
    if row >= rows:
        row = 0
    if col < 0:
        col = cols - 1
    if col >= cols:
        col = 0
    return row, col


def check_next_position(row, col, matrix):
    if matrix[row][col] == 'D':
        return 'Christmas decorations'
    if matrix[row][col] == 'G':
        return 'Gifts'
    if matrix[row][col] == 'C':
        return 'Cookies'
    if matrix[row][col] == '.':
        return


rows, cols = [int(x) for x in input().split(', ')]

matrix = [list(input().split()) for _ in range(rows)]

collected_items_dict = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0
}

current_row, current_col, all_items = find_initial_position(matrix, rows, cols)
collected_all_items = False

command = input()

while command != 'End' and not collected_all_items:
    command = command.split('-')
    direction = command[0]
    steps = int(command[1])

    for step in range(steps):
        next_row, next_col = find_next_position(direction, current_row, current_col)
        if not is_inside(next_row, next_col, rows, cols):
            next_row, next_col = adjust_position(next_row, next_col, rows, cols)

        found_item = check_next_position(next_row, next_col, matrix)
        if found_item:
            collected_items_dict[found_item] += 1

        matrix[current_row][current_col] = 'x'
        current_row, current_col = next_row, next_col
        matrix[current_row][current_col] = 'Y'
        if sum(collected_items_dict.values()) == all_items:
            collected_all_items=True
            break

    if collected_all_items:
        break

    command = input()

if collected_all_items:
    print("Merry Christmas!")

print("You've collected:")
for k, v in collected_items_dict.items():
    print(f"- {v} {k}")

for row in matrix:
    print(*row, sep=' ')
