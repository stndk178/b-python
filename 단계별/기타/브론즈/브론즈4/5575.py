import sys
input = sys.stdin.readline
for i in range(3):
    lst = list(map(int,input().split()))
    x = lst[:3]
    y = lst[3:]
    res = (y[0]-x[0])*3600 + (y[1]-x[1])*60 + (y[2]-x[2]) #초단위로 근무 시간 구하기
    print(res//3600,res%3600//60,res%3600%60) #시간 분 초 구해서 출력력