#a b c
import sys
input = sys.stdin.readline
lst = list(map(int,input().split()))
lst.sort()
s = input().rstrip()
res = []
for i in range(len(s)):
    if(s[i]=="A"):
        res.append(lst[0])
    elif(s[i]=="B"):
        res.append(lst[1])
    else:
        res.append(lst[2])

print(res[0],res[1],res[2])