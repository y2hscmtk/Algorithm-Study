# 최대 증가 부분 수열
'''
원소들 중 임의의 값을 골라 나열했을 때, 원소들이 계속 증가하도록 수열을 만들때 가장 긴 증가하는 수열의 길이
dp[i] : i번째 원소까지 도달하였을 때의 최장 길이
'''
n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n # 자기 자신은 무조건 선택 가능

for i in range(1,n):
    for j in range(i-1,-1,-1):
        # 해당 원소가 현재 원소보다 작은지 확인
        if arr[j] < arr[i]:
            # j번째 원소까지 선택 + 현재 값 선택
            dp[i] = max(dp[i],dp[j] + 1) # 최대값 갱신

# dp테이블의 최대값이 정답
ans = 1
for i in range(n):
    ans = max(ans,dp[i])

print(ans)