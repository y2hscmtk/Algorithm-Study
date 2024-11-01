# https://www.acmicpc.net/problem/16173
from collections import deque
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

# 현재 위치에서 오른쪽과 아래로만 이동 가능
dx = [1,0]; dy = [0,1] # 아래, 오른쪽

def bfs():
    queue = deque()
    visited = [[False]*N for _ in range(N)] 
    visited[0][0] = True # 시작 위치 방문 처리
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        if (x,y) == (N-1,N-1):
            print("HaruHaru")
            return
        p = graph[x][y]
        for i in range(2):
            nx = x + p*dx[i]; ny = y + p*dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
    print("Hing")

bfs()