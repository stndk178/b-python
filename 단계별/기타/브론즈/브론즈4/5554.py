import sys
input = sys.stdin.readline
sum = 0
for i in range(4):
    n = int(input())
    sum += n

x = sum//60 #분
y = sum%60 #초
print(x)
print(y)