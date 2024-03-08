from collections import deque

materials = [int(x) for x in input().split(' ')]
magic_levels = deque(int(x) for x in input().split(' '))

crafted_presents = {}

while materials and magic_levels:
    material = materials[-1]
    magic = magic_levels[0]
    mixed = material + magic
    present = ''

    if mixed < 100:
        if mixed % 2 == 0:
            result = material * 2 + magic * 3
            mixed = result
        else:
            result = mixed * 2
            mixed = result
    elif mixed > 499:
        mixed = mixed / 2

    if 100 <= mixed <= 199:
        present = 'Gemstone'
        if present not in crafted_presents:
            crafted_presents[present] = 1
        else:
            crafted_presents[present] += 1

    elif 200 <= mixed <= 299:
        present = 'Porcelain Sculpture'
        if present not in crafted_presents:
            crafted_presents[present] = 1
        else:
            crafted_presents[present] += 1

    elif 300 <= mixed <= 399:
        present = 'Gold'
        if present not in crafted_presents:
            crafted_presents[present] = 1
        else:
            crafted_presents[present] += 1

    elif 400 <= mixed <= 499:
        present = 'Diamond Jewellery'
        if present not in crafted_presents:
            crafted_presents[present] = 1
        else:
            crafted_presents[present] += 1

    materials.pop()
    magic_levels.popleft()

if ('Gemstone' in crafted_presents and 'Porcelain Sculpture' in crafted_presents) \
        or ('Gold' in crafted_presents and 'Diamond Jewellery' in crafted_presents) in crafted_presents:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

if crafted_presents:
    sorted_presents = [f'{key}: {value}' for key, value in sorted(crafted_presents.items(), key=lambda x: x[0])]
    print('\n'.join(sorted_presents))
