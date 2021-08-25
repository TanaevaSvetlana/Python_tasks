sms = input('Введите сообщение: ')
total = len(sms)*40
print(f'Стоимость сообщения: {total // 100} р. {total % 100} коп.')
