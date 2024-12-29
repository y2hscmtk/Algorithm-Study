from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 영역 검사 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    count = 1  # 현재 칸 포함
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                count += 1
                queue.append((nx, ny))
    return count

# 그룹별 필요한 포자의 수 계산
required_spores = 0
group_found = False  # 그룹이 발견되었는지 검사

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            group_size = bfs(i, j)
            group_found = True  # 그룹 존재 여부 확인
            required_spores += -(-group_size // k)  # 올림 계산

if not group_found:
    print("IMPOSSIBLE")  # 버섯을 심을 수 있는 칸이 하나도 없는 경우
elif required_spores <= m:
    print("POSSIBLE")
    print(m - required_spores)
else:
    print("IMPOSSIBLE")
