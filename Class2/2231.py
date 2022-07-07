num = int(input())

for i in range(num+1):
    a = list(map(int,str(i)))
    res = i + sum(a)

    if res == num:
        print(i)
        break
    if i == num:
        print(0)

