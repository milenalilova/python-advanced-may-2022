line = list(input())

stack = []

for i in range(len(line)):
    stack.append(line.pop())

print("".join(stack))
