# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

numbers = list(map(int,input().split()))

dp = [0]*(n+1) # 구간 합을 저장하기 위함ss
dp[0] = 0

# 누적합 저장
for i in range(n):
    dp[i+1] = dp[i] + numbers[i]

for _ in range(m):
    start,end = map(int,input().split())
    print(dp[end]-dp[start-1])
