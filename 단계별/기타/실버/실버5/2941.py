#이게 맞다고? 너무 오래걸림.. 다른 방법은?
s = input()
cnt = 0
i = 0

while(i < len(s)):
    if s[i]=="c":
        if (s[i:i + 2] == "c="):
            cnt += 1
            i += 2 #다른 문자 처리하기 위해 인덱스 이동, 문자 길이만큼 이동
        elif (s[i:i + 2] == "c-"):
            cnt += 1
            i += 2
        else:
            cnt +=1
            i += 1
    elif s[i] =="d":
        if(s[i:i+3]=="dz="):
            cnt+= 1
            i = i + 3
        elif(s[i:i+2]=="d-"):
            i = i + 2
            cnt+=1
        else:
            cnt +=1
            i += 1
    elif s[i] == "l":
        if (s[i:i + 2] == "lj"):
            cnt += 1
            i = i + 2
        else:
            cnt += 1
            i += 1
    elif s[i] == "n":
        if (s[i:i + 2] == "nj"):
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif s[i] == "s":
        if (s[i:i + 2] == "s="):
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif s[i] == "z":
        if (s[i:i + 2] == "z="):
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    else: #그외 문자인 경우
        cnt+= 1
        i+=1


print(cnt)


'''
#처음에 생각했던 코드
    if s[i]=="c":
        j = i+1
        if j == len(s):
            break
        elif s[j] == "=":
            cnt += 1
            i = j
        elif s[j] == "-":
            cnt +=1
            i = j



'''

#다른 코드
'''
s = input()
a = alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in a:
    if i in s:
        s = s.replace(i,".")
print(len(n))


'''