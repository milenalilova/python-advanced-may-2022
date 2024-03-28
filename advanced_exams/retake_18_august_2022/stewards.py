from collections import deque

seats = [x for x in input().split(', ')]
first_nums = deque([int(x) for x in input().split(', ')])
second_nums = deque([int(x) for x in input().split(', ')])

seat_matches = []
rotations = 0

while len(seat_matches) < 3 and rotations < 10:
    rotations += 1
    first_num = first_nums.popleft()
    second_num = second_nums.pop()
    sum_numbers = first_num + second_num
    ascii_char = chr(sum_numbers)

    for seat in seats:
        if seat == f'{first_num}{ascii_char}' or seat == f'{second_num}{ascii_char}':
            seats.remove(seat)
            seat_matches.append(seat)
            break
    else:
        first_nums.append(first_num)
        second_nums.appendleft(second_num)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
