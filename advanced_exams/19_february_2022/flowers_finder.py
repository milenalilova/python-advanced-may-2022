from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers_dict = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

is_found = False
found_flower = ''

while vowels and consonants and not is_found:
    current_vowel = vowels.popleft()
    current_consonants = consonants.pop()

    for flower in flowers_dict.keys():
        flowers_dict[flower] = flowers_dict[flower].replace(current_vowel, '')
        flowers_dict[flower] = flowers_dict[flower].replace(current_consonants, '')

        if flowers_dict[flower] == '':
            is_found = True
            found_flower = flower
            break
    if is_found:
        break

if is_found:
    print(f"Word found: {found_flower}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
