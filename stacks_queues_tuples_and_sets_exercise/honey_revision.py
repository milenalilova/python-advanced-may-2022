from collections import deque


def calculate_value(symbol, bee, nectar):
    value = 0
    if symbol == '+':
        value = bee + nectar
    elif symbol == '-':
        value = bee - nectar
    elif symbol == '*':
        value = bee * nectar
    elif symbol == '/':
        value = bee / nectar
    return value


bees = deque(int(x) for x in input().split())
nectars = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

while bees and nectars:
    current_bee = bees.popleft()
    current_nectar = nectars.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
        continue

    if current_nectar == 0:
        continue

    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        result = calculate_value(current_symbol, current_bee, current_nectar)
        honey += abs(result)

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(bee) for bee in bees)}")

if nectars:
    print(f"Nectar left: {', '.join(str(nectar) for nectar in nectars)}")
