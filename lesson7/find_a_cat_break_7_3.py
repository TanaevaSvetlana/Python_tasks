n = int(input())
flag = True
for i in range(n):
    s = input()
    if 'кот' in s or 'Кот' in s:
        flag = False
        print('МЯУ')
        break
if flag:
    print('НЕТ')
