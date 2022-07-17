import sys,math
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))

b,c = map(int,input().split()) #b는 총감독관(1명), c는 부감독관(여러명)
cnt = 0
for i in range(n):
    lst[i] -= b #총감독관이 감시할수있는 응시생들의 수를 뺀다.
    cnt+=1
    if(lst[i]>0): #그래도 응시생들이 남아있을 경우 부감독관의 수를 구해서 더한다.
        cnt += math.ceil(lst[i]/c) #반올림한다.

print(cnt)