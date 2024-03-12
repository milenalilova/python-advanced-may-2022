n = int(input())
cars = set()

for i in range(n):
    direction, car_plate = input().split(', ')

    if direction == 'IN':
        cars.add(car_plate)
    elif direction == 'OUT':
        cars.remove(car_plate)

if cars:
    [print(car) for car in cars]
else:
    print("Parking Lot is Empty")
