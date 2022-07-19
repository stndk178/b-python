res = []
n,k = map(int,input().split())
for i in range(n):
    coin = int(input())
    res.append(coin)

#Q.입력부터 내림차순으로 받는 방법?
res.reverse() #오름차순으로 동전이 주어지므로 그리디알고리즘을 위해서 역순으로 바꿈
cnt = 0
for c in res: #큰 동전부터 순서대로 주어짐
    cnt += k//c
    k %= c
print(cnt)