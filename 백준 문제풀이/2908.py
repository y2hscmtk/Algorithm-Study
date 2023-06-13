# https://www.acmicpc.net/problem/2908

a, b = input().split()

# 1. 문자열 뒤집기
a = a[::-1]
b = b[::-1]

# 2. 대소비교
if int(a)>int(b):
    print(a)
else:
    print(b)
