# dictionary
dict1 = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 34, "J": 18, "K": 19,
         "L": 20, "M": 21, "N": 22, "O": 35, "P": 23, "Q": 24, "R": 25, "S": 26, "T": 27, "U": 28, "V": 29,
         "W": 32, "X": 30, "Y": 31, "Z": 33}


ID = str(input())


# 數字加總為10的倍數即屬正確
sum = 0
n = int(dict1[ID[0:1]])
sum = n//10+(n % 10)*9

# 身分證由dict1英轉數
# N1 N2 = 英轉數二碼
# N1 + 9N2+ 8N3+ 7N4+ 6N5+ 5N6+ 4N7+ 3N8+ 2N9+ N10+ N11
# 若此組數字可被10整除，即此身分證為可用身分證
for i in range(1, 8+1):
    sum = sum + (9-i) * int(ID[i:i+1])
check = int(ID[9:10])
if (((sum+check)%10) == 0):
    print(ID, '的身分證號碼正確')
else:
    print(ID, '的身分證號碼不正確')

print('身分證的檢查碼=', check)