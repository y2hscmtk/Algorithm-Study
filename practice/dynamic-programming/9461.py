# https://www.acmicpc.net/problem/9461
dp = [0]*(101) # (1 ≤ N ≤ 100)
# 초기값 설정
dp[1],dp[2],dp[3],dp[4],dp[5] = 1, 1, 1, 2, 2
for i in range(6,101):
    # dp[6] = dp[1] + dp[5]
    # dp[7] = dp[2] + dp[6] ...
    dp[i] = dp[i-5] + dp[i-1]

T = int(input())
for _ in range(T):
    print(dp[int(input())])