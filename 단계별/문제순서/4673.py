res = 0
a = []
for i in range(1,10001):
    res = 0
    s = str(i)
    for j in range(len(s)):
       res += int(s[j])
    res += i
    a.append(res)

for i in range(1,10001):
    if i in a:
        continue
    else:
        print(i)

''' 조금더 생각
def selfNum(n)
    n += sum(map(int,str(n)))
    return n
    
a = [0]*10001
for i in range(1,10001):
    a[i] = selfNum(i)

for i in range(1,10001):
    if i not in a:
        print(i)
    

'''