import sys
input =sys.stdin.readline

lst = ['C','A','M','B','R','I','D','G','E']
s = input().rstrip()
for i in range(len(s)):
    if(s[i] in lst):
        s = s.replace(s[i],'-')
s = s.replace('-','')
print(s)

