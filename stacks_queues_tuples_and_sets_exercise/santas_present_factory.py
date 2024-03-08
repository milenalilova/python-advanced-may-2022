from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_toys = {}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    # product = current_material * current_magic

    if current_material == 0 and current_magic == 0:
        continue

    if current_magic == 0:
        materials.append(current_material)
        continue

    if current_material == 0:
        magic.appendleft(current_magic)
        continue

    product = current_material * current_magic
    if product in presents:
        crafted_toy = presents[product]
        if crafted_toy in crafted_toys:
            crafted_toys[crafted_toy] += 1
        else:
            crafted_toys[crafted_toy] = 1
        continue

    if product < 0:
        materials.append(current_material + current_magic)
    else:
        materials.append(current_material + 15)

if ('Doll' in crafted_toys and 'Wooden train' in crafted_toys) or \
        ('Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(str(x) for x in reversed(materials))}')

if magic:
    print(f'Magic left: {", ".join(str(x) for x in magic)}')

for key, value in sorted(crafted_toys.items()):
    print(f'{key}: {value}')
