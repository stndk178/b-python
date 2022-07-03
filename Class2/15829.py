L = int(input())
str = input()
res = 0
for i in range(L):
    res += (ord(str[i])-96) * (31 **i)

print(res%1234567891)
