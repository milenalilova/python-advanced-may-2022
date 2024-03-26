from collections import deque

money_sequence = [int(x) for x in input().split()]
prices_sequence = deque([int(x) for x in input().split()])

foods_eaten = 0

while money_sequence and prices_sequence:
    current_money = money_sequence.pop()
    current_price = prices_sequence.popleft()

    if current_money == current_price:
        foods_eaten += 1

    elif current_money > current_price:
        change = current_money - current_price
        foods_eaten += 1
        if money_sequence:
            money_sequence[-1] += change

if foods_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")

elif foods_eaten == 1:
    print(f"Henry ate: {foods_eaten} food.")

elif 1 < foods_eaten < 4:
    print(f"Henry ate: {foods_eaten} foods.")

elif foods_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")
