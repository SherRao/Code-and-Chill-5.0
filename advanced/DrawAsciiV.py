def drawV(n):
    for i in range(n, 0, -1):
        for _ in range(n - i):
            print(' ', end='')

        print('*', end='')
        for _ in range(1, 2*i - 2):
            print(' ', end='')

        if (i != 1):
            print('*')
        else:
            print()
