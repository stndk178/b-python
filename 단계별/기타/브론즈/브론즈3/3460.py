import sys
input = sys.stdin.readline
def my_fun(s):
    lst = []
    s = s[::-1]
    for i in range(len(s)):
        if(s[i]=="1"):
            lst.append(i)
    return lst

for i in range(int(input())):
    n = bin(int(input()))
    l = my_fun(str(n))
    print(' '.join(map(str,l)))  #숫자 리스트는 TypeError가 나는듯 -> 문자열로 변경


#reversed()로 뒤집기
#"".join(reversed(s))