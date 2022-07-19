import sys
input = sys.stdin.readline
res =[]
n = int(input())
for i in range(n):
    lst = list(map(int,input().split()))
    res.append(lst)
res.sort(key=lambda x:x[0]) #첫번째 원소(시작시간) 정렬
res.sort(key=lambda x:x[1]) #두번째 원소(종료시간) 정렬


k = res[0][1] #가장 처음 원소의 종료시간을 선택
cnt = 1
for i in range(1,n):
    if(res[i][0]>=k): #가능한 시작시간 확인(k와 같거나 커야됨)
        cnt +=1
        k = res[i][1] #종료시간 업데이트

print(cnt)