from collections import deque

food_quantity = int(input())
orders_line = input()

orders = deque(int(x) for x in orders_line.split(' '))

print(max(orders))

served = True
while orders:
    current_order = orders[0]
    if current_order <= food_quantity:
        food_quantity -= orders.popleft()
    else:
        served = False
        break

if served:
    print(f"Orders complete")
else:
    orders_left = []
    while orders:
        orders_left.append(str(orders.popleft()))
    print(f"Orders left: {' '.join(orders_left)}")
