import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
lst.sort() #시간 작은 순서대로 정렬한다.
s = [0]*n
s[0] = lst[0]
for i in range(1,n): #부분합 구하기
    s[i] = s[i-1] + lst[i] #이전합과 현재 시간이랑 더해서 현재 합을 구한다.
print(sum(s)) #s에 저장된 값들을 모두 더한다.

'''


for i in range(n):
  s+=lst[i]*(n-i)
'''