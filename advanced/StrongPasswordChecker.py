import sys


def strongPasswordChecker(s):
    if len(s) < 3:
        return 6-len(s)

    l, u, d = 1, 1, 1
    S = []
    for i in range(2):
        if 'a' <= s[i] <= 'z':
            l = 0
        elif 'A' <= s[i] <= 'Z':
            u = 0
        elif '0' <= s[i] <= '9':
            d = 0
        S.append(s[i])

    R = sys.maxsize

    def b(i, C, r, a):
        nonlocal s, S, R
        (l, u, d) = C
        if i == len(s):
            a = max(a, sum(C))
            if len(S) < 6:
                a = max(a, 6 - len(S))
            elif len(S) > 20:
                r += len(S) - 20
            R = min(R, r+a)
            return
        if s[i] == S[-1] == S[-2]:
            b(i+1, (l, u, d), r+1, a)  # removed

            S.append(None)
            # changed / appended if less than 6 symbols
            b(i+1, (l, u, d), r, a+1)
            S.pop()
        else:
            if 'a' <= s[i] <= 'z':
                l = 0
            elif 'A' <= s[i] <= 'Z':
                u = 0
            elif '0' <= s[i] <= '9':
                d = 0

            S.append(s[i])
            b(i+1, (l, u, d), r, a)  # added as is
            S.pop()

    b(2, (l, u, d), 0, 0)
    return R
