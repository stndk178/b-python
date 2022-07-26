import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
y = 0; m = 0;
for i in range(n):
    y += (lst[i]//30+1)*10
    m += (lst[i]//60+1)*15
if(y<m):
    print("Y",str(y))
elif(y>m):
    print("M",str(m))
else:
    print("Y M",str(y))