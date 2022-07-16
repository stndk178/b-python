#이게 되네..
import sys
input = sys.stdin.readline

h,m,s = map(int,input().split())
n = int(input())
m_t = n//60
s_t = n%60

m += m_t
s += s_t
#초 분 시 순서대로 처리한다.
while(s>59):
    s -=60
    m += 1

while(m>59):
    m -= 60
    h += 1

while(h>23):
    h -= 24

print(h,m,s)

'''
다른 방법
'''