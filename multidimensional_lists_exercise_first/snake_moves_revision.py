# Interesting task

rows, cols = [int(x) for x in input().split()]
line = input()

idx = 0

for row in range(rows):
    matrix = [None] * cols
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols - 1, -1, -1)
    for col in range(start, end, step):
        matrix[col] = line[idx % len(line)]
        idx += 1

    print(''.join(matrix))
