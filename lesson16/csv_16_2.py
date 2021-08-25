string_list = []

for _ in range(int(input())):
    string_list.append(input().split(','))

for _ in range(int(input())):
    string_num, word_num = [int(i) for i in input().split(',')]
    print(string_list[string_num][word_num])
