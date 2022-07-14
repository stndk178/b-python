n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in range(5):
    if n== lst[i]:
        cnt += 1

print(cnt)