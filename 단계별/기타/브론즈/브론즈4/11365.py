import sys
input = sys.stdin.readline
while True:
    s = input().rstrip()


    if s=="END":
        break
    s = list(s)
    s.reverse()
    res = ''.join(s) #리스트를 문자열로
    print(res)

#print(s[::-1]) 가능(문자열 뒤집기)
