import sys #이게 맞네 다른 방법은?

str = sys.stdin.readline()
str = str.lower().rstrip() #개행문자 제거

str2 = set() #set으로 중복된 문자 제거
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
        elif(x==mm): #여러 개 있을 경우 체크 
            lst.append(x)

if len(lst)==0:
    print(max_str.upper())
else: #가장 많이 사용된 알파벳이 여러 개 있을 가능성이 있음

    if mm>max(lst): #ex) AAAABBBBCCCCCCC 이런경우 
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
