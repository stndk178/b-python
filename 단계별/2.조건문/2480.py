import sys
a,b,c = map(int, sys.stdin.readline().split())

st = 0
m = 0
if(a==b==c):
    print(10000 + (a*1000))
elif(a==b or a==c):
    print(1000+ (a*100))
elif(b==c):
    print(1000 + (b * 100))
else:
    m = max(a,b,c)
    print(m*100)