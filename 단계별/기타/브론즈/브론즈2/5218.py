import sys
n = int(input())
def my_fun(s1,s2):
    res = []
    for i in range(len(s1)):
        r1 = ord(s1[i]) #ord()로 아스키코드 구하기
        r2 = ord(s2[i])
        if(r1>r2): #차이 구하기
            res.append(r2 + 26 - r1)
        else:
            res.append(r2 - r1)

    return res
for i in range(n):
    x,y = input().split()
    r = my_fun(x,y)
    print("Distances: ",end='')
    for i in range(len(r)):
        print(r[i],end=' ')
    print()