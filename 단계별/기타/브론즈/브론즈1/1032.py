import sys
input = sys.stdin.readline
lst = []
n = int(input())
for i in range(n):
    lst.append(input().rstrip())

a = len(lst[0])
res = list(lst[0])
for i in range(1,n):
    for j in range(a):
        if(lst[i-1][j] != lst[i][j]): #다른게 있다면 ?로 바꿈
            res[j] = "?" #여기서 replace(res[j],"?")를 사용하면 오답
print(''.join(res)) #리스트를 하나의 문자열로 합쳐서 출력

