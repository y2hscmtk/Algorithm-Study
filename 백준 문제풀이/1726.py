# https://www.acmicpc.net/problem/1726
'''
명령 1. Go k: k는 1, 2 또는 3일 수 있다. 현재 향하고 있는 방향으로 k칸 만큼 움직인다.
명령 2. Turn dir: dir은 left 또는 right 이며, 각각 왼쪽 또는 오른쪽으로 90° 회전한다.

로봇의 현재 위치와 바라보는 방향이 주어졌을 때, 로봇을 원하는 위치로 이동시키고, 
원하는 방향으로 바라보도록 하는데 최소 몇 번의 명령이 필요한지 구하는 프로그램을 작성하시오.

특정 지역으로 이동하였을 때, 이전에 해당 지역을 방문하였을 때보다 더 단축 가능한 상황에서 방문 가능하다면 업데이트

방향은 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4로 주어진다.

      3(북)
1(서)        0(동)
      2(남)
'''
import sys
from collections import deque
M,N = map(int,input().split()) # 세로, 가로 <= 100
dx = [0,0,1,-1]; dy = [1,-1,0,0] # 동,서,남,북

def bfs():
    queue = deque()
    # 각 방향으로 나아갔을 때에 대한 최소 명령 횟수를 저장한다.
    visited = [[[sys.maxsize for _ in range(4)] for _ in range(N)] for _ in range(M)]
    visited[sx][sy][sd] = 0 # 최초 위치,방향은 방문 수 0으로 기록
    queue.append((sx,sy,sd)) 
    while queue:
        x,y,d = queue.popleft()
        if (x,y,d) == (ex,ey,ed):
            return visited[ex][ey][ed]
        
        # 네 방향에 대해서
        for i in range(4):
            # 현재 방향에 +1 후 모듈러 연산
            nd = (d+i)%4
            # 방향을 바꾸는 것 또한 하나의 명령이므로 visited 카운트 + 1
            # 카운트 증가시 기존 해당 칸의 해당 방향에 도달하기 위한 횟수보다 
            # 현재 수행으로 인해 단축되는 경우에만 이동

            # (동,서),(서,동),(북,남),(남,북) 인 경우 즉 2번 회전해야 하는 경우
            if (d,nd) == (0,1) or (d,nd) == (1,0) or (d,nd) == (3,2) or (d,nd) == (2,3):
                if visited[x][y][d] + 2 < visited[x][y][nd]: 
                    visited[x][y][nd] = visited[x][y][d] + 2 # 최단거리로 업데이트
                    queue.append((x,y,nd)) # 현재 정보 큐에 삽입 후
            elif d != nd: # 자기 자신이 아닌경우 -> 한번의 명령으로 방향 회전이 가능한 경우
                if visited[x][y][d] + 1 < visited[x][y][nd]: 
                    # 이동하려는 방향이 현재 방향과 정 반대 방향의 경우
                    visited[x][y][nd] = visited[x][y][d] + 1 # 최단거리로 업데이트

                    queue.append((x,y,nd)) # 현재 정보 큐에 삽입 후

            # 현재 이동방향에 대해 k칸만큼 이동 연산 수행
            for k in range(1,4):
                nx = x + k*dx[nd]
                ny = y + k*dy[nd]
                
                # 현재 칸으로 이동 가능한지 파악
                if 0<=nx<M and 0<=ny<N:
                    if graph[nx][ny] == 1:
                        break # 벽이 있는 경우는 궤도가 없는 경우에 해당
                    # 궤도가 있는 경우 이동
                    # 현재 칸으로 이동 시 기존에 해당 위치에 도달했던 이력보다 더 단축 가능한지 확인
                    if visited[x][y][nd] + 1 < visited[nx][ny][nd]:
                        visited[nx][ny][nd] = visited[x][y][nd] + 1
                        queue.append((nx,ny,nd))
# 0은 갈 수 없는 지역, 1은 갈 수 있는 지역
graph = [list(map(int,input().split())) for _ in range(M)]

# 로봇의 출발 지점의 위치, 현재 바라보고 있는 방향
sx,sy,sd = map(int,input().split())
sx-=1; sy-=1; sd-=1 # 인덱스 맞추기

# 로봇의 도착 지점의 위치, 바라보길 희망하는 방향
ex,ey,ed = map(int,input().split())
ex-=1; ey-=1; ed-=1 # 인덱스 맞추기

# 첫째 줄에 로봇을 도착 지점에 원하는 방향으로 이동시키는데 필요한 최소 명령 횟수를 출력한다.
print(bfs())
