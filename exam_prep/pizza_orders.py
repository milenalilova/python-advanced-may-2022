from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]

pizzas_made = 0

while pizza_orders and employees:
    pizzas = pizza_orders[0]
    employee = employees[-1]

    if pizzas <= 0:
        pizza_orders.popleft()
        continue
    elif pizzas > 10:
        pizza_orders.popleft()
        continue

    if pizzas <= employee:
        pizzas_made += pizzas
        pizza_orders.popleft()
        employees.pop()

    elif pizzas > employee:
        pizza_orders[0] -= employee
        pizzas_made += employee
        employees.pop()

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    if employees:
        print(f'Employees: {", ".join([str(x) for x in employees])}')

if not employees:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizza_orders])}')
