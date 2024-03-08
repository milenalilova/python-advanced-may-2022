rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

sub_matrix = []
best_sum = float('-inf')
start_row = 0
start_col = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > best_sum:
            best_sum = current_sum
            start_row = row
            start_col = col

print(f'{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]}')
print(f'{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]}')
print(best_sum)
