#런타임 에러 코드 (OverflowError)
'''
n,m = map(int, input().split())
print(int(n/m))
print(n%m)
'''

#아마 큰 수여서 오류가 발생한 듯 -> int타입의 표현범위를 넘어서
n,m = map(int, input().split())
print(n//m) #나눗셈인데 소수점 이하는 버리고 정수 부분만
print(n%m)
#파이썬은 큰 수를 자동으로 처리 가능
