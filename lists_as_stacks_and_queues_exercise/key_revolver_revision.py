from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split(' ')]
locks = deque(int(x) for x in input().split(' '))
intelligence_value = int(input())

bullets_cost = 0
current_barrel = gun_barrel_size

while True:
    if not bullets or not locks:
        break

    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    bullets_cost += bullet_price
    current_barrel -= 1
    if current_barrel <= 0:
        if bullets:
            print("Reloading!")
            current_barrel = gun_barrel_size

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - bullets_cost}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
