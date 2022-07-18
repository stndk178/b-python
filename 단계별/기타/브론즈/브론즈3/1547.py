import sys
input = sys.stdin.readline
n = int(input())
res = 1
for i in range(n):
    lst = list(map(int,input().split()))
    if(lst[0]==res): #res에 첫번쨰 컵의 번호를 계속 저장해 나간다.
        res = lst[1]
    elif(lst[1]==res):
        res = lst[0]

print(res)