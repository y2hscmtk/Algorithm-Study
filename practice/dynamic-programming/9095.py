# https://www.acmicpc.net/problem/9095
'''
1을 더하는 경우, 2를 더하는 경우, 3을 더하는 경우 
=> 각각 이전 경우들의 합을 더해주면 됨
dp[i-1] + dp[i-2] + dp[i-3]
풀이 참조 : x
'''
T = int(input())
# n은 11 이하의 양수 -> 미리 11까지 기록해두고 사용
dp = [0] * 12
dp[0],dp[1],dp[2] = 1,1,2
for i in range(3,12):
    #       +1 경우   +2 경우    +3 경우
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])    