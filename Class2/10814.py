import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    name = list(sys.stdin.readline().split())
    lst.append(name)

lst.sort(key=lambda x:int(x[0]))



for item in lst:
    for i in item:
        print(i, end=' ')
    print()