# https://www.acmicpc.net/problem/11660
'''
(x1,y1)부터 (x2,y2)까지의 누적합
풀이 참조
https://sodehdt-ldkt.tistory.com/76
'''
N,M = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        #          왼쪽 줄       윗줄         중복 값         현재 값
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + data[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])