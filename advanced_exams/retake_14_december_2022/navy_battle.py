def find_initial_position(size, matrix):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'S':
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


def handle_next_position(next_row, next_col, current_row, current_col, matrix, hits, ships):
    if matrix[next_row][next_col] == '-':
        pass
    elif matrix[next_row][next_col] == '*':
        hits += 1
        matrix[next_row][next_col] = '-'
    elif matrix[next_row][next_col] == 'C':
        ships -= 1
        matrix[next_row][next_col] = '-'
    return hits, ships


size = int(input())
battlefield = [list(input()) for _ in range(size)]

sub_row, sub_col = find_initial_position(size, battlefield)
battlefield[sub_row][sub_col] = '-'
cruisers_count = 3
hits_taken = 0

while True:
    if cruisers_count == 0:
        battlefield[sub_row][sub_col] = 'S'
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    if hits_taken == 3:
        battlefield[sub_row][sub_col] = 'S'
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{sub_row}, {sub_col}]!")
        break

    command = input()

    next_row, next_col = find_next_position(command, sub_row, sub_col)
    hits_taken, cruisers_count = handle_next_position(next_row, next_col, sub_row, sub_col, battlefield,
                                                                   hits_taken,
                                                                   cruisers_count)
    sub_row, sub_col = next_row, next_col

for row in battlefield:
    print(''.join(row))
