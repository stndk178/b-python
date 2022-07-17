#import sys
#input = sys.stdin.readline
#sys로 입력하면 안되는 듯? --> 처리하는 방법?
#input()은 EOFError를 발생시킴
#sys.stdin.readline()은 빈 문자열을 반환한다.
while True:
    try:
        s = input()
        print(s)
    except:
        break


#sys.stdin.readline EOF 처리방법
'''
import sys
input = sys.stdin.readline
while True:
    s = input().rstrip()
    if s != '': 
        print(s)
    else: #빈 문자열일 때 EOF
        break


'''

