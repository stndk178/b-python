import math
d,h,w = map(int,input().split())
x = math.sqrt(d**2/(h**2+w**2))
print(int(x*h),int(w*x))