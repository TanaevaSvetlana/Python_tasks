column = int(input())
string = int(input())
for i in range(1, string + 1):
    for j in range(1, column + 1):
        value = j / i
        print('%.7f' % value, end=' ')
    print()
