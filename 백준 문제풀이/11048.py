'''
<분석>
1 2 3 4
0 0 0 5
9 8 7 6

dp[i][j] = (i,j)번째 위치에서 가질 수 있는 사탕의 최대 값
현재 칸에서 이동 가능한 범위는 오른쪽, 오른쪽 아래 대각선, 아래, 3가지 경우
따라서 (i,j)번째 위치에 올 수 있는 방법은 위 3가지 방법을 통해 올 수 있음
(i,j)번째 위치에서의 사탕의 최대 값은 위 3가지 방향의 값 들 중 최대 값 + 현재 칸의 사탕의 수를 의미

1  3  6  10
1  3  6  15
10 18 25 31

<점화식>
사탕 배열을 arr라고 할 때,
dp[i][j] = max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + arr[i][j]

=> 점화식을 편하게 사용하기 위해, 왼쪽 끝과 최상단을 값이 0인 패딩으로 감싼다.
'''
# https://www.acmicpc.net/problem/11048
n,m = map(int,input().split())
arr = [[0]*(m+1)] + [[0] + list(map(int,input().split())) for _ in range(n)] # 0으로 패딩 붙이기
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        # 현재 값 + 왼쪽,위,왼쪽위 대각선 중 최대 값
        dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + arr[i][j]
print(dp[n][m])
