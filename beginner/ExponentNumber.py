def exponentiation(n, e):
    ret = 1

    if n == 1:
        return 1

    if n == 0:
        return 0

    if e == 0:
        return 1

    for _ in range(e):
        ret *= n
    return ret
