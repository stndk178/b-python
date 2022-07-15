n = int(input()) #set도 이용
cnt = 0
for i in range(n):
    s = input()
    res = s[0] #res에 계속 추가함. 연속해서 나오는 문자를 하나로 압축함

    for j in s:
        if j != res[-1]: #다를 경우에만 추가한다.
            res += j

    s = set(s)

    if(len(s)==len(res)): #두개의 길이가 같으면 떨어져나오는 문자가 없다.
        cnt += 1


print(cnt)