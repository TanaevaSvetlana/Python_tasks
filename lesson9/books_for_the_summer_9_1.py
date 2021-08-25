m, n = int(input()), int(input())
home_library = set()

for _ in range(m):
    home_library.add(input())
for _ in range(n):
    book = input()
    if book in home_library:
        print('YES')
    else:
        print('NO')
