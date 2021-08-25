num = int(input('Введите число: '))
count = 0
if num == 0:
    print('error')
else:
    while num != 1:
        if num % 2 != 0:
            print('НЕТ')
            break
        num //= 2
        count += 1
    else:
        print(count)
