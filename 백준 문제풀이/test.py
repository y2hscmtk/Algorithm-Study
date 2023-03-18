# 테스트 케이스의 수
t = int(input())

dp = [0]*10001  # p는 최대 10,000

# 피보나치 수의 기본적인 수는 미리 기록
dp[0] = 0
dp[1] = 1

# 함수 호출전에 미리 메모이제이션
for j in range(2, 10001):
    dp[j] = dp[j-1] + dp[j-2]

# t만큼 반복
for i in range(1, t+1):
    p, q = map(int, input().split())
    print("Case #"+str(i)+":", dp[p] % q)
