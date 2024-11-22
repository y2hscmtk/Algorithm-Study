# https://www.acmicpc.net/problem/2839
'''
현재 무게를 만들 때 가장 적은 개수의 봉지를 사용하는 방법
현재 무게 - 3, 현재 무게 - 5 를 만들었던 기록 + 1(3키로 혹은 5키로를 추가하여 만들 것이기 때문)
dp = [float('inf')]*(N+1); dp[i] => i키로를 만들때 사용되는 가장 적은 양의 설탕 무게 조합 
풀이 참조 : x
'''
N = int(input())
IMPOSSIBLE = float('inf')
dp = [IMPOSSIBLE]*(N+1)
# 현재 금액을 만들 수 없는 경우 -1을 출력
for i in range(3,N+1): # 3kg 이상부터 만들 수 있으므로
    if i == 3 or i == 5:
        dp[i] = 1
        continue
    last_min = min(dp[i-3], dp[i-5])
    if last_min != IMPOSSIBLE:
        dp[i] = last_min + 1

print(dp[N] if dp[N]!=IMPOSSIBLE else -1)