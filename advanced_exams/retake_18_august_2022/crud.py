def find_next_position(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


def handle_operation(operation, next_row, next_col, value, matrix):
    if operation == 'Create':
        if matrix[next_row][next_col] == '.':
            matrix[next_row][next_col] = value

    elif operation == 'Update':
        if matrix[next_row][next_col] != '.':
            matrix[next_row][next_col] = value

    elif operation == 'Delete':
        if matrix[next_row][next_col] != '.':
            matrix[next_row][next_col] = '.'

    elif operation == 'Read':
        if matrix[next_row][next_col] != '.':
            print(matrix[next_row][next_col])
    return matrix


size = 6
matrix = [list(input().split()) for _ in range(size)]
coordinates = input()
current_row = int(coordinates[1])
current_col = int(coordinates[4])

while True:
    command = input().split(', ')

    if command[0] == 'Stop':
        break

    operation = command[0]
    direction = command[1]
    value = command[2] if operation == 'Create' or operation == 'Update' else None

    next_row, next_col = find_next_position(direction, current_row, current_col)
    matrix = handle_operation(operation, next_row, next_col, value, matrix)
    current_row, current_col = next_row, next_col

for row in matrix:
    print(*row, sep=' ')



# Also works 
# def find_next_position(command, row, col):
#     if command == 'up':
#         return row - 1, col
#     if command == 'down':
#         return row + 1, col
#     if command == 'left':
#         return row, col - 1
#     if command == 'right':
#         return row, col + 1
#
#
# size = 6
# matrix = [list(input().split()) for _ in range(size)]
# coordinates = input()
# current_row = int(coordinates[1])
# current_col = int(coordinates[4])
#
# while True:
#     command = input().split(', ')
#
#     if command[0] == 'Stop':
#         break
#
#     operation = command[0]
#     direction = command[1]
#     next_row, next_col = find_next_position(direction, current_row, current_col)
#
#     if operation == 'Create':
#         value = command[2]
#         if matrix[next_row][next_col] == '.':
#             matrix[next_row][next_col] = value
#
#     elif operation == 'Update':
#         value = command[2]
#         if matrix[next_row][next_col] != '.':
#             matrix[next_row][next_col] = value
#
#     elif operation == 'Delete':
#         if matrix[next_row][next_col] != '.':
#             matrix[next_row][next_col] = '.'
#
#     elif operation == 'Read':
#         if matrix[next_row][next_col] != '.':
#             print(matrix[next_row][next_col])
#
#     current_row, current_col = next_row, next_col
#
# for row in matrix:
#     print(*row, sep=' ')
