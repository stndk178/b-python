import sys
n = int(sys.stdin.readline())

lst = []

for i in range(n):
    d = list(map(int, sys.stdin.readline().split()))
    lst.append(d)


count = 0

res = []
for i in range(n):
    count = 0
    for j in range(n):

        if lst[i][0]<lst[j][0] and  lst[i][1]<lst[j][1]:
            count +=1

    res.append(count+1)


for i in res:
    print(i, end=' ')