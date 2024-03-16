n = int(input())

matrix = [[int(j) for j in input().split(' ')] for i in range(n)]

diagonal_sum = 0

for i in range(n):
    for j in range(n):
        if i == j:
            diagonal_sum += matrix[i][j]

print(diagonal_sum)
