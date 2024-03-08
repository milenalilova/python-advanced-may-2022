def get_next_position(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


line = input()

size = int(input())
field = []
player_row, player_col = 0, 0

for row in range(size):
    row_elements = [x for x in input()]
    for col in range(size):
        if row_elements[col] == 'P':
            player_row, player_col = row, col

    field.append(row_elements)

num = int(input())
for i in range(num):
    direction = input()

    next_row, next_col = get_next_position(player_row, player_col, direction)
    if is_inside(next_row, next_col, size):
        if field[next_row][next_col].isalpha():
            line += field[next_row][next_col]
        field[player_row][player_col] = '-'
        player_row, player_col = next_row, next_col
        field[player_row][player_col] = 'P'
    else:
        if len(line):
            line = line[0:-1]

print(line)
for row in field:
    print(''.join(row))
