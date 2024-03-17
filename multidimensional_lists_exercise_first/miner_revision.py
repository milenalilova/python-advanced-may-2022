def update_position(matrix, direction, row, col):
    new_position = []
    if direction == 'left':
        new_position = [row, col - 1]
    elif direction == 'right':
        new_position = [row, col + 1]
    elif direction == 'up':
        new_position = [row - 1, col]
    elif direction == 'down':
        new_position = [row + 1, col]
    new_row = new_position[0]
    new_col = new_position[1]

    if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix):
        new_row = row
        new_col = col

    return new_row, new_col


size = int(input())
directions = input().split()

matrix = [[ch for ch in input().split()] for ch in range(size)]

coal_pieces = 0

current_row = 0
current_col = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 's':
            current_row = row
            current_col = col
        elif matrix[row][col] == 'c':
            coal_pieces += 1

# game_over = False
for direction in directions:
    current_row, current_col = update_position(matrix, direction, current_row, current_col)

    if matrix[current_row][current_col] == 'e':
        # game_over = True
        print(f"Game over! ({current_row}, {current_col})")
        break
    elif matrix[current_row][current_col] == 'c':
        coal_pieces -= 1
        matrix[current_row][current_col] = '*'
        if coal_pieces <= 0:
            print(f"You collected all coal! ({current_row}, {current_col})")
            break
else:
    print(f"{coal_pieces} pieces of coal left. ({current_row}, {current_col})")
