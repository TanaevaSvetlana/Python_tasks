n = int(input())
namesakes = set()
total = set()

for _ in range(n):
    surname = input()
    if surname in total:
        namesakes.add(surname)
    else:
        total.add(surname)

diff = total - namesakes
count = n - len(diff)

print(count)
