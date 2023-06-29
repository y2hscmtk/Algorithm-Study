# https://www.acmicpc.net/problem/1743
from collections import deque

n,m,k = map(int,input().split())

# 그래프 생성
graph = [["."]*m for _ in range(n)]

# 생성한 그래프에 음식물 추가

for i in range(k):
    r,c = map(int,input().split())
    # 해당 위치에 음식물이 있음을 의미
    graph[r-1][c-1] = "#"


dx = [0,0,-1,1]
dy = [-1,1,0,0]

result = 0 # 가장 큰 음식물의 크기

def bfs(s,e):
    global graph,result
    count = 1
    queue = deque()
    queue.append([s,e])
    graph[s][e] = '.'
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않는다면
            if 0<=nx<n and 0<=ny<m:
                # 음식물이라면
                if graph[nx][ny] == '#':
                    graph[nx][ny] = '.' # 방문처리
                    queue.append([nx,ny])
                    count +=1
    # 더 큰 음식물을 발견했다면 업데이트
    result = max(result,count)
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            bfs(i,j)

print(result)
