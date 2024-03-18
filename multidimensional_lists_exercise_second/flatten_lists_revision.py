matrix = input().split('|')
flattened_matrix = []

for el in range(len(matrix) - 1, -1, -1):
    nums = [int(x) for x in matrix[el].split()]
    flattened_matrix.extend(nums)

print(*flattened_matrix, sep=' ')
