rows = int(input())

matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]

print(even_matrix)
