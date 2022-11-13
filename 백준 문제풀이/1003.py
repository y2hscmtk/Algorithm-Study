# https://www.acmicpc.net/problem/1003

# 피보나치 함수
def fibonacci(n):
    if n == 0:
        print("0")
        return 0
    elif n == 1:
        print("1")
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
