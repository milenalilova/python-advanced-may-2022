num = int(input())

unique_names = set()

for i in range(num):
    unique_names.add(input())

for name in unique_names:    # [print(name) for name in unique_names]
    print(name)
