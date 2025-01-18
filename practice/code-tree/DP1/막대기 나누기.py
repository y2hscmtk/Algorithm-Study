# 막대기 나누기
'''
dp[i] : 길이 i에서 얻을 수 있는 최대 이익

현재 길이 j에서 잘라서 팔 수 있는 모든 막대의 이익 중 최대가 되는 경우를 계산
''' 
# O(n^2 + n)
n = int(input())
profits = [0] + list(map(int,input().split()))

dp = [0]*(n+1)

for i in range(1,n+1): # 현재 길이 i에 대해서
    for j in range(1,i+1): # 현재 길이보다 작거나 같은 길이의 막대로 나누는 경우 생각
        dp[i] = max(dp[i], dp[i-j] + profits[j])

ans = 0
for i in range(n+1):
    ans = max(ans,dp[i])

print(ans)
    
