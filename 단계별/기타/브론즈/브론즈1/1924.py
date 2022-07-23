r=[0,31,28,31,30,31,30,31,31,30,31,30,31] #일 수
x,y = map(int,input().split())
w=["SUN","MON", "TUE", "WED", "THU", "FRI", "SAT"]

s = sum(r[1:x])
res = (s+y)%7 #7로 나눈 나머지
print(w[res])