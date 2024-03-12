def is_vip(guest_code):
    return guest_code[0].isdigit()


n = int(input())

vip_guests = set()
regular_guests = set()

for i in range(n):
    guest_code = input()

    if is_vip(guest_code):
        vip_guests.add(guest_code)
    else:
        regular_guests.add(guest_code)

while True:
    command = input()

    if command == 'END':
        break
    if command in vip_guests:
        vip_guests.remove(command)
    else:
        regular_guests.remove(command)

print(len(vip_guests) + len(regular_guests))
[print(guest) for guest in sorted(vip_guests)]
[print(guest) for guest in sorted(regular_guests)]
