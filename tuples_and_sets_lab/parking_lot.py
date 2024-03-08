num = int(input())

car_plates = set()

for i in range(num):
    direction, car_plate = input().split(', ')
    if direction == 'IN':
        car_plates.add(car_plate)
    elif direction == 'OUT':
        car_plates.remove(car_plate)

if car_plates:
    for car in car_plates:
        print(car)
else:
    print(f'Parking Lot is Empty')
