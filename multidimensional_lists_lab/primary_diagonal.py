size = int(input())
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split()))
    for y in range(0, size):
        matrix[x][y] = line[y]

sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
print(sum_diagonal)


# Other solutions

# def get_primary_diagonal_sum(matrix):
#     n = len(matrix)
#     # the_sum = 0
#
#     # This is very bad, O(NxN)
#     # for r in range(n):
#     #     for c in range(n):
#     #         if r == c:
#     #             the_sum += matrix[r][c]
#
#     # for i in range(n):
#     #     the_sum += matrix[i][i]
#     # return the_sum
#
#     return sum(matrix[i][i] for i in range(n))
#
#
# def get_secondary_diagonal(matrix):
#     n = len(matrix)
#     return sum(matrix[i][n - i - 1] for i in range(n))
#
#
# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     matrix.append(
#         [int(x) for x in input().split(' ')]
#     )
#
# print(get_primary_diagonal_sum(matrix))
# # print(get_secondary_diagonal(matrix))