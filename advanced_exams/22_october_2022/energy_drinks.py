from collections import deque

caffeine = [int(x) for x in input().split(', ')]
drinks = deque([int(x) for x in input().split(', ')])

caffeine_consumed = 0

while caffeine and drinks:
    last_caffeine = caffeine.pop()
    first_drink = drinks.popleft()
    amount = last_caffeine * first_drink

    if amount + caffeine_consumed <= 300:
        caffeine_consumed += amount
    else:
        drinks.append(first_drink)
        caffeine_consumed -= 30
        if caffeine_consumed < 0:
            caffeine_consumed = 0

if drinks:
    print(f"Drinks left: {', '.join(str(x) for x in drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_consumed} mg caffeine.")
