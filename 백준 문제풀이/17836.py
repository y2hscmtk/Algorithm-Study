# https://www.acmicpc.net/problem/17836
'''
벽을 만났을때, 그람을 들고 있는지, 안들고있는지 확인하여 벽을 넘을지 안넘을지 결정한다.
'''
from collections import deque

n, m, t = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]


# bfs
def bfs():
    # 방문 정보를 기록
    visited = [[-1]*m for _ in range(n)]
    # 시작 좌표 방문처리
    visited[0][0] = 0
    gram = 10001 # 칼을 주웠을때 => 현재 걸린 시간 + 공주까지의 거리
    queue = deque()
    queue.append([0,0]) # 시작 좌표
    while queue:
        x,y = queue.popleft()
        
        # 목적지에 도달하였다면 최소값 리턴
        if x==n-1 and y==m-1:
            return min(visited[x][y],gram)
        # 그람을 주웠을 경우
        if graph[x][y] == 2:
            # 현재 위치에서 공주까지의 최단거리 더해주기
            gram = visited[x][y]-1 + n-1-x + m-1-y
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안의 수인지
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
                # 아래는 방문한적 없는 좌표에 대해
                # 벽을 만났을 경우
                if graph[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                    
    return gram

# 시간을 초과하지 않았다면 정답 출력
result = bfs()
if result > t:
    print('Fail')
else:
    print(result+1)