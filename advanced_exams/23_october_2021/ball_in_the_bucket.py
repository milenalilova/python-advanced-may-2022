def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = 6
board = [list(input().split()) for _ in range(size)]
buckets_hit = []
total_points = 0

for _ in range(3):
    coordinates = input()
    current_row, current_col = map(int, coordinates.strip('(').strip(')').split(', '))
    if not is_inside(current_row, current_col, size):
        continue

    if board[current_row][current_col] == 'B':
        if [current_row, current_col] not in buckets_hit:
            buckets_hit.append([current_row, current_col])
            for i in range(6):
                if i != current_row:
                    total_points += int(board[i][current_col])
        else:
            continue
    else:
        continue

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
else:
    prize = ''

    if 100 <= total_points <= 199:
        prize = 'Football'

    elif 200 <= total_points <= 299:
        prize = 'Teddy Bear'

    elif total_points >= 300:
        prize = 'Lego Construction Set'

    print(f"Good job! You scored {total_points} points, and you've won {prize}.")



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
#                 and matrix[child_row][child_col] != 'B' and matrix[child_row][child_col] != 'H':
#             result += int(matrix[child_row][child_col])
#
#     return result
#
#
# def is_inside(row, col, size):
#     return 0 <= row < size and 0 <= col < size
#
#
# size = 6
#
# matrix = []
# for row in range(size):
#     row_elements = input().split(' ')
#     matrix.append(row_elements)
#
# points = 0
#
# prizes = {
#     "Football": 0,
#     "Teddy Bear": 0,
#     "Lego Construction Set": 0
# }
#
# for i in range(3):
#     coordinates = eval(input())
#     current_row, current_col = coordinates
#
#     if is_inside(current_row, current_col, size):
#         if matrix[current_row][current_col] == 'B':
#             value = check_position(current_row, current_col, matrix)
#             points += value
#             matrix[current_row][current_col] = 'H'
#
# if 100 <= points <= 199:
#     prizes["Football"] += 1
# elif 200 <= points <= 299:
#     prizes["Teddy Bear"] += 1
# elif points > 300:
#     prizes["Lego Construction Set"] += 1
#
# if prizes["Football"] > 0:
#     print(f"Good job! You scored {points} points, and you've won Football.")
#
# elif prizes["Teddy Bear"] > 0:
#     print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
#
# elif prizes["Lego Construction Set"] > 0:
#     print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
#
# else:
#     print(f'Sorry! You need {100-points} points more to win a prize.')