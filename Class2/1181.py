
N = int(input())
s = set()
for _ in range(N):

    str = input()
    s.add(str)

s = list(s)
s.sort()
s.sort(key = len)

for i in s:
    print(i)





