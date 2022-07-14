import math
s = input()
e = math.ceil(len(s)/10)

for i in range(e):

    if(i==e-1): #마지막 길이가 10이 아닌 경우를 처리함
        print(s[i*10:])
    else:
        print(s[i * 10:i * 10 + 10])
