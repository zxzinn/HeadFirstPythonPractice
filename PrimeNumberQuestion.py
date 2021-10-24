

#不使用def含式的原因是因為回傳的值的類型會是"NoneType"，此類型無法做任何處理 例如取長度len(),個數size()

i = int(input())
#取小於i的所有質數
PrimeList = []
# 此空List拿來存所取範圍的所有質數

for i in range(1, i):

     for j in range(2, i):
         if i % j == 0:
             break
     #2到j若全部都無法被i整除，則此樹為質數，將i加入列表，並且尋找下一個質數i


     else:
         PrimeList.append(str(i))# 將質數加入質數列

print(PrimeList)


print("在i內所有質數的數量為", len(PrimeList))
# 若要取在i內所有質數的數量 只要將PrimeList的長度print出來






