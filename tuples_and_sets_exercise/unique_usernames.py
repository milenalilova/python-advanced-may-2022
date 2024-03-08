num = int(input())

unique_usernames = set()

for i in range(num):
    username = input()
    unique_usernames.add(username)

for username in unique_usernames:
    print(username)
