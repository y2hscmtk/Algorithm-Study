# https://www.acmicpc.net/problem/2293
'''
n가지 동전, 가치의 합이 k개가 되는 경우의 수
동전의 개수는 무제한
dp[i] : i원을 만들수 있는 동전 조합의 수
'''
n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)] # n가지 동전

dp = [0]*(k+1)
dp[0] = 1 # 0원은 무조건 만들 수 있음

# 동전을 하나씩 넣는다고 생각 - 매 수행에 대해서 동전을 추가한다면 중복 발생
for cost in coin:
    # i원을 완성할수 있는지 확인 - cost이후의 값에 대해서 확인해야 하므로 cost부터 시작
    for i in range(cost, k+1):
        dp[i] += dp[i-cost] # cost원을 추가함으로서 얻을 수 있는 경우의 수

# k원을 만들때 필요한 모든 경우의 수
print(dp[k])