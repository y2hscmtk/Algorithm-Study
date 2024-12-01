# https://www.acmicpc.net/problem/12865
'''
<풀이 참조>
각 물건을 담을것인지, 담지 않을 것인지 결정
담는 경우 : 해당 물건의 무게를 담지 않는 시점에서의 최대값 + 현재 물건의 가치
담지 않는 경우 : 이전까지의 최대 가치 
물건을 담는 경우는 해당 물건을 담아도 무게가 남는 경우에 해당
      -> 물건의 가치
물건들
...
..
.
'''
import sys
input = sys.stdin.readline
N, K = map(int,input().split())
data = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)] 
for i in range(1,N+1): # 각 물건들에 대하여
    for w in range(1,K+1): # 담을 수 있는 최대 가치에 대하여
        weight,value = data[i] # 해당 물건의 무게, 가치
        # 해당 물건을 담을 수 있는지 확인
        if weight <= w: # 담을 수 있다면
            #          물건을 담거나,       담지 않거나
            dp[i][w] = max(dp[i-1][w-weight] + value, dp[i-1][w])
        else: # 담을 수 없는 경우, 이전의 최대값으로 할당
            dp[i][w] = dp[i-1][w]

print(dp[N][K])