numbers = list(input().split(' '))

reversed_numbers = []
for i in range(len(numbers)):
    reversed_numbers.append(numbers.pop())

print(' '.join(reversed_numbers))
