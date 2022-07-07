import sys #이게 맞네 다른 방법은?

str = sys.stdin.readline()
str = str.lower().rstrip()

str2 = set()
for i in str:
    str2.add(i)

res =[]
mm = 0

lst = []
max_str = ""
for i in str2:
    if i in str:
        x = str.count(i)
        if(x>mm):
            mm = x
            max_str = i
        elif(x==mm):
            lst.append(x)

if len(lst)==0:
    print(max_str.upper())
else:

    if mm>max(lst):
        print(max_str.upper())
    else:
        print("?")

'''시간 초과 풀이
str = input()
str = str.lower()

cnt = 0
lst = []
for i in range(len(str)):

    t = str.count(str[i])

   if(t>cnt):
         cnt = t
        lst.append(str[i])

    elif(t == cnt and lst[-1] !=str[i]):
        cnt = 0
        break


if cnt == 0:
    print("?")
else:
    print(lst.pop().upper())

'''