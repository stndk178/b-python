s = input()
lst = [0]*26
for i in range(len(s)):
    n = ord(s[i])-ord('a')
    lst[n] += 1


for i in range(len(lst)):
    print(lst[i],end=' ')
#print(*lst)
#리스트 요소 한번에 출력하기(리스트 압축 해제해서)

'''#다른 풀이
a = [0]*26
s = input()
for i in s:
    a[ord(i)-ord('a')] += 1
print(*a)



'''