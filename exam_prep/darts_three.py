# From pastebin

def position_value(r, c):
    row_value = int(matrix[r][0]) + int(matrix[r][size - 1])
    col_value = int(matrix[0][c]) + int(matrix[size - 1][c])
    return row_value + col_value


size = 7
player_one, player_two = input().split(', ')
players = {player_one: 501, player_two: 501}

matrix = []
for _ in range(size):
    elements = input().split(' ')
    matrix.append(elements)

current_player, other_player = player_one, player_two
throws = 0
while True:
    if current_player == player_one:
        throws += 1
    result = players[current_player]
    row, col = (int(x) for x in input().strip('()').split(', '))
    if row < 0 or row >= size or col < 0 or col >= size:
        current_player, other_player = other_player, current_player
        continue

    value = matrix[row][col]
    if value == 'B':
        result -= result
    elif value == "D":
        result -= position_value(row, col) * 2
    elif value == "T":
        result -= position_value(row, col) * 3
    else:
        result -= int(value)
    players[current_player] = result
    if result <= 0:
        break
    current_player, other_player = other_player, current_player

print(f'{current_player} won the game with {throws} throws!')