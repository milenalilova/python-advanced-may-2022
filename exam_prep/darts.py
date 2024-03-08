# My code

def is_outside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def calculate_score(row, col, size, multiplier):
    score_sum = int(board[0][col]) + int(board[size - 1][col]) + int(board[row][0]) + int(board[row][size - 1])
    if multiplier == 'D':
        return score_sum * 2
    elif multiplier == 'T':
        return score_sum * 3
    elif multiplier == 'B':
     return 501

first_player, second_player = [x for x in input().split(', ')]
size = 7
board = []

for row in range(size):
    row_elements = input().split(' ')
    board.append(row_elements)

current_player, other_player = first_player, second_player
players_points = {first_player: 501, second_player: 501}
players_throws = {first_player: 0, second_player: 0}

winner = ''

while True:

    coordinates = eval(input())
    current_row, current_col = coordinates
    players_throws[current_player] += 1

    if is_outside(current_row, current_col, size):

        if board[current_row][current_col].isdigit():
            players_points[current_player] -= int(board[current_row][current_col])
        else:
            multiplier = board[current_row][current_col]
            score = calculate_score(current_row, current_col, size, multiplier)
            players_points[current_player] -= score

        if players_points[current_player] <= 0:
            winner = current_player
            break

    current_player, other_player = other_player, current_player

print(f"{winner} won the game with {players_throws[winner]} throws!")
