import sys
input = sys.stdin.readline
res = []
for i in range(7):
    n = int(input())
    if(n%2==1): #홀수인 것만 리스트에 추가
        res.append(n)
if len(res)!=0:
    print(sum(res))
    print(min(res))
else:
    print(-1)