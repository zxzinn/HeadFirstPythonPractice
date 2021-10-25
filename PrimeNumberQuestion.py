
#不使用def含式的原因是因為回傳的值的類型會是"NoneType"，此類型無法做任何處理 例如取長度len(),個數size()

while (True):

    i = int(input())
    #取小於i的所有質數

    PrimeList = []
    # 此空List拿來存所取範圍的所有質數


    for i in range(2, i+1):
        #右邊取i+1的原因是因為(2,9)只會取(2到8)，不會取9，類似微積分的(]，所以要取到i+1才會包含數字，否則當i為2，此程式不會有值


         for j in range(2, i):

             if i % j == 0:
                 break
         #2到j若全部都無法被i整除，則此樹為質數，將i加入列表，並且尋找下一個質數i


         else:
             PrimeList.append(str(i))# 將質數加入質數列

    print(PrimeList)


    print("在2到", i, "之間所有整數質數的數量為", len(PrimeList))
    # 若要取在i+1內所有質數的數量 只要將PrimeList的長度print出來






