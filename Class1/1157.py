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


