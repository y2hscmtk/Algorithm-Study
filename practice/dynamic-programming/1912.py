# https://www.acmicpc.net/problem/1912
'''
수를 선택하거나, 선택하지 않거나 2가지 경우의 수로 갈림
이전 수들까지의 가장 큰 합 + 현재 항을 더하는 경우, 더하지 않는 경우
연속된 수를 선택해야 하며, 한 개 이상의 수를 선택해야함
'''
n = int(input())
num = list(map(int,input().split()))
dp = [n for n in num] # dp[i] ; i번째 요소까지의 수들의 가장 큰 합
for i in range(1,n):
    # 이전 수를 선택함으로서, 합이 더 커진다면 더한다.
    # 합이 더 커지지 않는다면 더하지 않는다.
    if dp[i-1] + num[i] > dp[i]:
        dp[i] = dp[i-1] + num[i]
print(max(dp))