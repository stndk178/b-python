a = int(input())
b = int(input())

n3 = a *(((b%100))%10)
n4 = a * int(((b%100))/10)
n5 = a * int(b/100)


print(n3)
print(n4)
print(n5)
print(n3+(n4*10)+(n5*100))