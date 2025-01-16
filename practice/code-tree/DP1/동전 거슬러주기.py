# 아이템을 적절히 고르는 문제
# 동전 거슬러주기
'''
특정 값 i를 선택하기 이전의 상황들 중 최대값 + 1

같은 동전을 여러번 사용하여 거슬러 줄 수 있다
'''
N,M = map(int,input().split())
coin = list(map(int,input().split()))
dp = [float('inf')]*(M+1)
dp[0] = 0
for i in range(1,M+1):
    # i원을 거슬러 주는 방법은 - 동전을 최소한으로 사용하여 거슬러 주고 싶다.
    # 동전의 종류가 1,4,5원일 때
    # i-1 원까지 거슬러 준 상태에서 1원을 거슬러 주는 경우
    # i-4 원까지 거슬러 준 상태에서 4원을 거슬러 주는 경우
    # i-5 원까지 거슬러 준 상태에서 5원을 거슬러 주는 경우
    # min(dp[i-1],dp[i-4],dp[i-5]) + 1 
    temp = float('inf')
    for cost in coin:
        if i-cost >= 0:
            temp = min(temp,dp[i-cost]) # 더 작은 경우 찾기
    if temp == float('inf'):
        continue
    dp[i] = min(dp[i],temp + 1)

if dp[M] == float('inf'):
    print(-1)
else:
    print(dp[M])
