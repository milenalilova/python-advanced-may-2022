def is_in_range(row1, col1, row2, col2, row, col):
    result = True
    if not 0 <= row1 < row:
        result = False
    elif not 0 <= row2 < row:
        result = False
    elif not 0 <= col1 < col:
        result = False
    elif not 0 <= col2 < col:
        result = False

    return result


def is_valid(command):
    result = True
    if len(command) != 5:
        result = False
    elif command[0] != 'swap':
        result = False
    elif not is_in_range(int(command[1]), int(command[2]), int(command[3]), int(command[4]), rows, cols):
        result = False
    return result


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


rows, cols = [int(x) for x in input().split()]

matrix = [[ch for ch in input().split()] for ch in range(rows)]

command = input().split()

while command[0] != 'END':
    if is_valid(command):
        current_row = int(command[1])
        current_col = int(command[2])
        new_row = int(command[3])
        new_col = int(command[4])
        first_value = matrix[current_row][current_col]
        second_value = matrix[new_row][new_col]

        matrix[current_row][current_col] = second_value
        matrix[new_row][new_col] = first_value
        print_matrix(matrix)
    else:
        print("Invalid input!")

    command = input().split()
