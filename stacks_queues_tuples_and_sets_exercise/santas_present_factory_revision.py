from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

magic_needed_dict = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

presents_crafted_dict = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    if current_material == 0 and current_magic == 0:
        continue

    if current_material == 0:
        magic.appendleft(current_magic)
        continue

    if current_magic == 0:
        materials.append(current_material)
        continue

    result = current_material * current_magic

    if result in magic_needed_dict.keys():
        present = magic_needed_dict[result]
        presents_crafted_dict[present] += 1

    elif result < 0:
        result = current_material + current_magic
        materials.append(result)

    elif result > 0:
        materials.append(current_material + 15)

condition = False

for k, v in presents_crafted_dict.items():
    if (presents_crafted_dict['Doll'] > 0 and presents_crafted_dict['Wooden train'] > 0) or \
            (presents_crafted_dict['Teddy bear'] > 0 and presents_crafted_dict['Bicycle'] > 0):
        condition = True

if condition:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(material) for material in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(magic) for magic in magic)}")

for k, v in sorted(presents_crafted_dict.items()):
    if v > 0:
        print(f"{k}: {v}")
