letter = input()
string = input()

word_list = string.split()

for word in word_list:
    if letter.lower() in word or letter.upper() in word:
        print(word)
