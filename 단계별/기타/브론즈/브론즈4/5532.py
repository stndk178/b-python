import sys
import math
input = sys.stdin.readline
lst = []
for i in range(5):
    lst.append(int(input()))
l,a,b,c,d = lst
w = max(math.ceil(a/c),math.ceil(b/d)) #동시에 숙제를 할 수 있기 때문에 둘 중에 더 큰 값을 선택하면 됨
print(l-w)
