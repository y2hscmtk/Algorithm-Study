# https://www.acmicpc.net/problem/17404
'''
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값
1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

가장 먼저 칠할 집의 색상을 고정시켜두고 dp를 구한다.
'''
import sys
input = sys.stdin.readline
N = int(input())
# 각각의 집을 칠하는데 드는 비용(arr[i][RGB] => i번째 집을 R,G,B로 칠하는데 드는 비용)
arr = [list(map(int,input().split())) for _ in range(N)]
INF,result = sys.maxsize,sys.maxsize
# 첫번째 집의 색상을 R,G,B 중 하나로 고른다
for i in range(3):
    dp = [[INF]*3 for _ in range(N)]
    # i색상을 가장 먼저 칠할 때, 0번째 집을 가장 작은 비용으로 지정
    dp[0][i] = arr[0][i]
    # 이후의 집들에 대해
    for j in range(1,N):
        # 빨간색을 선택할 경우, 이전 집은 빨간색이 아니면서 둘 중 최소값으로
        dp[j][0] = min(dp[j-1][1],dp[j-1][2]) + arr[j][0]
        # 초록색을 선택할 경우, 이전 집은 초록색이 아니면서 둘 중 최소값으로
        dp[j][1] = min(dp[j-1][0],dp[j-1][2]) + arr[j][1]
        # 파란색을 선택할 경우, 이전 집은 파란색이 아니면서 둘 중 최소값으로
        dp[j][2] = min(dp[j-1][0],dp[j-1][1]) + arr[j][2]
    # 최초에 선택한 색상과 같은 색인 경우 무시
    dp[-1][i] = INF
    result = min(result,min(dp[-1]))
print(result)