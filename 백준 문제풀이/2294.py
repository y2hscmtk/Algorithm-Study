# https://www.acmicpc.net/problem/2294
'''
a,b,c원의 동전이 있다고 가정할때
dp[i] = i원을 만들기 위해 선택해야 하는 동전의 최소 개수
dp[i] = min(dp[i-a],dp[i-b],dp[i-c]) + 1, a원,b원,c원 중 1개를 고르는건 정해져있고 
현재 금액을 고르기 전 최소 개수 + 현재 금액을 하면 됨
'''
import sys
n,k = map(int,input().split())
cost = [int(input()) for _ in range(n)]
dp = [sys.maxsize]*(k+1)
dp[0] = 0 # 초기값 설정
for i in range(1,k+1): # k원 만드는데 필요한 최소 금액
    for c in cost:
        if i-c >= 0 and dp[i-c]!=sys.maxsize: # 배열의 범위를 초과하지 않는 선 + 만들 수 있는 경우에 대해서
            # 현재 동전을 선택함으로서 현재 금액을 만들 수 있다면 업데이트
            dp[i] = min(dp[i],dp[i-c]+1) # dp[i-c]를 만들 수 있으므로, dp[i]는 dp[i-c]에 c원 동전 1개를 더한 값
print(dp[k] if dp[k]!=sys.maxsize else -1)
