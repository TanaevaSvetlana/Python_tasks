num1, num2, sign = float(input()), float(input()), input()
if sign == '+':
    print(num1 + num2)
elif sign == '-':
    print(num1 - num2)
elif sign == '*':
    print(num1 * num2)
elif sign == '/':
    if num2 != 0:
        print(num1/num2)
    else:
        print('888888')
else:
    print('888888')
