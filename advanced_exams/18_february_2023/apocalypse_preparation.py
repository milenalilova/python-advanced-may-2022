from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

healing_items_dict = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    items_sum = current_textile + current_medicament

    if items_sum == 30:
        healing_items_dict['Patch'] += 1
    elif items_sum == 40:
        healing_items_dict['Bandage'] += 1
    elif items_sum == 100:
        healing_items_dict['MedKit'] += 1
    elif items_sum > 100:
        healing_items_dict['MedKit'] += 1
        items_sum -= 100
        medicaments[-1] += items_sum
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

if not textiles and medicaments:
    print("Textiles are empty.")

if not medicaments and textiles:
    print("Medicaments are empty.")

if healing_items_dict:
    sorted_items = sorted(healing_items_dict.items(), key=lambda x: (-x[1], x[0]))
    for item in sorted_items:
        if int(item[1]) > 0:
            print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
