import sys
input = sys.stdin.readline

a = ['a', 'e', 'i', 'o', 'u']
while True:
    s = input().rstrip() #sys로 할때는 꼭 rstrip()으로 공백 제거 해주기
    if(s=="#"):
        break
    s = s.lower()
    cnt = 0
    for i in a: #모음 찾기
        cnt += s.count(i)

    print(cnt)
