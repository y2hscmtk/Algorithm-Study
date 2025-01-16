MOD = 10007

n = int(input())
dp = [0] * (n+1)

# 초기값 설정
dp[0] = 1  # 아무것도 선택하지 않는 방법

for i in range(1, n+1):
    if i >= 1:
        dp[i] = (dp[i] + dp[i-1]) % MOD
    if i >= 2:
        dp[i] = (dp[i] + dp[i-2]) % MOD
    if i >= 5:
        dp[i] = (dp[i] + dp[i-5]) % MOD

print(dp[n])
