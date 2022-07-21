import sys
input = sys.stdin.readline

res_p = 0
res_s = 0

for i in range(5):
    lst = list(map(int,input().split()))
    if(sum(lst)>res_s):
        res_s = sum(lst)
        res_p = i+1
print(res_p,res_s)