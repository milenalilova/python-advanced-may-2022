n, m = [int(x) for x in input().split()]
n_length_set = set()
m_length_set = set()

for _ in range(n):
    number = int(input())
    n_length_set.add(number)

for _ in range(m):
    number = int(input())
    m_length_set.add(number)

[print(num) for num in n_length_set.intersection(m_length_set)]
