def returnDivisibleNums(n):
    res = []
    for i in range(n):
        if i % 3 == 0 and i % 5 != 0:
            res.append(i)
        elif i % 5 == 0 and i % 3 != 0:
            res.append(i)
    return res
