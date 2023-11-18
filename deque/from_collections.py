from collections import deque


deq = deque()
deq.append('a')  # ['a']
deq.append('b')  # ['a', 'b']
deq.append('c')  # ['a', 'b', 'c']
deq.appendleft('9')
deq.rotate(1)

print(deq)