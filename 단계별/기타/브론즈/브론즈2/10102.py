v = int(input())
s = input()
a = 0
b = 0
for i in range(v):
    if(s[i]=="A"):
        a += 1
    else:
        b += 1
if(a>b):
    print("A")
elif(a<b):
    print("B")
else:
    print("Tie")
#s.count('A') 이용하면 더 쉽게 풀 수 있음..