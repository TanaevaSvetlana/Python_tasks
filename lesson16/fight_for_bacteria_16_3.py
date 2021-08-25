n = int(input())

box = [[int(input()) for x in range(n)] for y in range(n)]

k = int(input())
for _ in range(k):
    y = int(input())
    x = int(input())
    box[x][y] -= 8
    if x - 1 >= 0 and y - 1 >= 0:
        box[x - 1][y - 1] -= 4
    if x - 1 >= 0 and y + 1 <= n - 1:
        box[x - 1][y + 1] -= 4
    if x + 1 <= n - 1 and y - 1 >= 0:
        box[x + 1][y - 1] -= 4
    if x + 1 <= n - 1 and y + 1 <= n - 1:
        box[x + 1][y + 1] -= 4
    if x + 1 <= n - 1:
        box[x + 1][y] -= 4
    if y + 1 <= n - 1:
        box[x][y + 1] -= 4
    if x - 1 >= 0:
        box[x - 1][y] -= 4
    if y - 1 >= 0:
        box[x][y - 1] -= 4

for i in range(n):
    for j in range(n):
        if box[i][j] < 0:
            box[i][j] = 0

for i in range(n):
    print(*box[i], sep=' ')

