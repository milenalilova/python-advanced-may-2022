def accommodate_new_pets(hotel_capacity, max_weight_limit, *args):
    accommodated_pets = {}
    all_pets_accommodated = True

    for arg in args:
        if hotel_capacity <= 0:
            all_pets_accommodated = False
            break
        pet_type, pet_weight = arg
        if pet_weight > max_weight_limit:
            continue

        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        hotel_capacity -= 1

    accommodated_pets = dict(sorted(accommodated_pets.items(), key=lambda x: x[0]))

    output = ''

    if all_pets_accommodated:
        output += f"All pets are accommodated! Available capacity: {hotel_capacity}.\n"
    else:
        output += "You did not manage to accommodate all pets!\n"
    output += "Accommodated pets:\n"

    for k, v in accommodated_pets.items():
        output += f"{k}: {v}\n"

    return output


# Author's solution
# def accommodate_new_pets(capacity, max_weight, *pets_data):
#     accommodated_pets = {}
#     result = []
#
#     for pet_type, pet_weight in pets_data:
#         if capacity <= 0:
#             result.append('You did not manage to accommodate all pets!')
#             break
#         if pet_weight > max_weight:
#             continue
#         if pet_type not in accommodated_pets:
#             accommodated_pets[pet_type] = 0
#         accommodated_pets[pet_type] += 1
#         capacity -= 1
#     else:
#         result.append(f'All pets are accommodated! Available capacity: {capacity}.')
#
#     result.append('Accommodated pets:')
#     [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(accommodated_pets.items())]
#     return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print()

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print()

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
