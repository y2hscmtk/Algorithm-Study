# https://www.acmicpc.net/problem/15988
'''
n은 양수이며 1,000,000보다 작거나 같다.
1,000,000,009로 나눈 나머지를 출력한다.
'''
dp = [0]*1_000_001
dp[0],dp[1],dp[2] = 1,1,2
for i in range(3,1_000_001):
    #       +1 경우   +2 경우    +3 경우
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])    