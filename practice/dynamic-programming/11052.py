# https://www.acmicpc.net/problem/11052
'''
1,2,3, .. n
p1,p2,p3 => 각 카드 팩의 가격
카드 N개를 최대 가격으로 사는것이 목표
단계별로 선택하는 문제
'''
n = int(input())
p = [0] + list(map(int,input().split()))
dp = [0]*(n+1) # dp[i] : i개의 카드팩을 살때 드는 최대 가격

for i in range(1,n+1): # 1개부터 n개까지의 카드 구매
    # i개 이하의 카드팩으로만 조합 가능
    for j in range(1,i+1):
        # i-j개를 최대 가격으로 구매한 상태에서 j개짜리 카드팩을 구매하는 경우
        dp[i] = max(dp[i], dp[i-j] + p[j])

print(dp[n])