from math import *

a,b,v = map(int, input().split())

print(ceil((v-a)/(a-b)) +1)




'''
while(True):

    res += a
    if(res>=v):
        day += 1
        print(day)

        break

    res -= b

    day+= 1
'''