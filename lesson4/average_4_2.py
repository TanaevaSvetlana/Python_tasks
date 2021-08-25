num = float(input('Введите температуру воздуха: '))
count = 1
total = num
while num >= -300:
    num = float(input())
    if num < -300:
        break
    else:
        total += num
        count += 1
print(total/count)
