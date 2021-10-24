

def graph1():
    for i in range(6):
        print(i*'*')

graph1()


def graph2():
    for i in range(6):
        print(' '*(5-i), ' *'*i, ' '*(5-i))
    for j in range(5):
        print(' ' + ' ' * j, ' *' * (4-j), ' ' * j)

graph2()


def graph3():
    list1 = []
    for i in range(1, 6):
        list1.append(i)
    for j in range(5):
        print(str(list1[j]) * int(list1[j]))

graph3()


def graph4():
    for i in range(-4, 5):
        for j in range(-4, 5):
            if (abs(i) > abs(j)):
                print(abs(i)+1, end='')
            else:
                print(abs(j)+1, end='')
        print()

graph4()


def graph5():
    list1 = ['A', 'B', 'C', 'D', 'E']
    for i in range(5):
        print(list1[i]*(i+1))

graph5()


def graph6():
    list1 = ['A', 'B', 'C', 'D', 'E']
    for i in range(5):
        print(list1[i])
    print(''.join(list1))

graph6()


def graph7():
    for i in range(1, 5):
        for j in range(1, 4):
            for k in range(i):
                print(j*'*'+(3-j)*' ', end='')
            print()

graph7()