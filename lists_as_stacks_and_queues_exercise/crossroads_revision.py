from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
cars_passed = 0

line = input()
has_crashed = False

while line != 'END':
    current_green = green_light

    if line != 'green':
        cars.append(line)
    else:
        while current_green > 0 and cars:
            current_car = cars.popleft()
            if len(current_car) <= current_green:
                current_green -= len(current_car)
                cars_passed += 1
            else:
                if len(current_car) <= current_green + free_window:
                    cars_passed += 1
                    current_green = 0
                else:
                    idx = current_green + free_window
                    ch = current_car[idx]
                    print("A crash happened!")
                    print(f"{current_car} was hit at {ch}.")
                    has_crashed = True
                    break
        if has_crashed:
            break

    line = input()

if not has_crashed:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
