
def FindNumber():
    num = str(input("請輸入三位數數字"))
    list1 = []
    list1 = []
    for i in num:
        list1.append(i)

    list1.sort()
    print(list1)

    list1.reverse()
    print(list1)
    print("Diff =", int(list1[0])-int(list1[2]))

FindNumber()






