from math import log

number = int(input())
base = input()

if base == 'natural':
    print(f"{log(number):.2f}")

else:
    print(f"{log(number, int(base)):.2f}")


# Variant 2
# from math import log, e
# 
# # Log(b)X = Y => b^y = x
#
# # Log(2)1024 = 10 => 2^10 = 1024
# # Log(10)10 = 1 => 10^1 = 10
# # Log(e)10 = 2.30 => e^2.30 = 10
#
#
# print(log(10, 10))
# print(log(10, e))
# print(log(10))
