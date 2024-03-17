rows, cols = [int(x) for x in input().split()]

matrix = [[ch for ch in input().split()] for ch in range(rows)]

equals_count = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            equals_count += 1

print(equals_count)
