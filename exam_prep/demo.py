# size = 6
# area = []
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == 'E':
#             rover_row, rover_col = row, col
#     area.append(row_elements)
#
# print(area)
#
#
# # matrix = [list(input())for _ in range(6)]
# # commands = input().split(", ")
# #
# # print(matrix)
#
# def get_next_pos(row, col, direction):
#     if direction == 'up':
#         return row - 1, col
#     if direction == 'down':
#         return row + 1, col
#     if direction == 'left':
#         return row, col - 1
#     if direction == 'right':
#         return row, col + 1
#
#
# def is_inside(row, col, size):
#     return 0 <= row < size and 0 <= col < size
#
# def is_outside(rows, cols, santa_row, santa_col):
#     if santa_row < 0:
#         return rows - 1, santa_col
#     elif santa_col < 0:
#         return santa_row, cols - 1
#     elif santa_row > rows - 1:
#         return 0, santa_col
#     elif santa_col > cols - 1:
#         return santa_row, 0
#     else:
#         return santa_row, santa_col
#
# def get_around_kids(matrix, row, col):
#     result = []
#     if is_inside(row, col - 1, len(matrix) and matrix[row][col - 1] == 'X' or matrix[row][col - 1] == "V"):
#         result.append([row, col - 1])
#     if is_inside(row, col + 1, len(matrix) and matrix[row][col + 1] == 'X' or matrix[row][col + 1] == "V"):
#         result.append([row, col + 1])
#     if is_inside(row - 1, col, len(matrix) and matrix[row - 1][col] == 'X' or matrix[row - 1][col] == "V"):
#         result.append([row - 1, col])
#     if is_inside(row + 1, col, len(matrix) and matrix[row + 1][col] == 'X' or matrix[row + 1][col] == "V"):
#         result.append([row + 1, col])
#
#     return result

# def check_position(row, col, matrix):
#     possible_moves = [
#         [row, col],
#         [row - 1, col],
#         [row - 2, col],
#         [row - 3, col],
#         [row - 4, col],
#         [row - 5, col],
#         [row + 1, col],
#         [row + 2, col],
#         [row + 3, col],
#         [row + 4, col],
#         [row + 5, col],
#     ]
#     result = 0
#     for child_row, child_col in possible_moves:
#         if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) \
#                 and matrix[child_row][child_col] != 'B':
            # and matrix[child_row][child_col] != 'H':
            # result += int(matrix[child_row][child_col])
    #
    # return result


# size = 6
#
# matrix = []
# for row in range(size):
#     row_elements = input()
#     matrix.append(row_elements)
#
# print(check_position(0, 0, matrix))

def get_children(row, col, rows, cols):
    possible_children = [
        [row - 1, col],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col]
    ]

    result = []
    for child_row, child_col in possible_children:
        if not is_outside(child_row, child_col, rows, cols):
            result.append([child_row, child_col])

    return result