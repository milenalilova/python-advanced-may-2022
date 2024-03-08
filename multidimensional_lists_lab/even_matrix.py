n = int(input())

matrix = []

for i in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]

print(even_matrix)
