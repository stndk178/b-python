#다른 방법은 없나?
import sys
input = sys.stdin.readline
res = []
for i in range(10):
    res.append(int(input()))

x = 0
idx = 0
while True:
    x += res[idx]
    if x>100 or idx==9: #idx==9가 없으면 런타임 에러 (IndexError)가 남
        break
    #반례) 1 2 3 4 5 6 ... 10인 경우
    idx += 1
x = sum(res[:idx]); y = sum(res[:idx+1]) #합이 100을 넘어가는 index를 찾아서 그 값과 그다음 값을 비교한다. 답이 100을 넘어갈 수도 있다.
if(100-x>y-100):
    print(y)
elif(100-x<y-100):
    print(x)
else:
    print(y)
