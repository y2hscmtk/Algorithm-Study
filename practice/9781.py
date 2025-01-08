# https://www.acmicpc.net/problem/9781
from collections import deque
dxs = [-1,-2,-2,-1,1,2,2,1]
dys = [-2,-1,1,2,2,1,-1,-2]

n,m = map(int,input().split())

graph = [list(input()) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'K': # 탐색 시작 위치
            sx,sy = i,j
        elif graph[i][j] == 'X': # 목적지 위치
            ex,ey = i,j

# 영역 검사
def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():
    visited[sx][sy] = 0
    queue = deque([(sx,sy)]) # 시작 위치 기록
    while queue:
        x,y = queue.popleft()
        # 목적지 도달 확인
        if (x,y) == (ex,ey):
            return visited[x][y]
        for dx,dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny) and visited[nx][ny] == -1:
                # 방문 가능한 칸인지 확인
                if graph[nx][ny] != '#':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return -1

print(bfs())
