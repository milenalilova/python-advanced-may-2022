from collections import deque

cycles = deque([int(x) for x in input().split(', ')])
index = int(input())

target_cycle = cycles[index]
counter = 0
clock_cycles = 0

while cycles:
    current_cycle = cycles.popleft()
    if current_cycle < target_cycle or (current_cycle == target_cycle and counter <= index):
        clock_cycles += current_cycle
    counter += 1

print(clock_cycles)
