N = int(input())

count = 0
lst = list(map(int, input().split()))

for i in lst:
    for k in range(1,1000):


        if(i%k==0):
            continue
        else:
            count += 1
            break

print(count)