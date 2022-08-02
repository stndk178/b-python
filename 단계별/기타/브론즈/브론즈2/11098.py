import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    p = int(input())
    res = []
    for _ in range(p):
        x,y = input().split() #리스트에 (가격,선수이름)리스트를 추가한다.
        res.append((int(x),y))
    print(max(res)[1]) #가격이 가장 큰 선수의 이름을 출력한다.
