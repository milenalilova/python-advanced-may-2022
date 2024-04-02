def find_initial_position(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'E':
                return i, j


def find_next_position(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


def validate_position(row, col, size):
    if row < 0:
        row = size - 1
    if row >= size:
        row = 0
    if col < 0:
        col = size - 1
    if col >= size:
        col = 0
    return row, col


matrix = [list(input().split()) for _ in range(6)]
commands = input().split(', ')
current_row, current_col = find_initial_position(matrix, 6)
water = 0
metal = 0
concrete = 0

for command in commands:
    next_row, next_col = find_next_position(command, current_row, current_col)
    current_row, current_col = validate_position(next_row, next_col, 6)

    if matrix[current_row][current_col] == 'W':
        water += 1
        print(f"Water deposit found at ({current_row}, {current_col})")
    elif matrix[current_row][current_col] == 'M':
        print(f"Metal deposit found at ({current_row}, {current_col})")
        metal += 1
    elif matrix[current_row][current_col] == 'C':
        print(f"Concrete deposit found at ({current_row}, {current_col})")
        concrete += 1
    elif matrix[current_row][current_col] == 'R':
        print(f"Rover got broken at ({current_row}, {current_col})")
        break
    elif matrix[current_row][current_col] == '-':
        pass

if water and metal and concrete:
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
