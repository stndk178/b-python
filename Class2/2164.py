import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
c = list(range(1,n+1))
q = deque(c)
while True:
    if(len(q)==1):
        break

    q.popleft()
    q.append(q.popleft())

print(q[0])


#시간초과 코드
'''
import sys
input = sys.stdin.readline
n = int(input())
q = []
for i in range(1,n+1):
    q.append(i)

while True:
    if(len(q)==1):
        break

    q.pop(0)
    q.append(q.pop(0))

print(q[0])







'''

'''
q = deque()
for i in range(1,n+1):
    q.append(i)
    

'''