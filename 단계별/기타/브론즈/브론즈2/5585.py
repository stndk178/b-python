import sys
input = sys.stdin.readline
coins = [500,100,50,10,5,1]
res = 0
n = int(input())
n = 1000-n
for i in coins:
    res += n//i
    n %= i

print(res)