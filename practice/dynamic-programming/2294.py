# https://www.acmicpc.net/problem/2294
'''
dp 테이블 1개 사용
각 동전에 대해서 해당 동전을 사용하는 경우, 사용하지 않는 경우를 비교 후 갱신
'''
n, k = map(int,input().split())
coines = []
for i in range(n):
    coines.append(int(input()))

dp = [float('inf')] * (k+1) # dp[i]; i원을 만드는데 필요한 동전 조합의 최소 개수
dp[0] = 0 # 0원을 만드는데는 어떤 동전이든 0개로 가능
# 각 동전에 대해서
for coin in coines:
    for j in range(1,k+1):
        # 동전의 가치가 적용가능한지 확인
        if j-coin >= 0:
            #       해당 동전을 사용하지 않는 경우, 사용하는 경우
            dp[j] = min(dp[j],dp[j-coin]+1) # +1 현재 동전의 개수

# k원을 만들 수 없는 경우 -1, 만들 수 있는 경우 dp[k]
print(-1) if dp[k] == float('inf') else print(dp[k])