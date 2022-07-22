import sys
input = sys.stdin.readline
x,y = input().split()
x = x[::-1]; y= y[::-1]
res = int(x)+int(y)
print(int(str(res)[::-1]))

#''.join(list(reversed(x)))