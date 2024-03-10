clothes = [int(x) for x in input().split(' ')]
capacity = int(input())

racks_count = 0
current_capacity = 0

while clothes:
    piece = clothes[-1]
    current_capacity += piece
    if current_capacity <= capacity:
        clothes.pop()
        if not clothes:
            racks_count += 1
    else:
        racks_count += 1
        current_capacity = 0

print(racks_count)
