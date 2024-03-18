def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())

matrix = [[int(x) for x in input().split()] for x in range(size)]

command = input()

while command != 'END':
    instruction, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if instruction == 'Add':
        if is_valid(row, col, size):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    elif instruction == 'Subtract':
        if is_valid(row, col, size):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    command = input()

for row in matrix:
    print(*row, sep=' ')


