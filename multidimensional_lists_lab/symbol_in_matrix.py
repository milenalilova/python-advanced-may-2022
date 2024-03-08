n = int(input())

# matrix = [list(input()) for _ in range(n)]

matrix = []

for _ in range(n):
    line = list(input())
    matrix.append(line)

symbol = input()
location = ()
is_found = False

for row in range(n):
    if is_found:
        break
    for col in range(n):
        if matrix[row][col] == symbol:
            location = (row, col)
            is_found = True

if location:
    print(location)
else:
    print(f'{symbol} does not occur in the matrix')


# def find_symbol(matrix, symbol):
#     # for row_index in range(n):
#     #     for column_index in range(n):
#     #         if matrix[row_index][column_index] == symbol:
#     #             return row_index, column_index
#
#     for row_index in range(n):
#         if symbol in matrix[row_index]:
#             column_index = matrix[row_index].index(symbol)
#             return row_index, column_index
#
#
# n = int(input())
#
# matrix = [list(input()) for _ in range(n)]
# symbol = input()
#
# result = find_symbol(matrix, symbol)
#
# if result:
#     row_index, column_index = result
#     print(f'({row_index}, {column_index})')
# else:
#     print(f'{symbol} does not occur in the matrix')
#