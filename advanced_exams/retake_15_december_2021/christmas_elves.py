from collections import deque

energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

toys = 0
energy_spent = 0
times = 0

while energy and materials:
    while energy and energy[0] < 5:
        energy.popleft()
    if not energy:
        break
    times += 1

    current_energy = energy.popleft()
    current_material = materials.pop()

    if times % 15 == 0:
        if current_energy >= 2 * current_material:
            energy_spent += 2 * current_material
            current_energy -= 2 * current_material
            energy.append(current_energy)

    elif times % 5 == 0:
        if current_energy >= current_material:
            energy_spent += current_material
            current_energy -= current_material
            energy.append(current_energy)
        else:
            materials.append(current_material)
            energy.append(current_energy * 2)

    elif times % 3 == 0:
        if current_energy >= 2 * current_material:
            toys += 2
            energy_spent += 2 * current_material
            current_energy -= 2 * current_material
            current_energy += 1
            energy.append(current_energy)
        else:
            materials.append(current_material)
            energy.append(current_energy * 2)

    elif current_energy >= current_material:
        toys += 1
        energy_spent += current_material
        current_energy -= current_material
        current_energy += 1
        energy.append(current_energy)

    elif current_energy < current_material:
        materials.append(current_material)
        energy.append(current_energy * 2)

print(f"Toys: {toys}")
print(f"Energy: {energy_spent}")
if energy:
    print(f"Elves left: {', '.join(map(str, energy))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
