# From pastebin. 81/100 in Judge. To change range (-1) probably. Deff up and left

# check with this input
# . . . . . . . .
# . . Q . . . . .
# . . . . . . . .
# . . Q . . . . .
# . . . . . . . .
# Q Q K . . . . .
# . . . . . . . .
# . . . . . . . .
# на горе трябва да върне [3, 2], а на ляво [5, 1], при теб връща [1, 2] и [5, 0]



def check_row_up(sign, player_row, player_col, board):
    for row in range(0, player_row):
        if board[row][player_col] == sign:
            return [row, player_col]


def check_row_down(sign, player_row, player_col, board):
    for row in range(player_row, len(board)):
        if board[row][player_col] == sign:
            return [row, player_col]


def check_col_left(sign, player_row, player_col, board):
    for col in range(0, player_col):
        if board[player_row][col] == sign:
            return [player_row, col]


def check_col_right(sign, player_row, player_col, board):
    for col in range(player_col, len(board)):
        if board[player_row][col] == sign:
            return [player_row, col]


def down_right_diagonal(sign, player_row, player_col, board):
    col = player_col
    row = player_row
    while row < len(board) and col < len(board):
        if board[row][col] == sign:
            return [row, col]
        else:
            row += 1
            col += 1


def down_left_diagonal(sign, player_row, player_col, board):
    col = player_col
    row = player_row
    while row < len(board) and col >= 0:
        if board[row][col] == sign:
            return [row, col]
        else:
            row += 1
            col -= 1


def up_right_diagonal(sign, player_row, player_col, board):
    col = player_col
    row = player_row
    while row >= 0 and col < len(board):
        if board[row][col] == sign:
            return [row, col]
        else:
            row -= 1
            col += 1


def up_left_diagonal(sign, player_row, player_col, board):
    col = player_col
    row = player_row
    while row >= 0 and col >= 0:
        if board[row][col] == sign:
            return [row, col]
        else:
            row -= 1
            col -= 1


size = 8
matrix = []
king_row = 0
king_col = 0
queens_list_hit = []
queens_sign = 'Q'
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'K':
            king_row = row
            king_col = col
        elif row_elements[col] == 'Q':
            queen_row = row
            queen_col = col
    matrix.append(row_elements)

queens_list_hit.append(check_row_up(queens_sign, king_row, king_col, matrix))
queens_list_hit.append(check_row_down(queens_sign, king_row, king_col, matrix))
queens_list_hit.append(check_col_left(queens_sign, king_row, king_col, matrix))
queens_list_hit.append(check_col_right(queens_sign, king_row, king_col, matrix))
queens_list_hit.append(up_left_diagonal(queens_sign, king_row, king_col, matrix))
queens_list_hit.append(up_right_diagonal(queens_sign, king_row, king_col, matrix))
queens_list_hit.append(down_left_diagonal(queens_sign, king_row, king_col, matrix))
queens_list_hit.append(down_right_diagonal(queens_sign, king_row, king_col, matrix))

queens_list_hit = [x for x in queens_list_hit if x != None]

if len(queens_list_hit) <= 0:
    print("The king is safe!")
else:
    for item in queens_list_hit:
        print(item)