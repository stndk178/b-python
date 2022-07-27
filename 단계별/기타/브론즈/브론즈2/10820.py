#다른 풀이?
#파이썬 EOF

def  count_lower(s):
    cnt = 0
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            cnt += 1
    return cnt

def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if "A"<= s[i] <= "Z":
           cnt += 1
    return cnt

def count_num(s):
    cnt = 0
    for i in range(10):
        cnt += s.count(str(i))
    return cnt

while True:
    try:
        s = input()
        print(count_lower(s), count_upper(s), count_num(s), s.count(" "))

    except:
        break