n = int(input())

odd_set = set()
even_set = set()

for i in range(n):
    name = input()
    ch_sum = 0

    for ch in name:
        ch_sum += ord(ch)
    result = ch_sum // (i + 1)

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)

if odd_set_sum == even_set_sum:
    result = odd_set.union(even_set)

elif odd_set_sum > even_set_sum:
    result = odd_set.difference(even_set)

elif even_set_sum > odd_set_sum:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=', ')
