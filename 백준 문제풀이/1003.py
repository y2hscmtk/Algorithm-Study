# https://www.acmicpc.net/problem/1003

# 피보나치 함수

'''
def fibonacci(n):
    global count0, count1, dp
    if dp[n] != 0:  # dp에 값이 저장되어 있는 상태라면
        return dp[n]  # dp에 저장된 값을 리턴
    else:  # 새로운 인덱스의 데이터라면 값 저장
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
새롭게 작성하거나, 혹은 반복문을 이용하여 값을 할당하는 방법을 고안할것
'''


count0, count1 = 0, 0  # fibo(0)과 fibo(1)의 출력횟수를 카운트한다.
dp = [0 for _ in range(40)]  # 40의 dp공간을 마련
# 아래는 이미 결과가 정해진 값이므로 저장
dp[0] = 0
dp[1] = 1


t = int(input())
for _ in range(t):
    n = int(input())  # n은 40보다 작거나 같은 자연수이므로 크기 40의 dp공간을 만들면 될것
    fibonacci(n)
    print(count0, count1)
    count0, count1 = 0, 0
