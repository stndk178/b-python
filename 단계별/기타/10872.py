n = int(input())
def f1(n):
    if(n==0):
        return 1
    else:
        return f1(n-1)*n

print(f1(n))