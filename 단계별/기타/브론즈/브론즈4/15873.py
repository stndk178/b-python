s = input()
if len(s)==2:
    print(int(s[0])+int(s[1]))
elif len(s) ==3:
    if s[0:2] == "10":
        print(int(s[0:2])+int(s[2]))
    elif s[1:3] == "10":
        print(int(s[1:3])+int(s[0]))
else:
    print(int(s[0:2]) + int(s[2:4]))