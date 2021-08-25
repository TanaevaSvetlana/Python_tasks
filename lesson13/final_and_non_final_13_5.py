import math

n = int(input())
result = []

for i in range(n):
    result.append((input(), int(input())))

for i in range(len(result) - 1):
    for j in range(len(result) - i - 1):
        if result[j][1] < result[j + 1][1]:
            result[j], result[j + 1] = result[j + 1], result[j]

middle = math.ceil(len(result) / 2)
final = result[:middle]
others = result[middle:]

for i in range(len(final) - 1):
    for j in range(len(final) - i - 1):
        if final[j] > final[j + 1]:
            final[j], final[j + 1] = final[j + 1], final[j]

for team in final:
    print(team[0])

for i in range(len(others) - 1):
    for j in range(len(others) - i - 1):
        if others[j] > others[j + 1]:
            others[j], others[j + 1] = others[j + 1], others[j]

for team in others:
    print(team[0])
