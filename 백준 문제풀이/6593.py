# https://www.acmicpc.net/problem/6593
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,0,0,-1,1]
dy = [0,0,-1,1,0,0]
dz = [-1,1,0,0,0,0]

def escape():
    global graph
    visited = [[[-1]*C for _ in range(R)] for _ in range(L)]
    visited[sx][sy][sz] == 0
    queue = deque([[sx,sy,sz]])
    while queue:
        x,y,z = queue.popleft()
        if (x,y,z) == (ex,ey,ez): # 목적지 발견시
            t = visited[x][y][z] + 1
            print(f'Escaped in {t} minute(s).')
            return
        for i in range(6):
            nx = x + dx[i]; ny = y + dy[i]; nz = z + dz[i]
            if 0<=nx<L and 0<=ny<R and 0<=nz<C:
                # 빈 공간 중에서 아직 가지 않은 길 인 경우
                if graph[nx][ny][nz] != '#' and visited[nx][ny][nz] == -1:
                    visited[nx][ny][nz] = visited[x][y][z] + 1 # 방문처리
                    queue.append([nx,ny,nz])
    print("Trapped!") # 탈출 불가시
while True:
    L,R,C = map(int,input().split())
    if (L,R,C) == (0,0,0):
        break
    graph = [[] for _ in range(L)] # L개의 층
    for i in range(L):
        for j in range(R):
            cols = list(input().rstrip())
            for k in range(len(cols)):
                if cols[k] == 'S':
                    sx,sy,sz = i,j,k
                elif cols[k] == 'E':
                    ex,ey,ez = i,j,k
            graph[i].append(cols)
        input()
    escape()