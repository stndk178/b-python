a = []
for i in range(4):
    a.append(int(input()))
a.sort()
s = sum(a[1:4])

lst = []
for i in range(2):
    lst.append(int(input()))

print(s+max(lst))