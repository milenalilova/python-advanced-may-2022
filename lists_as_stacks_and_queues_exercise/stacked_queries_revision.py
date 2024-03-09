n = int(input())
stack = []

for i in range(n):
    query = input().split(' ')

    if query[0] == '1':
        number = int(query[1])
        stack.append(number)

    elif query[0] == '2' and stack:
        stack.pop()

    elif query[0] == '3' and stack:
        print(max(stack))

    elif query[0] == '4' and stack:
        print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))
