# https://www.acmicpc.net/problem/17404
'''
점화식으로 구현
1. 1번 집의 색상 먼저 결정
2. 1번 집 이후의 집에 대해서 탐색 수행
'''
INF = float('inf')
n = int(input())
cost = [list(map(int,input().split())) for _ in range(n)]
min_cost = INF
# 1번 집 먼저 선택
for i in range(3):
    # dp 테이블 초기화
    dp = [[INF]*3 for _ in range(n)]
    dp[0][i] = cost[0][i] # 첫번째 집 선택
    # 1번 집 이후의 집 선택 -> 이전에 고른 집은 선택할 수 없음
    for j in range(1,n):
        # j번째 집의 색상을 결정하는 과정에서
        # 빨강색(0)을 선택하려면, 이전에 초록,파랑 선택한 상황 중 최소값으로 선택
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost[j][0]
        # 초록색(1)을 선택하려면, 이전에 빨강,파랑 선택한 상황 중 최소값으로 선택
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + cost[j][1]
        # 파란색(2)을 선택하려면, 이전에 빨강,초록 선택한 상황 중 최소값으로 선택
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + cost[j][2]
    
    # 가장 최소가 되는 경우 확인
    temp_min_cost = INF
    for k in range(3):
        if k == i:
            continue # 처음 선택한 집과 같은 경우는 무시
        temp_min_cost = min(temp_min_cost, dp[n-1][k])
    
    min_cost = min(min_cost,temp_min_cost)

print(min_cost)