#스택
#시간초과 코드
'''

n = int(input())
a = []
for i in range(n):
    n1 = int(input())
    if(n1==0): #0이오면 가장 최근의 숫자를 pop한다.
        a.pop()
    else:
        a.append(n1)

print(sum(a))
'''
import sys #input만 이렇게해도 시간초과 안나네.. 다른 방법은 없나?
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    n1 = int(input())
    if(n1==0): #0이오면 가장 최근의 숫자를 pop한다.
        a.pop()
    else:
        a.append(n1)

print(sum(a))


