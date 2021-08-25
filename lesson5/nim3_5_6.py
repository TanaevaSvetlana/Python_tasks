first = int(input('Начальное количество камней в первой куче: '))
second = int(input('Начальное количество камней во второй куче: '))
third = int(input('Начальное количество камней в третьей куче: '))
while first != 0 or second != 0 or third != 0:
    n = int(input('Номер кучи: '))
    c = int(input('Количество забираемых камней: '))
    if n == 1:
        first -= c
        print(first, second, third)
    elif n == 2:
        second -= c
        print(first, second, third)
    else:
        third -= c
        print(first, second, third)
