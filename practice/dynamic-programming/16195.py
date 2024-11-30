# https://www.acmicpc.net/problem/15992
'''
dp[i][m] = 정수 i를 m개의 1,2,3을 사용하여 나타내는 방법
dp[i][m] = dp[i-1][m-1] + dp[i-2][m-1] + dp[i-3][m-1]
'''
dp = [[0]*1001 for _ in range(1001)] # n,m <= 1000
dp[1][1],dp[2][1],dp[3][1] = 1,1,1
for i in range(1,1001):
    for j in range(2,1001): # 1,2,3을 제외한 나머지는 1,2,3의 조합으로 구성되므로 2개부터 시작
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % 1000000009

for _ in range(int(input())):
    n,m = map(int,input().split())
    # m개 이하로 사용한 모든 경우 반환
    print(sum(dp[n][:m+1])%1000000009)
