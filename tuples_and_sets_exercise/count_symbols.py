text = input()

symbols = {}

for ch in text:
    if ch in symbols:
        symbols[ch] += 1
    else:
        symbols[ch] = 1

for symbol, count in sorted(symbols.items()):
    print(f'{symbol}: {count} time/s')
