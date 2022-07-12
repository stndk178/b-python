'''
import sys
n, k = map(int, sys.stdin.readline().split())
lst = []
for i in range(1,n+1):
    lst.append(i)

print(lst)
rmv = k-1;
res = []


while(len(lst)!=0) :

    res.append(lst.pop(rmv))

    if(rmv>=len(lst)):
        rmv -= len(lst)
        continue

    rmv += k - 1

print(res)
'''

#큐 이용
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
lst = list(range(1,n+1))
q = deque(lst)
cnt = 0
res = []

while len(q) !=0:
    cnt += 1
    if(cnt == k):
        t = q.popleft()
        res.append(t)
        cnt = 0
    else:
        t = q.popleft()
        q.append(t)
print("<",end = '')
for i in res:
    if i == res[-1]:
        print(i,end='')
    else:
        print(i,",",sep = '', end = ' ')

print(">", end= '')

#출력부분 다시 해보기
'''
print('<' ,end= '')
for i in range(len(res)):
    if i == len(res)-1:
        print('%d>' %res[i])
    else:
        print(res[i], end=', ')
'''
