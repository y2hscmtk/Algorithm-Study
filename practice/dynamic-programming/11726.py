# https://www.acmicpc.net/problem/2579
n = int(input())
dp = [0]*1001
dp[1],dp[2] = 1,2 # dp[i] : 2*i 블록을 만들 수 있는 조합
for i in range(3,n+1):
    #  1칸 블록 추가  2칸 블록 추가
    dp[i] = dp[i-1]%10007 + dp[i-2]%10007

print(dp[n]%10007)