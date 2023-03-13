# https://www.acmicpc.net/problem/17086

'''
N×M 크기의 공간에 아기 상어 여러 마리가 있다. 

공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 

한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 

두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 

이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자. 
'''
'''
각 칸에 대해서 bfs를 수행하면서, 1을 발견하면 bfs를 멈추고 이동한 칸 수를 기록한다.
모든 칸에 대해 bfs가 끝나면 가장 큰 값을 정답으로 출력한다.
'''
from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 이동은 대각선까지 포함한다.
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


# bfs정의
def bfs(s, e):
    queue = deque()
    queue.append([s, e])
    # 최소거리를 기록할 배열
    visited = [[-1]*m for _ in range(n)]
    visited[s][e] = 0  # 방문처리
    while queue:
        x, y = queue.popleft()

        # 만약 목적지에 도달하였다면 정답 출력
        if graph[x][y] == 1:
            return visited[x][y]

        for i in range(8):  # 이동할수 있는 모든 방향에 대해 bfs
            nx, ny = x + dx[i], y + dy[i]
            # 영역을 벗어나지 않으면서 처음 방문하는 경우만 방문
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

    return -1  # 주위에 아기상어가 전혀 없는경우 -1 리턴


# 안전거리를 저장할 배열 생성
safe = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        safe[i][j] = bfs(i, j)

result = 0

# 최대값 탐색
for array in safe:
    result = max(result, max(array))

print(result)
