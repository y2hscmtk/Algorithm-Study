# https://www.acmicpc.net/problem/1003

# 피보나치 함수
def fibonacci(n):
    global count0, count1
    if n == 0:
        count0 += 1
        return 0
    elif n == 1:
        count1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


count0, count1 = 0, 0  # fibo(0)과 fibo(1)의 출력횟수를 카운트한다.
t = int(input())
for _ in range(t):
    n = int(input())
    fibonacci(n)
    print(count0, count1)
    count0, count1 = 0, 0
