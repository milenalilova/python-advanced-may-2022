from collections import deque

orders = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]

pizzas_made = 0

while orders and employees:
    while orders and orders[0] <= 0:
        orders.popleft()
    if not orders:
        break

    current_order = orders.popleft()
    current_employee = employees.pop()

    if current_order > 10:
        employees.append(current_employee)

    elif current_order <= current_employee:
        pizzas_made += current_order
    else:
        pizzas_made += current_employee
        current_order -= current_employee
        orders.appendleft(current_order)

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    if employees:
        print(f"Employees: {', '.join(map(str, employees))}")
if not employees and orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, orders))}")
