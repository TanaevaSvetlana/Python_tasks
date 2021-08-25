login = input('Введите логин: ')
mail = input('Введите адрес электронной почты: ')
if '@' not in login and '@' in mail:
    print('OK')
elif '@' in login:
    print('Некорректный логин')
elif '@' not in mail:
    print('Некорректный адрес')
else:
    print('Error')
