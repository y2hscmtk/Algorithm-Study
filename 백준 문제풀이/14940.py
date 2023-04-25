from collections import deque
n, m = map(int, input().split())
# 그래프 입력받기
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문정보를 저장할 배열 생성
visited = [[-1]*m for _ in range(n)]

s, e = -1, -1  # 방문을 시작할 위치


def bfs(s, e):
    queue = deque()
    queue.append([s, e])
    while queue:
        x, y = queue.popleft()
        # 네 방향에 대해 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않으면서 처음 방문하는 정점에 대해서만
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:

                # '1'인 좌표만 지나갈수 있음
                if graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1  # 이전 좌표에서 +1(방문처리)
                    queue.append([nx, ny])


# 시작 위치 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            visited[i][j] = 0  # 방문 시작할 위치
            s, e = i, j
        elif graph[i][j] == 0:
            visited[i][j] = 0

# bfs 수행
bfs(s, e)

# 정답 출력
for array in visited:
    print(*array)
