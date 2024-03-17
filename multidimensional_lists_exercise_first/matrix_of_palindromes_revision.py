rows, cols = [int(x) for x in input().split()]

letter = ord('a')
matrix = []

for row in range(rows):
    matrix.append([])
    palindrome = ''

    for col in range(cols):
        palindrome = f"{chr(row + letter)}{chr(col + row + letter)}{chr(row + letter)}"
        matrix[row].append(palindrome)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
