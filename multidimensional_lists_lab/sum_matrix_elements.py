rows, cols = [int(x) for x in input().split(', ')]

matrix = []
matrix_sum = 0

for row in range(rows):
    lines = [int(x) for x in input().split(', ')]
    matrix.append(lines)
    matrix_sum += sum(matrix[row])

print(matrix_sum)
print(matrix)
