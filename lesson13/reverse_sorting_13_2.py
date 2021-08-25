n = int(input())
revers = []

for i in range(n):
    revers.append(int(input()))
for i in range(n - 1):
    for j in range(n - 1 - i):
        if revers[j] < revers[j + 1]:
            revers[j], revers[j + 1] = revers[j + 1], revers[j]

print(*revers, sep='\n')
