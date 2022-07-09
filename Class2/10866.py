import sys
n = int(sys.stdin.readline())
res = []
for i in range(n):
    lst = sys.stdin.readline().split()
    x = lst[0]
    if(len(lst)==2):
        y = lst[1]

    if(x =="push_front"):
        res.insert(0,y)
    if (x == "push_back"):
        res.append(y)

    elif(x=="pop_front"):
        if(len(res)!=0):
            print(res.pop(0))
        else:
            print(-1)
    elif (x == "pop_back"):
        if (len(res) != 0):
            print(res.pop())
        else:
            print(-1)

    elif(x=="size"):
        print(len(res))
    elif(x=="empty"):
        if(len(res)==0):
            print(1)
        else:
            print(0)
    elif(x=="front"):
        if(len(res)==0):
            print(-1)
        else:
            print(res[0])
    elif (x == "back"):
        if (len(res) == 0):
            print(-1)
        else:
            print(res[-1])
