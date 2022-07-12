#시간초과 코드
'''
n = int(input())
lst = list(map(int, input().split()))
m = int(input())
res = list(map(int, input().split()))

for i in res:
    if i in lst:
        print(1)
    else:
        print(0)
'''

#이진탐색으로 풀기
import sys
input = sys.stdin.readline

def search(a, v, l, h):
    if l>h :
        return False
    m = (l+h)//2
    if a[m] > v:
        return search(a,v,l,m-1)
    elif a[m] < v:
        return search(a,v,m+1,h)
    else:
        return True

n = int(input())
lst = sorted(list(map(int, input().split()))) #이분탐색을 위해서 정렬해야함
m = int(input())
res = list(map(int, input().split()))

for i in res:
    if search(lst,i,0,n-1):
        print(1)
    else:
        print(0)
