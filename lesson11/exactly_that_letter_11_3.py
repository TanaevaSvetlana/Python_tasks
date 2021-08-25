string, number, letter = input(), int(input()), input()

if number <= len(string) and number > 0 and len(letter) == 1:
    if string[number - 1] == letter:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('ОШИБКА')
