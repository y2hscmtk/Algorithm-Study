# https://www.acmicpc.net/problem/2775
'''
0층 i호에는 i명 거주
a층 b호는 a-1층 1호부터 b호까지의 사람 거주 가능
k층에 n호에는 몇 명이 살고 있는지 출력
1 ≤ k, n ≤ 14
'''
dp = [[0 for _ in range(15)] for _ in range(15)] # 최대 14층 14호
# dp[a][b] => a층 b호에 거주중인 사람의 수
for i in range(15):
    dp[0][i] = i # 0층 i호에는 i명 거주

for i in range(1,15):
    for j in range(1,15):
        dp[i][j] = sum(dp[i-1][1:j+1]) # 거주자 수 사전 계산

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(dp[k][n])