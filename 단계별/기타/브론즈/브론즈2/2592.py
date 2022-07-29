import sys
input = sys.stdin.readline

lst = []
#평균 구하기
for i in range(10):
    lst.append(int(input()))
print(sum(lst)//10)

#최빈값 구하기
s = set(lst) #set으로 중복되는 값 제거
m = 0; res = 0;
for i in s: #set에 있는 값으로 리스트에서 count
    if lst.count(i) >m: #최빈값을 저장한다.
        m = lst.count(i)
        res = i
print(res)

'''
lst2 = []
for i in lst:
    lst2.append([lst.count(i),i)])
    
print(lst2) #max(lst2)[1]
'''