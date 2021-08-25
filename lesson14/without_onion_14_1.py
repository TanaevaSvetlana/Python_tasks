n = int(input())
recipe = list()

for _ in range(n):
    strings = input()
    if 'лук' in strings:
        continue
    else:
        recipe.append(strings)

print(*recipe, sep=', ')
