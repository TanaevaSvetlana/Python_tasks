number = int(input())

for _ in range(number):
    string = input()
    if string[:2] == '%%':
        print(string[2:])
    elif string[:4] == '####':
        continue
    else:
        print(string)
