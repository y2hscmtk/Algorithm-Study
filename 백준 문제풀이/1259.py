# https://www.acmicpc.net/submit/1259
while True:
    number = input()
    if number == '0':
        break
    flag = True
    for i in range(0,len(number)//2):
        if number[i] != number[len(number)-i-1]:
            flag = False
            break
    print("yes" if flag else "no")