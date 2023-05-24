# https://www.acmicpc.net/problem/1926
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

count = 0 # 그림의 개수
result = 0 # 가장 넓은 그림의 넓이

# 네방향 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(s,e):
    global result # 가장 넓은 그림 업데이트를 위해
    count = 1 # 그림의 넓이 카운트
    graph[s][e] = 0  # 방문처리
    queue = deque()
    queue.append([s,e])
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 1인 지점에 대해서만 탐색
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0 # 방문처리
                    count += 1 # 넓이 카운트 1 증가
                    queue.append([nx,ny]) # 큐에 좌표 삽입
    
    result = max(result,count)

# 반복문을 돌다가 1을 발견하면
# 새로운 그림이라는 의미로 카운트 증가
for i in range(n):
    for j in range(m):
        # 1을 발견하면
        if graph[i][j] == 1:
            bfs(i,j) # 해당 좌표에서 bfs수행
            count += 1 # 그림의 개수 증가
            
print(count)
print(result)    