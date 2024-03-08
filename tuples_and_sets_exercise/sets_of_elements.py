n, m = [int(x) for x in input().split()]

set_n = set()
set_m = set()

# [set_n.add(int(input())) for _  in range(n)]  possible syntax

for _ in range(n):
    set_n.add(int(input()))

for _ in range(m):
    set_m.add(int(input()))

result = set_n.intersection(set_m)

for num in result:
    print(num)
