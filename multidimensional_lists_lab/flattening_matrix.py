rows = int(input())

matrix = []
#
for i in range(rows):
    line = (int(x) for x in input().split(', '))
    matrix.append(line)

# matrix = [map(int, input().split(', ')) for _ in range(rows)] ???

flattened = [num for sublist in matrix for num in sublist]

print(matrix)
print(flattened)
