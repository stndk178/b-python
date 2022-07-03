
x, y, w, h = map(int, input().split())


lst = [x,y,w-x,h-y]

res = min(lst)

print(res)
