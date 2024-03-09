stack = list(input())

reversed_line = []

for i in range(len(stack)):
    reversed_line.append(stack.pop())

print(''.join(reversed_line))
