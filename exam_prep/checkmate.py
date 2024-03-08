def is_inside(a_row, a_col, matrix):
    return 0 <= a_row < len(matrix) and 0 <= a_col < len(matrix)


def opposite_king(a_row, a_col, matrix):
    can_capture = []

    directions = {
        "right": lambda r, c: (r, c + 1),
        "left": lambda r, c: (r, c - 1),
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c),
        "up left": lambda r, c: (r - 1, c - 1),
        "up right": lambda r, c: (r - 1, c + 1),
        "down left": lambda r, c: (r + 1, c - 1),
        "down right": lambda r, c: (r + 1, c + 1),
    }

    for key in directions:
        row, col = directions[key](a_row, a_col)
        while is_inside(row, col, matrix):
            if matrix[row][col] == "Q":
                can_capture.append([row, col])
                break
            row, col = directions[key](row, col)

    return can_capture

size = 8
king_row, king_col = 0, 0
board = []
queens_hits = []

for row in range(size):
    row_elements = input().split(' ')
    for col in range(size):
        if row_elements[col] == 'K':
            king_row, king_col = row, col
    board.append(row_elements)

capturing_king = opposite_king(king_row, king_col, board)

if capturing_king:
    for el in capturing_king:
        print(el)
else:
    print(f"The king is safe!")

