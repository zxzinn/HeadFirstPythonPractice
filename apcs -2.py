import sys

for RCM in sys.stdin:
    R, C, M = RCM.split()
    '''
    RCM
    '''

    x = [[0, 0],
         [0, 0],
         [0, 0]
         ]

    '''
    1 1
    3 1
    1 2
    '''
    for i in range(3):
        j = 0
        A0, A1 = input().split()
        x[i][j] = int(A0)
        x[i][j + 1] = int(A1)
    print(x)

    result = [[0, 0, 0],
              [0, 0, 0]]
    if len(x) == 3:
    for a in range(3):
        for b in range(2):
            result[b][a] = x[a][b]
    print(result)
