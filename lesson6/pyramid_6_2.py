space = int(input()) - 1
count = 1
while space >= 0:
    print(' ' * space + '*' * count)
    space -= 1
    count += 2
