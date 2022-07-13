l,p = map(int,input().split())
lst = list(map(int,input().split()))
res = [l*p]*5
for i in range(5):
    print(lst[i]-res[i],end=' ')
