def my_fun(n):
    lst = list(map(int,input().split()))
    return sum(lst)

for i in range(int(input())):
    print(my_fun(int(input())))
