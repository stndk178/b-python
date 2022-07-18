n = int(input())
res = [0]*2
for i in range(n):
    n1 = int(input())
    res[n1] += 1

if(res[0]>res[1]):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")