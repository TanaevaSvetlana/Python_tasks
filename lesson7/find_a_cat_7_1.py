n = int(input())
flag = False
for i in range(n):
    s = input()
    if 'кот' in s or 'Кот' in s:
        flag = True
if flag:
    print('МЯУ')
else:
    print('НЕТ')
