import sys

for i in sys.stdin:
    i = int(i)
    1 <= i <= 20
    for x in sys.stdin:

        x = x.split()
        x.sort()
        x.sort(key = len)
        if x[0] == '100':
            del x[0]
            x.append('100')
        print(' '.join(x))
        Z = list(map(int, x))

        Alist = []
        Blist = []
        break

    Z.reverse()
    for A in Z:
        if A < 60:
            Alist.append(A)
    if len(Alist) == 0:
        print('best case')
    else:
        print(Alist[0])

    Z.reverse()

    for B in Z:
        if B >= 60:
            Blist.append(B)

    if len(Blist) == 0:
        print('worst case')
    else:
        print(Blist[0])