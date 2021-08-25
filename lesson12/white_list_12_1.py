white_list, requests = list(), list()

for _ in range(int(input())):
    white_list.append(input())

for _ in range(int(input())):
    requests.append(input())

for request in requests:
    for permit in white_list:
        if permit == request:
            print(request)
