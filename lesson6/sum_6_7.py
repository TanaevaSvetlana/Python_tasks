n = int(input())
total = 0
for i in range(n):
    num = int(input())
    if i % 2 == 0:
        total += num
    else:
        total -= num
print(total)
