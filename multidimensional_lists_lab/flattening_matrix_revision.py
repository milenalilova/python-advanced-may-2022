rows = int(input())

matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
flattened_matrix = [num for sublist in matrix for num in sublist]
print(flattened_matrix)
