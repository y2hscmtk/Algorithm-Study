# https://www.acmicpc.net/problem/1303
'''
내 병사는 w
n명이 뭉쳐있을때 n^2만큼의 힘을 낼 수 있다.
W의 총력과 B의 총력을 차례로 출력한다.
'''
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n,m = map(int,input().split())

graph = [list(input()) for _ in range(m)]
# 방문 정보를 기록하기 위한 배열
visited = [[False]*n for _ in range(m)]


W_power,B_power = 0,0 # 각 병력


def bfs(s,e):
    global visited,W_power,B_power
    queue = deque()
    queue.append([s,e])
    visited[s][e] = True # 방문처리
    color = graph[s][e] # 탐색을 시작할 해당 좌표가 어느 진영인지 가져온다.
    count = 1 # 총 몇명이 뭉쳐있는지 판단
    while queue:
        x,y = queue.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않는 선에서
            if 0<=nx<m and 0<=ny<n:
                # 아직 방문하지 않았고, 같은 팀 이라면
                if not visited[nx][ny] and color==graph[nx][ny]:
                    count += 1 # 카운팅 증가
                    visited[nx][ny] = True # 방문처리
                    queue.append([nx,ny]) # 큐에 삽입
    # 탐색이 끝난이후 전력 업데이트
    if color == 'W':
        W_power += (count*count)
    else:
        B_power += (count*count)
        


# 배열을 돌면서 아직 방문하지 않은 좌표에 대해 bfs수행
for i in range(m):
    for j in range(n):
        if not visited[i][j]: # 아직 탐색하지 않은 좌표라면
            bfs(i,j) # bfs수행


# 각 전력을 출력한다.
print(W_power,B_power)
