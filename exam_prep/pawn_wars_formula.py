'''
# Best solution:
white - (6, 2)
black - (1, 6)
if abs(col(white) - col(black)) > 1:
   fastest to last row
else:
    distance = abs(row(white) - row(black))
    if distance is odd:
        black wins
    else:
        white wins
'''


def find_player_position(matrix, player):
    for (row_index, row) in enumerate(matrix):
        if player in row:
            return (row_index, row.index(player))

    return (None, None)


def get_chess_position(row, column):
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    columns_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return row_names[row], columns_names[column]


ROWS_COUNT = 8
COLUMNS_COUNT = 8

matrix = [input().split(' ') for _ in range(ROWS_COUNT)]

white_row, white_column = find_player_position(matrix, 'w')
black_row, black_column = find_player_position(matrix, 'b')

position = (None, None)
winner = 'w'
is_queen = abs(white_column - black_column) > 1
white_steps = white_row
black_steps = ROWS_COUNT - black_row - 1
winner = 'w' if white_steps <= black_steps else 'b'

if is_queen:
    pass

else:
    pass
# capture

player = 'White' if current_player == 'w' else 'Black'
(row_name, column_name) = get_chess_position(*current_player_position)
position_name = f'{column_name}{row_name}'

if is_capture:
    print(f'Game over! {player} win, capture on {position_name}.')

if is_queen:
    print(f'Game over! {player} pawn is promoted to a queen at {position_name}.')
