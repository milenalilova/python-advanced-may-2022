from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk = deque(int(x) for x in input().split(', '))

milkshakes = 0

while chocolates and milk and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_milk = milk.popleft()

    if current_chocolate <= 0 and current_milk <= 0:
        continue

    if current_chocolate <= 0:
        milk.appendleft(current_milk)
        continue

    if current_milk <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_milk == current_chocolate:
        milkshakes += 1

    else:
        milk.append(current_milk)
        current_chocolate = current_chocolate - 5
        chocolates.append(current_chocolate)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f'Chocolate: {", ".join([str(x) for x in chocolates])}')
else:
    print(f'Chocolate: empty')

if milk:
    print(f'Milk: {", ".join([str(x) for x in milk])}')
else:
    print(f'Milk: empty')
