first_player, second_player = input().split(', ')

size = 6
matrix = []

current_player, next_player = first_player, second_player
winner = ""
resting_players = {
    'Tom': False,
    'Jerry': False
}

for row in range(size):
    row_elements = [x for x in input().split(' ')]
    matrix.append(row_elements)

while True:
    coordinates = eval(input())
    current_row, current_col = coordinates

    if current_player in resting_players:
        is_resting = ""
        continue
        # current_player, next_player = next_player, current_player

    if matrix[current_row][current_col] == 'E':
        winner = current_player
        print(f'{current_player} found the Exit and wins the game!')
        break

    elif matrix[current_row][current_col] == 'T':
        winner = next_player
        print(f'{current_player} is out of the game! The winner is {winner}.')
        break

    elif matrix[current_row][current_col] == 'W':
        print(f'{current_player} hits a wall and needs to rest.')
        is_resting = current_player

    elif matrix[current_row][current_col] == '.':
        pass

    current_player, next_player = next_player, current_player

