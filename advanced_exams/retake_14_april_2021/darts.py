def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def find_corresponding_cells_value(row, col, matrix, size):
    left_cell = int(matrix[row][0])
    right_cell = int(matrix[row][size - 1])
    upper_cell = int(matrix[0][col])
    down_cell = int(matrix[size - 1][col])
    return left_cell + right_cell + upper_cell + down_cell


current_player, other_player = input().split(', ')

size = 7
dartboard = [list(input().split()) for _ in range(size)]
players_info_dict = {
    current_player: {'points': 501, 'throws': 0},
    other_player: {'points': 501, 'throws': 0}
}

winner = None

while True:
    coordinates = input()
    current_player_row, current_player_col = eval(coordinates)

    if not is_inside(current_player_row, current_player_col, size):
        players_info_dict[current_player]['throws'] += 1
        current_player, other_player = other_player, current_player
        continue

    if dartboard[current_player_row][current_player_col] == 'D':
        current_points = find_corresponding_cells_value(current_player_row, current_player_col, dartboard, size)
        players_info_dict[current_player]['points'] -= current_points * 2

    elif dartboard[current_player_row][current_player_col] == 'T':
        current_points = find_corresponding_cells_value(current_player_row, current_player_col, dartboard, size)
        players_info_dict[current_player]['points'] -= current_points * 3

    elif dartboard[current_player_row][current_player_col] == 'B':
        players_info_dict[current_player]['throws'] += 1
        winner = current_player
        break

    elif dartboard[current_player_row][current_player_col].isdigit():
        players_info_dict[current_player]['points'] -= int(dartboard[current_player_row][current_player_col])

    players_info_dict[current_player]['throws'] += 1

    if players_info_dict[current_player]['points'] <= 0:
        winner = current_player
        break
    current_player, other_player = other_player, current_player

print(f"{winner} won the game with {players_info_dict[current_player]['throws']} throws!")
