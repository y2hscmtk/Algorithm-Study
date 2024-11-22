# https://www.acmicpc.net/problem/1932
N = int(input())
point = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    if i == 0:
        dp[0][0] = point[0][0]
    elif i == 1:
        dp[1][0] = dp[0][0] + point[1][0]
        dp[1][1] = dp[0][0] + point[1][1]
    else:
        for j in range(i+1):
            # 해당 칸에 도달하는 경우 양 대각선 중 한 경우 + 현재 값
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + point[i][j]

print(max(dp[N-1]))