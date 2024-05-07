# https://www.acmicpc.net/problem/1110
n = input()  # 숫자를 문자열로 입력받기
check = int(n) # 원본 저장
count = 1
while True:
    if len(n) == 1:
        n = '0' + n
    n = n[-1]+str(int(n[0])+int(n[-1]))[-1]
    if int(n) == check:
        break
    count += 1
print(count)
