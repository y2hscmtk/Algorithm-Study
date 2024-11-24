# https://www.acmicpc.net/problem/15989
'''
앞자리가 1일때 3을 만드는 방법 dp[1][3]
1은 보유중이므로 1,2,3을 포함하여 2를 만들어야함
4를 만드는 방법 = dp[1][3] + dp[2][2] + dp[3][1]
<n을 만드는 방법>
dp[1][n-1] + dp[2][n-2] + dp[3][n-3]
가장 깊이 내려가는 경우는 모든 수를 1로 채우는 경우
'''
import sys
sys.setrecursionlimit(10001) # 모두 1인 경우
dp = [[0]*10001 for i in range(4)]
# 앞자리가 i이고 남은 자리수가 depth일때, n을 만드는 방법
def dfs(i,n):
    # i에서 n을 만드는 방법의 개수가 정의 되어 있다면 반환
    if dp[i][n] != 0:
        return dp[i][n]
    if n == 0: # 가장 끝에 도달하였을때, 0을 만드는 방법은 현재 수 그대로 1가지
        dp[i][n] = 1
        return dp[i][n]
    for k in range(3,0,-1):
        # 규칙을 만족시키기 위해 1,2,3중에 자기보다 작은 수만 더함
        # 1,2,3을 더함으로서 목적으로 했던 수보다 커지는 경우는 제외
        if k <= n and k <= i:
            dp[i][n] += dfs(k,n-k)
    return dp[i][n]


for _ in range(int(input())):
    n = int(input())
    for i in range(1,4):
        # dp[1][n] + dp[2][n] + dp[3][n]
        dp[i][n-i] = dfs(i,n-i)
    print(dp[1][n-1] + dp[2][n-2] + dp[3][n-3])