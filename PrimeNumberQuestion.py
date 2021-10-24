

def FindPrimeNumber():
    PrimeList = [] # 此空List拿來存所取範圍的所有質數
    i = int(input()) # 要取的數
    for i in range(2, i):

         for j in range(2, i):
             if i % j == 0:
                 break
         #2到j若全部都無法被i整除，則此樹為質數，將i加入列表，並且尋找下一個質數i


         else:
             PrimeList.append(i)# 將質數加入質數列

    print(PrimeList)

FindPrimeNumber()


