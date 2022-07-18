import sys
input = sys.stdin.readline

while True:
    res = 0
    n = input().rstrip()
    if n=="0":
        break

    res += (len(n)-1) + 2 #숫자사이의 여백 + 양끝에서 여백 2cm
    for i in range(len(n)):
        if(n[i]=="1"):
            res += 2
        elif(n[i]=="0"):
            res += 4
        else:
            res += 3

    print(res)