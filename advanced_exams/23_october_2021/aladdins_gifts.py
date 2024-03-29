from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

gifts_dict = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

have_succeeded = False

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    sum_values = current_material + current_magic

    if sum_values < 100:
        if sum_values % 2 == 0:
            sum_values = current_material * 2 + current_magic * 3
        else:
            sum_values *= 2

    if sum_values > 499:
        sum_values = current_material / 2 + current_magic / 2

    if 100 <= sum_values <= 199:
        gifts_dict['Gemstone'] += 1

    elif 200 <= sum_values <= 299:
        gifts_dict['Porcelain Sculpture'] += 1

    elif 300 <= sum_values <= 399:
        gifts_dict['Gold'] += 1

    elif 400 <= sum_values <= 499:
        gifts_dict['Diamond Jewellery'] += 1

if (gifts_dict['Gemstone'] > 0 and gifts_dict['Porcelain Sculpture'] > 0) or \
        (gifts_dict['Gold'] > 0 and gifts_dict['Diamond Jewellery'] > 0):
    have_succeeded = True

if have_succeeded:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

sorted_dict = dict(sorted(gifts_dict.items(), key=lambda x: x[0]))
for gift, amount in sorted_dict.items():
    if amount > 0:
        print(f"{gift}: {amount}")



