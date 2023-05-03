# https://www.acmicpc.net/problem/16174
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방문정보 기록
visited = [[False]*n for _ in range(n)]

# 오른쪽과 아래만 이동 가능
dx = [1, 0]
dy = [0, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        jump = graph[x][y]  # 얼만큼 점프를 할 수 있는지

        # 목적지에 도달하였다면
        if jump == -1:
            return "HaruHaru"
        for i in range(2):
            nx = x + dx[i]*jump
            ny = y + dy[i]*jump
            # 범위를 벗어나지 않았는지 확인
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 새로이 큐에 삽입
                queue.append([nx, ny])
                visited[nx][ny] = True  # 방문처리
    # 원하는 목적지에 도달하지 못했다면
    return "Hing"


print(bfs(0, 0))
