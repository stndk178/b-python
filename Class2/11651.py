import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    d = list(map(int, sys.stdin.readline().split()))
    lst.append(d)

lst.sort(key= lambda x : (x[1], x[0]))

for i in lst:
    for j in i:
        print(j, end=' ')
    print()