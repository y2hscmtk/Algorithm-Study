n = int(input())

dp = [[0] for i in range(n+1)]
#메모이제이션
dp[1],dp[2] = 1,1
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n],n-2)
