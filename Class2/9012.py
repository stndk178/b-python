n = int(input())
for i in range(n):
    res = []
    s = input()
    t = 1
    for j in range(len(s)):
        if(s[j]=="("): #(이면 스택에 추가
            res.append(s[j])
        else: #)이면 스택에서 pop
            if(len(res)==0): #pop할게 없으면 괄호 짝이 없음
                t = 0
                break
            else:
                res.pop()

    if t==0 or len(res) !=0: #스택에 남아있는 경우도 괄호 짝이 없는 경우이다.
        print("NO")
    else:
        print("YES")
