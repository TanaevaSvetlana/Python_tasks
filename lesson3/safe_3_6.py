code = int(input('Введите код доступа: '))
first_digit = code // 100
second_digit = (code // 10) % 10
third_digit = code % 10
if first_digit != second_digit and first_digit != third_digit and second_digit != third_digit:
    print('OK')
elif first_digit == second_digit and first_digit == third_digit:
    print('В числе все цифры одинаковые')
elif first_digit == second_digit or first_digit == third_digit or second_digit == third_digit:
    print('В числе две одинаковые цифры')
