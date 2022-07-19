import sys
input = sys.stdin.readline
n = int(input())
res = []
for i in range(n):
    a,b,c = map(int,input().split())
    if(a==b==c):
        res.append(10000+a*1000)
    elif(a==b):
        res.append(1000 + a * 100)
    elif(a==c):
        res.append(1000 + a * 100)
    elif(b==c):
        res.append(1000+b*100)
    else:
        m = max(a, b, c)
        res.append(m * 100)

print(max(res))

#3의 수가 모두 다른 경우가 a!=b!=c가 아닌건가?