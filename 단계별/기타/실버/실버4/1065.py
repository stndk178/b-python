n = input()

def f1(n):
    ss = 0

    for i in range(1,int(n)+1):
        res = list(map(int, str(i)))
        if i<=99: #99까지 모두 한수
            ss += 1
        elif (res[0]-res[1]) == (res[1]-res[2]): #등차수열 확인
            ss += 1

    return ss

print(f1(n))