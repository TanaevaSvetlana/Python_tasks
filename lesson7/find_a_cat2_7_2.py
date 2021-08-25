s = input()
line_number = 0
i = 0
while s != 'СТОП':
    s = input()
    i += 1
    if 'кот' in s or 'Кот' in s:
        line_number = i+1
if line_number != 0:
    print(line_number)
else:
    print(-1)
