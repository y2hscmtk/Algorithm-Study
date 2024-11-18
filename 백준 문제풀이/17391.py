# https://www.acmicpc.net/problem/17391
import sys
input = sys.stdin.readline
from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
visited[0][0] = 0
dx = [0,1]; dy = [1,0] # 오른쪽 또는 아래로만 이동 가능

def bfs():
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        # 목적지 도달시 성공
        if (x,y) == (N-1,M-1):
            print(visited[x][y])
            return
        p = graph[x][y]
        # 최대 p칸만큼 이동 가능
        for j in range(1,p+1):
            for i in range(len(dx)):
                nx = x + j*dx[i]; ny = y + j*dy[i]
                if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
bfs()