# 최대 동전 거슬러주기
'''
dp[i] : i번째 동전을 선택할 때 최대로 사용한 동전의 개수
'''
N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp = [-1]*(M+1)
dp[0] = 0 # 초기값 설정

for i in range(1,M+1):
    # 어떤 동전을 추가로 사용할 것인지
    for cost in coin:
        if i-cost >= 0 and dp[i-cost] != -1:
            # 이전 상황 vs cost를 추가하기 전 상황 + cost를 추가하는 상황
            dp[i] = max(dp[i],dp[i-cost] + 1)

print(dp[M])