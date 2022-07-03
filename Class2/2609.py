#다시 풀어보기
#수학 정수론, 유클리드 호제법 공부
a, b = map(int, input().split())

def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def lcm(x,y):
    res = (x*y) //gcd(x,y)
    return res

print(gcd(a,b))
print(lcm(a,b))
