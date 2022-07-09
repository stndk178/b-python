import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

res = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = lst[i] + lst[j] + lst[k]
            if(sum<=M):
                res = max(sum,res)


print(res)