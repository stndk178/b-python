import sys
a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

b += c
while(b>=60):
    b -= 60
    a += 1
    if(a>=24):
        a -= 24

print(a, end=' ')
print(b)