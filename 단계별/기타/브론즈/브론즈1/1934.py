#유클리드 호제법 이용
import sys
input = sys.stdin.readline
#최대공약수
#r = x를 y로 나눈 나머지
#gcd(x,y) = gcd(y,r) r이 0이 될때의 b가 최대공약수
def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x

#최소공배수
for i in range(int(input())):
    a,b = map(int,input().split())
    print(a*b//gcd(a,b))