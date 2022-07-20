import sys
input = sys.stdin.readline
n = int(input())
for i in range(1,2*n+1):
    if i%2 == 0:
        x = n//2
        print(" *"*x)
    else:
        x = (n-1)//2
        print("* "*x + "*")
