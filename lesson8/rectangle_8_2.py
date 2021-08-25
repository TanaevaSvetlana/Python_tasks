n = int(input())
m = int(input())
symbol = input()
for i in range(m):
    if i == 0 or i == m - 1:
        for j in range(n):
            print(symbol, end='')
    else:
        print(symbol + ' ' * (n - 2) + symbol, end='')
    print()
