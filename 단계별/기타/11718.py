#예외처리
while True:
    try:
        print(input())
    except EOFError:
        break