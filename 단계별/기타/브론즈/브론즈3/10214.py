import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    res = [0] * 2
    for i in range(9):
        y,k = map(int,input().split())
        res[0] += y
        res[1] += k

    if(res[0]>res[1]):
        print("Yonsei")
    elif(res[0]<res[1]):
        print("Korea")
    else:
        print("Draw")
