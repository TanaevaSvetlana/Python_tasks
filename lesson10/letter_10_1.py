message = input()
number = int(input())

if number > 0 and number <= len(message):
    print(message[number - 1])
else:
    print('ОШИБКА')
