n = int(input())
compounds_set = set()

for _ in range(n):
    compounds = input().split()
    for compound in compounds:
        compounds_set.add(compound)

[print(compound) for compound in compounds_set]
