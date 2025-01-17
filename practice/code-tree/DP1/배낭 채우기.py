# 배낭 채우기
'''
보석을 선택하는 경우, 선택하지 않는 경우

dp[i] 보석의 무게 합이 i일때의 최대 가치 라고 정의 할때,
j번째 보석의 무게가 w라면 - dp[i-w] 를 살피면 된다 -> w만큼의 무게를 추가할 수 있는 상황이므로
dp[i] = max(dp[i], dp[i-w] + value[j])
'''
N, M = map(int, input().split())
weight, value = zip(*[tuple(map(int, input().split())) for _ in range(N)])
weight, value = list(weight), list(value)

dp = [0]*(M+1)
dp[0] = 0

for j in range(N): # 각 보석은 한번씩만 사용할 수 있음
    w,v = weight[j],value[j]
    for i in range(M,-1,-1): # 각 무게
        if i-w >= 0: # 각 보석을 넣을 것인지, 넣지 않을 것인지 여부
            dp[i] = max(dp[i], dp[i-w] + v)

ans = 0
for i in range(M+1):
    ans = max(ans,dp[i])

print(ans)

