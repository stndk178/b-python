import sys
n, k = map(int, sys.stdin.readline().split())
lst = []
for i in range(1,n+1):
    lst.append(i)

print(lst)
rmv = k-1;
res = []


while(len(lst)!=0) :

    res.append(lst.pop(rmv))

    if(rmv>=len(lst)):
        rmv -= len(lst)
        continue

    rmv += k - 1

print(res)