#리스트를 문자열로 변환
s = input()
res = []
for i in range(len(s)):
    if(s[i].isupper()):
        res.append(s[i].lower())
    else:
        res.append(s[i].upper())

print(''.join(res))