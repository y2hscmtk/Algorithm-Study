# https://www.acmicpc.net/problem/25416
'''
5 x 5 크기의 격자판
-1 이 적힌 칸으로 이동불가, 0,1이 적힌 칸으로 이동 가능
상하좌우 이동 가능, 1이 적혀 있는 칸에 도달하기 위한 최소 이동 횟수 출력
'''
from collections import deque

graph = [list(map(int,input().split())) for _ in range(5)]
visited = [[-1 for _ in range(5)] for _ in range(5)]
r,c = map(int,input().split())

def bfs(s,e):
    queue = deque()
    queue.append((s,e))
    dx = [0,0,-1,1]; dy = [-1,1,0,0]
    visited[s][e] = 0 # 시작지점 방문처리
    while queue:
        x,y = queue.popleft()
        # 1이 적혀있는 칸에 도달하였다면 정답 리턴
        if graph[x][y] == 1:
          return visited[x][y]
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0<=nx<5 and 0<=ny<5:
                # -1인 칸은 방문 불가
                if graph[nx][ny] != -1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    
    return -1 # 이동할 수 없는 경우
    
print(bfs(r,c))
