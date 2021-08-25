num_str = input('Введите число: ')
num = int(num_str)
first_digit = num // 100
second_digit = (num // 10) % 10
third_digit = num % 10
max_ = max(first_digit, second_digit, third_digit)
min_ = min(first_digit, second_digit, third_digit)
if (max_ + min_)/2 == (first_digit+second_digit+third_digit - min_ - max_):
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')
