from collections import deque

queue = deque()
water_quantity = int(input())
name = input()
while name != "Start":
    queue.append(name)
    name = input()

command = input()
while command != "End":
    if "refill" in command:
        water_quantity += int(command.split()[1])
    else:
        litres = int(command)
        if litres <= water_quantity:
            water_quantity -= litres
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    command = input()

print(f"{water_quantity} liters left")


# SECOND VARIANT
# from collections import deque
#
# queue = deque()
#
# quantity = int(input())
#
# while True:
#     name = input()
#     if name == "Start":
#         break
#     else:
#         queue.append(name)
#
# while True:
#     command = input().split()
#
#     if command[0] == "End":
#         break
#
#     elif command[0] == "refill":
#         amount = int(command[1])
#         quantity += amount
#     else:
#         water = int(command[0])
#         if water <= quantity:
#             quantity -= water
#             name = queue.popleft()
#             print(f"{name} got water")
#         else:
#             name = queue.popleft()
#             print(f"{name} must wait")
#
# print(f"{quantity} liters left")
