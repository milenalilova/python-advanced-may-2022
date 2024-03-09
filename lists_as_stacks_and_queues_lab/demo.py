from collections import deque

q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(q)
for _ in range(4):
    q.append(q.popleft())

print(q)

q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(q)
q.rotate(5)
print(q)

q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(q)
q.rotate(-4)
print(q)

# ll = []
#
# # Push, add, append
# ll.append(1) - correct
# ll.insert(0, 1) - very wrong
#
# # Pop, remove
# ll.pop() - correct
# ll.pop(0) - very wrong
#
# # Peek
# print(ll[-1]) - correct
# print(ll[0]) - very wrong
#
# # Len, count, size
# print(len(ll))


# Stack implemented with list, resizing array
# (other) Stack implemented as linked list
s = []  # This is a stack

# Pushes
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
s.append(7)
s.append(8)
print(s)

# Peek
print(s[-1])  # s[len(s) -1]
print(s)

# s.insert(2, 15) # This is not a stack operation

# Pop
s.pop()
print(s)

# Push
s.append(9)
print(s)

# Not stack operations
# s.insert()
# s.reverse()
# s.count()
# s.sort()
# s.pop(0)
# s[0]

from collections import deque

q = deque()
# Enqueue, push, add
q.append(2)  # appendRight()
q.append(3)  # appendRight()
q.append(4)  # appendRight()
# q.appendleft(3)

print(q)
# Dequeue, pop, remove
q.popleft()
# q.pop()  # popRight()

# Combinations:
# append() + popleft()
# appendleft() + pop()
print(q)

# Peek
print(q[0])

# Count

class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def count(self):
        return len(self.values)


s = Stack()

for v in range(5, 10): # 5, 6, 7, 8, 9
    s.push(v)

print(s.pop())
print(s.peek())
print(s.count())

import time

s = []
count = 2 ** 16  # 1024 * 32 ~ 32000
result = 0

start = time.time()
for i in range(count):
    s.append(i)
while s:
    result += s.pop()

end = time.time()
print(end - start)

start = time.time()
for i in range(count):
    s.insert(0, i)
while s:
    result += s.pop(0)

end = time.time()

print(end - start)