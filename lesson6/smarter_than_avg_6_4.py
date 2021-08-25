count = int(input())
total_iq = 0
avg_iq = 0
for i in range(1, count+1):
    iq = int(input())
    if iq == avg_iq or i == 1:
        print('0')
    elif iq > avg_iq:
        print('>')
    else:
        print('<')
    total_iq += iq
    avg_iq = total_iq/i

