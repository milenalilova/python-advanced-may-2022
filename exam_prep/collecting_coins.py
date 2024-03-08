# Needs optimization. Unite the two functions about position

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


def is_outside(size, next_row, next_col):
    if next_row < 0:
        return size - 1, next_col
    elif next_col < 0:
        return next_row, size - 1
    elif next_row > size - 1:
        return 0, next_col
    elif next_col > size - 1:
        return next_row, 0
    # else:
    #     return next_row, next_col


size = int(input())

matrix = []
player_row, player_col = 0, 0
already_collected = []
my_path = []

for row in range(size):
    row_elements = input().split(' ')
    for col in range(size):
        if row_elements[col] == 'P':
            player_row, player_col = row, col
            my_path.append([player_row, player_col])
    matrix.append(row_elements)

coins = 0

while coins < 100:
    direction = input()
    next_row, next_col = get_next_position(player_row, player_col, direction)

    if is_inside(next_row, next_col, size):
        player_row, player_col = next_row, next_col

    else:
        player_row, player_col = is_outside(size, next_row, next_col)

    my_path.append([player_row, player_col])

    if matrix[player_row][player_col].isdigit():
        if [player_row, player_col] in already_collected:
            continue
        else:
            coins += int(matrix[player_row][player_col])
            already_collected.append([player_row, player_col])
            if coins >= 100:
                break
    elif matrix[player_row][player_col] == 'X':
        coins //= 2
        break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print('Your path:')
for el in my_path:
    print(el)
