import sys
input = sys.stdin.readline
def my_func(n):
    s = 0
    for i in range(n):
        s += int(input())
    return s

for i in range(3):
    t = int(input())
    res = my_func(t)
    if(res>0):
        print("+")
    elif(res<0):
        print("-")
    else:
        print(0)