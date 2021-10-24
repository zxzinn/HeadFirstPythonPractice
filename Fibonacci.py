def Fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


k = int(input())
print(Fibonacci(k))


print('1'.ljust(2), end='')
print('8'.ljust(2), end='')
print('19'.ljust(2), end='')