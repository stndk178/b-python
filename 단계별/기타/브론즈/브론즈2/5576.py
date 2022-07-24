
def my_sum():
    res = []
    for i in range(10):
        res.append(int(input()))

    res.sort()
    s = sum(res[7:10])
    return s

print(my_sum(),my_sum())
