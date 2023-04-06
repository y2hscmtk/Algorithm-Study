# https://www.acmicpc.net/problem/2553

n = int(input())

factorial = 1
for i in range(1, n+1):
    factorial *= i

factorial = str(factorial)  # 문자열 변환
# 정수 변환하여 뒤에서부터 0이 아닌 숫자 출력
for i in range(len(factorial)-1, -1, -1):
    if factorial[i] != '0':
        print(factorial[i])
        break
