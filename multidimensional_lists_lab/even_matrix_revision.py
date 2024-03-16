# rows = int(input())
#
# matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
# even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
#
# print(even_matrix)


# Better version
def is_even(number):
    return number % 2 == 0


def get_even(matrix):
    return [x for x in matrix if is_even(x)]


rows = int(input())

matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]

print(
    [get_even(row) for row in matrix]
)
