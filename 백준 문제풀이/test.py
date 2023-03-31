from collections import deque

# 상, 하, 좌, 우 이동을 위한 dx, dy 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 얼음 미로의 크기를 입력받음
n, m = map(int, input().split())

# 얼음 미로를 나타내는 2차원 리스트 생성
ice_maze = [list(map(int, input().split())) for _ in range(n)]

# 각 칸이 언제 [빈 칸]이 될지에 대한 정보도 2차원 리스트에 저장
for i in range(n):
    for j in range(m):
        if ice_maze[i][j] > 0:  # [얼음 벽]인 경우 음수로 저장하여 구분
            ice_maze[i][j] = -ice_maze[i][j]

# BFS를 위한 큐 생성 및 초기화
queue = deque()
queue.append((0, 0))  # 시작점 (0, 0)을 큐에 추가
ice_maze[0][0] = 0  # 시작점의 값을 0으로 변경

# BFS 실행
while queue:
    x, y = queue.popleft()
    for i in range(4):  # 상, 하, 좌, 우 이동
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 방문한 칸이 [빈 칸]인 경우
            if ice_maze[nx][ny] == 0:
                ice_maze[nx][ny] = ice_maze[x][y] + 1
                queue.append((nx, ny))
            # 방문한 칸이 [얼음 벽]인 경우
            elif ice_maze[nx][ny] < 0:
                # 해당 칸이 [빈 칸]이 될 때까지 걸리는 시간을 더하여 방문
                if ice_maze[nx][ny] > ice_maze[x][y] - 1:
                    ice_maze[nx][ny] = ice_maze[x][y] - 1
                    queue.append((nx, ny))

# 도착점의 값을 출력
print(ice_maze[n-1][m-1])
