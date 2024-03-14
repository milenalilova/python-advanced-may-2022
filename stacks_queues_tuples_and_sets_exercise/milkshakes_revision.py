from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_milk = deque(int(x) for x in input().split(', '))

milkshakes_count = 0

while chocolates and cups_milk and milkshakes_count < 5:

    current_chocolate = chocolates.pop()
    current_milk = cups_milk.popleft()

    if current_milk <= 0 and current_chocolate <= 0:
        continue

    if current_chocolate <= 0:
        cups_milk.appendleft(current_milk)
        continue

    if current_milk <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        milkshakes_count += 1

    else:
        cups_milk.append(current_milk)
        current_chocolate -= 5
        chocolates.append(current_chocolate)

if milkshakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(choc) for choc in chocolates)}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join(str(milk) for milk in cups_milk)}")
else:
    print("Milk: empty")
