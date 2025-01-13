# 조건에 맞게 선택적으로 전진하는 DP
# 2차원 최대 증가 수열
'''
(0,0) 좌표에서 현재 위치까지 탐색하며, 해당 위치에서 목표 위치까지 도달이 가능한지 확인 후 갱신
dp[i][j] : (0,0)좌표에서 (i,j) 좌표까지 도달하면서 밟을 수 있는 최대 칸의 수
'''
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*m for _ in range(n)]
dp[0][0] = 1 # 시작좌표는 무조건 밟을 수 있음

# 한칸 이상 오른쪽 + 아래 위치여야 점프 가능
dxs = [1,0]; dys = [0,1]

# O(nm)
def update(i,j):
    # 3번 조건 clear
    for ii in range(i):
        for jj in range(j):
            # 1번 조건 - 도달 가능한 칸인지 확인
            if grid[ii][jj] == -1:
                continue
            # 2번 조건 - 현재 위치의 값이 더 작은지 확인
            if grid[ii][jj] < grid[i][j]:
                dp[i][j] = max(dp[i][j], dp[ii][jj] + 1)
    

# O(nm)
# (1,1) 좌표에서부터 탐색 시작
for i in range(1,n):
    for j in range(1,m):
        # (0,0)에서 (i,j)위치까지의 모든 좌표(x,y)들에 대해서
        # 1. (0,0)에서 (x,y)에 도달 가능해야 함 -> 그래야 (x,y)에서 (i,j)로의 도달이 가능
        # 2. grid[x][y]의 칸보다 grid[i][j]의 칸이 더 커야함
        # 3. (x,y)에서 (i,j)까지 한칸이상 오른쪽, 아래 위치여야 한다.
        update(i,j)

ans = 0
# dp테이블에서의 최대값이 정답
for i in range(n):
    for j in range(m):
        ans = max(ans,dp[i][j])

print(ans)

# 최종 시간 복잡도
# O((nm)^2)