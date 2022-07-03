num = int(input())
cnt = 0
for i in range(num):
    res = i + int(i/100) + int((i%100)/10) + ((i%100)%10)

    if res >0 and res == num:
        print(i)
        cnt = 1
        break



if cnt==0:
    print(0)