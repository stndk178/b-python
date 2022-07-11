''' 시간초과
n,m = map(int, input().split())
for i in range(n,m+1):
    flag = 0
    if(i==1):
        flag = 1
    for j in range(2,i):
        if(i%j==0):
            flag = 1

    if flag == 0:
        print(i)

'''
#에라토스테네스의 체 소수구하기
n,m = map(int, input().split())
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    else:
        return True

for i in range(n,m+1):
    if isPrime(i):
        print(i)