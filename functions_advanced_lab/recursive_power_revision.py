def recursive_power(number, power):
    result = 1
    if power == 0:
        return result
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
