#n을 사용하지 않음. count가 아니라 다른 방법으로 풀어야 하나?
n = int(input())
lst = list(map(int, input().split()))
v = int(input())

print(lst.count(v))