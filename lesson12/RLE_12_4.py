string = input()
count = 1

for i in range(len(string)):
     if i + 1 == len(string):
         print(count, string[i])
     elif string[i] == string[i + 1]:
        count += 1
     elif string[i] != string[i + 1]:
        print(count, string[i])
        count = 1

