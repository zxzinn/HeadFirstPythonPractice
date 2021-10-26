
while True:
    i, j = map(int, input().split())
    # i,j表示所取數值範圍

    c, s = map(int, input().split())
    # c表示每行所會印出的數字量，s無意義

    count = 0
    # 創建一個計數器

    for x in range(i, j+1):
        # (i,j)在微積分上屬於(i,j]，所以取值要取(i,j+1)，否則j不會備取到

        if count == c-1:
            # 當計數器=每行的數字量時，印出那個數字(不印的畫會每行少一個數字，例如:1 2 3然後5 6 7，少了4)
            print("{:>3d}".format(x), end=" ")

            print("\n")
            #換行

            count = count - c + 1
            # 將計數器初始化
        else:
            print("{:>3d}".format(x), end=" ")
            # 正常打印流程

            # format的用法是  "{}".format() 其中{}的初始index是0，假設這樣使用 "{index[0]}{index[1]}".format(index[0],index[1])
            # format左邊括弧""內的{}內的index值可自訂，例如"{a}{b}".format(a = x,b = y)，當有指定名稱時，可不照順序，例如"{a}{b}".format(b = y,a = x)
            # format()的括弧()內要輸入index值和代數，或者字串

            count += 1
            #計數器+1



