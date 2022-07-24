'''시간초과 코드

import sys
input = sys.stdin.readline

a,b = input().split()
res =0
for i in range(len(a)):
    for j in range(len(b)):
        res += int(a[i]) * int(b[j])

print(res)
'''

import sys
input = sys.stdin.readline

a,b = input().split()
aa = 0; bb = 0;
for i in range(len(a)):
    aa += int(a[i])

for j in range(len(b)):
    bb += int(b[j])

print(aa*bb)