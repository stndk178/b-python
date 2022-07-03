#W 안쓴이유가 뭐지 다른 방법 생각 
import math
num = int(input())

for i in range(num):
    H,W,N = map(int, input().split())

    A = (N % H)

    if A == 0:
        A = H
    res = (A* 100) + (math.ceil(N / H))
    print(res)
