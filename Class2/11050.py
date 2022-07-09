n, k = map(int,input().split())

def C1(n):
    if(n==0):
        return 1
    else:
        return C1(n-1)*n

print(int(C1(n)/(C1(k)*C1(n-k))))