from collections import deque

quantity = int(input())
queue = deque()

name = input()

while name != "Start":
    queue.append(name)

    name = input()

command = input().split(' ')

while command[0] != "End":
    if command[0] == "refill":
        litres = int(command[1])
        quantity += litres
    else:
        litres = int(command[0])
        if quantity >= litres:
            quantity -= litres
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    command = input().split(' ')

print(f"{quantity} liters left")
