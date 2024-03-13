n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n + 1):
    ascii_values = 0

    name = input()
    for ch in name:
        ascii_values += ord(ch)
    ascii_values = int(ascii_values / row)

    if ascii_values % 2 == 0:
        even_set.add(ascii_values)
    else:
        odd_set.add(ascii_values)

result = set()

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)

elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)

elif sum(even_set) > sum(odd_set):
    result = even_set.symmetric_difference(odd_set)

print(', '.join(str(x) for x in result))
