# https://www.acmicpc.net/problem/1149
'''
선택 가능한 2개의 값 중 최소값 + 현재 칸의 값
'''
N = int(input())
dp = [[0]*3 for _ in range(N)]

cost = [list(map(int,input().split())) for _ in range(N)]

dp[0] = cost[0] # 초기값 설정

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + cost[i][2]

print(min(dp[N-1]))