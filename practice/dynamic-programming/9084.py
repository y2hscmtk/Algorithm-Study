# https://www.acmicpc.net/problem/9084
'''
풀이참조 : x
dp[i][j] : i번째 동전까지 사용하여 금액 j를 표현하는 방법의 개수

i번째 동전을 사용하는 경우 + 사용하지 않는 경우
dp[i][j-value[i]] + dp[i-1][j]
'''
for _ in range(int(input())):
    N = int(input())
    values = list(map(int,input().split()))
    M = int(input())
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1,N+1):
        value = values[i-1]
        for k in range(1,M+1):
            # 해당 동전의 가치를 더해서 목표 금액 k를 만들수 있는지 없는지 파악
            if value <= k:
                dp[i][k] = dp[i-1][k] + dp[i][k-value]
                if value == k:
                    dp[i][k] += 1 # 금액과 일치하는 경우, value만을 사용하여 k원 표현 가능
            else: # 동전의 가치를 더할 수 없는 경우, 이전 가치
                dp[i][k] = dp[i-1][k] # i-1번째 동전까지 사용했을 때 k를 만들 수 있는 경우의 수
    print(dp[N][M])