size = int(input())
matrix = [[j for j in input()] for i in range(size)]
symbol = input()

is_found = False
location = ()

for row in range(size):
    if is_found:
        break
    for col in range(size):
        if matrix[row][col] == symbol:
            location = f"({row}, {col})"
            is_found = True

if is_found:
    print(location)

else:
    print(f"{symbol} does not occur in the matrix")
