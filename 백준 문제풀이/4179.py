# https://www.acmicpc.net/problem/4179

'''
지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!

미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.

지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.

불은 각 지점에서 네 방향으로 확산된다.

지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.

지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.

지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.
'''
from collections import deque

r,c =map(int,input().split())

graph = [list(input()) for _ in range(r)]

# 지훈이의 이동에 대해 기록할 배열
visit = [[-1]*c for _ in range(r)]

# 불의 이동에 대해 기록할 배열
fire = [[False]*c for _ in range(r)]

# 지훈이의 초기위치
jx, jy = -1,-1

# 불의 위치 기록
fire_positon = []


# 불과 지훈이의 초기 위치 지정
for i in range(r):
    for j in range(c):
        # 지훈이의 위치 기록
        if graph[i][j] == "J":
            jx, jy = i,j
        # 불의 위치 기록
        elif graph[i][j] == "F":
            fire_positon.append([i,j])


# bfs에 사용할 큐 생성
queue = deque()

# 불의 위치 먼저 기록
for x,y in fire_positon:
    queue.append([x,y,True]) # 불임을 확인하기위해
    # 초기 불 위치 기록
    fire[x][y] = True # 불이 번졌다는 표시

# 지훈이의 위치 기록
queue.append([jx,jy,False])
visit[jx][jy] = 0 # 지훈이 현재위치 표시 수를 늘려가며 누적시킬예정


# 방향 벡터
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(queue):
    while queue:
        x,y,isFire = queue.popleft()

        # 지훈이가 목적지에 도달하였는지 확인
        if not isFire:
            if x == 0 or x == r-1 or y==0 or y==c-1:
                return visit[x][y]+1

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            # 영역을 벗어나지 않으면서 벽이 아닌지 확인
            if 0<=nx<r and 0<=ny<c and graph[nx][ny] != '#':
                # 불의 이동과 지훈이의 이동을 나누어 생각
                if isFire:
                    # 불의 경우
                    # 불이 아직 번지지 않은 부분인지 확인
                    if not fire[nx][ny]:
                        fire[nx][ny] = True # 불 번지게 
                        queue.append([nx,ny,True])
                else:
                    # 지훈이의 이동의 경우
                    # 지훈이가 아직 방문하지 않은 지역이면서 불이 번지지않은 지역인지 확인
                    if not fire[nx][ny] and visit[nx][ny] == -1:
                        visit[nx][ny] = visit[x][y] + 1
                        queue.append([nx,ny,False])
    
    # 탈출이 불가할경우
    return "IMPOSSIBLE"

print(bfs(queue))
