from collections import deque


def find_result(operator, nums):
    result = 0
    while len(nums) > 1:
        a = nums.popleft()
        b = nums.popleft()

        if operator == '*':
            result = a * b
        elif operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '/':
            result = a // b
        nums.appendleft(result)

    return result


expression = input().split()

operators = ["*", "+", "-", "/"]
numbers = deque()

for ch in expression:
    if ch not in operators:
        numbers.append(int(ch))
    else:
        result = find_result(ch, numbers)

print(numbers.popleft())

# Variant 2

# def find_result(operator, nums):
#     result = nums[0]
#     if operator == '*':
#         for num in nums[1:]:
#             result *= num
#     elif operator == '+':
#         for num in nums[1:]:
#             result += num
#     elif operator == '-':
#         for num in nums[1:]:
#             result -= num
#     elif operator == '/':
#         for num in nums[1:]:
#             result //= num
#     return result
#
#
# line = input().split()
# operators = ["*", "+", "-", "/"]
# digits = []
#
# for ch in line:
#     if ch not in operators:
#         digits.append(int(ch))
#     else:
#         result = find_result(ch, digits)
#         digits.clear()
#         digits.append(result)
#
# print(digits[0])
