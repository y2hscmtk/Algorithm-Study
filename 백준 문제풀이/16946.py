# https://www.acmicpc.net/problem/16946
from collections import deque
n,m = map(int,input().split())

# 그래프 입력받기
graph = [list(map(int, input())) for i in range(n)]

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]


# bfs 정의
def bfs(s,e):
    count = 1 # 이동할수 있는 좌표들
    queue = deque()
    queue.append([s,e])
    # 방문정보 그래프
    visited = [[False]*m for _ in range(n)]
    visited[s][e] = True # 방문처리
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않는지 확인
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                # 빈칸인 경우에만 방문 가능
                if graph[nx][ny] == 0:
                    # 방문 처리 후 큐에 삽입
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    # 카운트 1 증가
                    count+=1
    return count%10 # 10으로 나눈 나머지 리턴


# 맵의 형태로 정답을 출력한다. 원래 빈 칸인 곳은 0을 출력하고, 
# 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력한다.
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: # 원래 빈칸인 곳은 0을 출력한다.
            print(0,end='')
        else: #벽인 곳은 이동할수 있는 칸을 10으로 나눈 나머지를 출력한다.
            print(bfs(i,j),end='')
    print("")