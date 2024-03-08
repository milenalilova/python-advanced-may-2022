clothes_stack = [int(x) for x in input().split()]
capacity = int(input())

racks_number = 1
capacity_left = capacity

while clothes_stack:
    last_piece_clothing = clothes_stack[-1]
    if last_piece_clothing <= capacity_left:
        capacity_left -= last_piece_clothing
        clothes_stack.pop()

    else:
        racks_number += 1
        capacity_left = capacity

print(racks_number)
