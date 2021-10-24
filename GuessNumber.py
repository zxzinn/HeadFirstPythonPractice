
guessnumber = 5
goalnumber = 50
i = 0
while i <= (guessnumber-1):
    guess = int(input("請輸入數字"))
    if guess < goalnumber:
        print("數字太小了")
    elif guess > goalnumber:
        print("數字太大了")
    else:
        print("答對")
        break
    i += 1
print("遊戲結束")