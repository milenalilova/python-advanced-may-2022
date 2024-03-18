size = int(input())

field = [[ch for ch in input().split()] for ch in range(size)]

bunny_row = 0
bunny_col = 0

for row in range(size):
    for col in range(size):
        if field[row][col] == 'B':
            bunny_row = row
            bunny_col = col

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

best_sum = float('-inf')
best_direction = ''
best_path = []

for direction in directions:
    current_sum = 0
    current_path = []

    row, col = directions[direction](bunny_row, bunny_col)
    while 0 <= row < size and 0 <= col < size and field[row][col] != 'X':
        current_sum += int(field[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

    if current_sum > best_sum:
        best_sum = current_sum
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path, sep='\n')
print(best_sum)
