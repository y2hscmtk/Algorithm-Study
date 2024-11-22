# https://www.acmicpc.net/problem/2579
'''
규칙에 따라 마지막 칸에 도달하는 방법은
1. n-1칸에서 1칸 올라오는 방법
2. n-2칸에서 2칸 올라오는 방법
최대값을 만드는 것이 목표이기 때문에, dp[i] -> i번째 칸에 도달시점에서 최대 점수 합
dp[n] = max(dp[n-2], dp[n-3] + point[n-1]) + point[n]
dp[n-2] => 2칸을 밟고 올라오는 경우에 해당
dp[n-3] + point[n-1] => 3칸전 + 1칸전 칸을 밟고 올라오는 경우에 해당
'''
N = int(input())
dp = [0]*(301) # 계단은 최대 300개
point = [0]
for _ in range(N):
    point.append(int(input()))

for i in range(N+1):
    if i < 2:
        dp[i] = point[i]
    else:
        # 1칸 이전 칸, 2칸 이전칸 둘 중 최대 값 + 현재 포인트
        dp[i] = max(dp[i-2], dp[i-3] + point[i-1]) + point[i]

print(dp[N])