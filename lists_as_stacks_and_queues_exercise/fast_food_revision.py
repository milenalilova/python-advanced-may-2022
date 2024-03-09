from collections import deque

quantity_food = int(input())
orders = [int(x) for x in input().split(' ')]

queue = deque(orders)
print(max(queue))

while queue:
    current_order = queue[0]
    if current_order <= quantity_food:
        quantity_food -= current_order
        queue.popleft()
    else:
        break

if queue:
    result = "Orders left: "
    while queue:
        result += f"{str(queue.popleft())} "
    print(result)
else:
    print("Orders complete")
