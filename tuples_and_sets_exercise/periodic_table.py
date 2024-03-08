n = int(input())

elements = set()

for _ in range(n):
    current_set = set(input().split())
    elements = elements.union(current_set)

# for element in elements:
#     print(element)

print(*elements, sep='\n')

# n = int(input())
#
# elements = set()
#
# for _ in range(n):
#     compounds = input().split()
#     for el in compounds:
#         elements.add(el)
#
# for element in elements:
#     print(element)
