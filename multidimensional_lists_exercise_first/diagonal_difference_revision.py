size = int(input())

matrix = [[int(x) for x in input().split(' ')] for y in range(size)]

primary_diagonal = []
secondary_diagonal = []

for idx in range(size):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][size - 1 - idx])

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference)
