rows, cols = [int(x) for x in input().split(',')]
matrix = []
matrix_sum = 0

for row in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)
    matrix_sum += sum(line)

print(matrix_sum)
print(matrix)
