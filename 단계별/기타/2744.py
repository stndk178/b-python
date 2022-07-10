s = input()
res = []
for i in range(len(s)):
    if(s[i].isupper()):
        res.append(s[i].lower())
    else:
        res.append(s[i].upper())

