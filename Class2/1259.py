while(True):
    num = list(input())


    if num[0]=='0':
        break

    if num == num[::-1]:
        print("yes")
    else:
        print("no")



