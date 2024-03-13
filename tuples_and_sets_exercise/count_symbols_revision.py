text = input()

characters_count = {}

for ch in text:
    if ch not in characters_count.keys():
        characters_count[ch] = 0
    characters_count[ch] += 1

for char, count in sorted(characters_count.items()):
    print(f"{char}: {count} time/s")
