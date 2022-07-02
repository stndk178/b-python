data = list(map(int, input().split()))
lst = [1,2,3,4,5,6,7,8]

if data == lst:
    print("ascending")
elif data == lst[::-1]:
    print("descending")
else:
    print("mixed")



#오답
'''
data = list(map(int, input().split()))

count = 0
for i in range(7):

    if data[0]==1 and (data[i]+1 == data[i+1]):
        count = 1
    elif data[0]==8 and (data[i]-1 == data[i+1]):
        count = 2
    else:
        break



if count ==1 :
    print("ascending")
elif count ==2:
    print("descending")
else:
    print("mixed")



'''