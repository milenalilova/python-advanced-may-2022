names = input().split(', ')

board = [list(input().split()) for _ in range(6)]
current_player = names[0]
other_player = names[1]
hit_a_wall = []

while True:
    position = list(map(int, input().strip('(').strip(')').split(', ')))

    player_row, player_col = position[0], position[1]
    if hit_a_wall:
        if current_player == hit_a_wall[0]:
            hit_a_wall.remove(current_player)
            current_player, other_player = other_player, current_player
            continue

    if board[player_row][player_col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif board[player_row][player_col] == 'T':
        print(f"{current_player} is out of the game! The winner is {other_player}.")
        break

    elif board[player_row][player_col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        hit_a_wall.append(current_player)

    elif board[player_row][player_col] == '.':
        pass

    current_player, other_player = other_player, current_player
