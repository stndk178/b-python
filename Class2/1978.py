N = int(input())

count = 0
flag = 1
lst = list(map(int, input().split()))

for i in lst:
    flag = 1
    if(i==1):
        continue
    else:
        for k in range(2,i):
            if(i%k==0):
                flag = 0

        if(flag==1):
            count +=1

print(count)