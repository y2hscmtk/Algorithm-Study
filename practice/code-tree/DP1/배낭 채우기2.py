N, M = map(int, input().split())
weight, value = zip(*[tuple(map(int, input().split())) for _ in range(N)])
weight, value = list(weight), list(value)

dp = [0]*(M+1)
dp[0] = 0

for i in range(1,M+1): # 현재 시점에서의 무게
    for j in range(N):
        w,v = weight[j],value[j]
        if i-w >= 0:
            # j번째 보석을 선택하는 경우와 선택하지 않는 경우
            dp[i] = max(dp[i], dp[i-w] + v) # 선택하는 경우, w무게를 고르지 않았던 시점에서 현재 가치를 더함

ans = 0
for i in range(M+1):
    ans = max(ans,dp[i])

print(ans)