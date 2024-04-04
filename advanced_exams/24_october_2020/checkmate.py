def find_position(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'K':
                return i, j


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
board = [list(input().split()) for _ in range(size)]

king_row, king_col = find_position(board, size)

queens_coordinates = opposite_king(king_row, king_col, board)
if queens_coordinates:
    for coord in queens_coordinates:
        print(coord)
else:
    print("The king is safe!")

# # Code needs optimization
# def find_position(matrix, size):
#     for i in range(size):
#         for j in range(size):
#             if matrix[i][j] == 'K':
#                 return i, j
#
#
# size = 8
# board = [list(input().split()) for _ in range(size)]
# queens_coordinates = []
#
# start_king_row, start_king_col = find_position(board, size)
# king_row, king_col = start_king_row, start_king_col
#
# # left
# while king_col > 0:
#     king_col -= 1
#     if board[king_row][king_col] == 'Q':
#         queens_coordinates.append([king_row, king_col])
#         break
# king_row, king_col = start_king_row, start_king_col
#
# # right
# while king_col < size - 1:
#     king_col += 1
#     if board[king_row][king_col] == 'Q':
#         queens_coordinates.append([king_row, king_col])
#         break
# king_row, king_col = start_king_row, start_king_col
#
# # up
# while king_row > 0:
#     king_row -= 1
#     if board[king_row][king_col] == 'Q':
#         queens_coordinates.append([king_row, king_col])
#         break
# king_row, king_col = start_king_row, start_king_col
#
# # down
# while king_row < size - 1:
#     king_row += 1
#     if board[king_row][king_col] == 'Q':
#         queens_coordinates.append([king_row, king_col])
#         break
# king_row, king_col = start_king_row, start_king_col
#
# # main diagonal (up left)
# while king_row > 0 and king_col > 0:
#     king_row -= 1
#     king_col -= 1
#     if board[king_row][king_col] == 'Q':
#         queens_coordinates.append([king_row, king_col])
#         break
# king_row, king_col = start_king_row, start_king_col
#
# # main diagonal (down left)
# while king_row < size - 1 and king_col < size - 1:
#     king_row += 1
#     king_col += 1
#     if board[king_row][king_col] == 'Q':
#         queens_coordinates.append([king_row, king_col])
#         break
# king_row, king_col = start_king_row, start_king_col
#
# # secondary diagonal (up right)
# while king_row > 0 and king_col < size - 1:
#     king_row -= 1
#     king_col += 1
#     if board[king_row][king_col] == 'Q':
#         queens_coordinates.append([king_row, king_col])
#         break
# king_row, king_col = start_king_row, start_king_col
#
# # secondary diagonal (down left)
# while king_row < size - 1 and king_col > 0:
#     king_row += 1
#     king_col -= 1
#     if board[king_row][king_col] == 'Q':
#         queens_coordinates.append([king_row, king_col])
#         break
#
# if queens_coordinates:
#     for coord in queens_coordinates:
#         print(coord)
# else:
#     print("The king is safe!")
