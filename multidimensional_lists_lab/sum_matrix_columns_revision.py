rows, cols = [int(x) for x in input().split(',')]

matrix = [[int(j) for j in input().split(' ')] for i in range(rows)]

for col_index in range(cols):
    column_sum = 0
    for row_index in range(rows):
        column_sum += matrix[row_index][col_index]
    print(column_sum)
