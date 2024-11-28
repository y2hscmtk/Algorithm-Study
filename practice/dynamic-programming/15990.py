# https://www.acmicpc.net/problem/15990
'''
같은 수를 두 번 이상 연속해서 사용하면 안 된다.
'''
import sys
input = sys.stdin.readline

dp = [[0 for _ in range(100001)] for _ in range(4)]

# 현재수 i, 만들고 싶은수 m
def dfs(i,n):
    # 이미 알고있는 수라면 반환
    if dp[i][n] != 0:
        return dp[i][n]
    # 마지막에 도달하였다면 반환
    if n == 0: # 더이상 필요한 수가 없는 경우, 즉 끝에 해당
        dp[i][n] = 1
        return dp[i][n]
    # 사용가능한 수는 1,2,3
    for k in range(1,4):
        if k != i: # 이전에 사용한 수를 사용할 수는 없음
            # i를 보유하고 있는 상태에서 n을 만들고 싶고 k를 추가로 사용할 것
            # 현재 수는 i, 추가로 필요한 수는 n
            if k <= n: # k를 추가로 더하는 결정이 목표했던 수를 초과하지 않아야함
                dp[i][n] += dfs(k,n-k)
    return dp[i][n]

for _ in range(int(input())):
    n = int(input())
    result = 0
    for i in range(1,4):
        result += dfs(i,n-i)%1000000009
    print(result)