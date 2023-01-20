# https://www.acmicpc.net/problem/7569

'''
3차원 배열형태의 토마토 틀의 토마토가 모두 익는데 걸리는 시간 구하기

토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''
# BFS에 활용할 큐
from collections import deque
# 입출력 시간 최소화
import sys
input = sys.stdin.readline

# 가로칸,세로칸,높이
m, n, h = map(int, input().split())

# 토마토에 대한 정보를 저장
graph = [[list(map(int, input().split())) for i in range(n)] for j in range(h)]

# 방문정보를 저장할 배열
visited = [[[False]*m for i in range(n)] for j in range(h)]

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향으로 접근 가능
dx = [0, 0, 0, 0, 1, -1]  # 가로 벡터
dy = [0, 0, 1, -1, 0, 0]  # 세로 벡터
dz = [1, -1, 0, 0, 0, 0]  # 높이 벡터

queue = deque()  # BFS에 사용할 큐


# BFS구현 => 3차원
def BFS():
    while queue:
        # 큐에서 데이터 팝
        z, y, x = queue.popleft()
        visited[z][y][x] = True  # 방문처리
        # 해당 좌표의 6방향 인접 정점에 대해 BFS수행
        for i in range(6):
            # 인접 좌표로 이동
            nx = x + dx[i]  # 0<=x<m
            ny = y + dy[i]  # 0<=y<n
            nz = z + dz[i]  # 0<=z<h

            # 이동한 좌표가 배열의 범위를 벗어나지 않았고, 익지않은 토마토인경우에만 검사(-1,1등을 무시하기 위해)
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and graph[nz][ny][nx] == 0:
                # 배열의 범위를 벗어나지않는다면 탐색 수행
                if not visited[nz][ny][nx]:  # 아직 방문하지 않았다면
                    visited[nz][ny][nx] = True  # 방문처리
                    # 하루가 지났다는 의미로 값을 누적해준다.
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append([nz, ny, nx])  # 해당 좌표 큐에 삽입


# 1은 익은 토마토,0은 익지않은 토마토, -1은 빈칸
# 탐색을 진행하기전
# 모든 토마토가 1인지 아닌지검사 => 모두 1이라면 0을 출력(모든 토마토가 익는데 0일이 걸렸다.)
# 3차원 배열을 돌면서 익은 토마토를 큐에 삽입
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])  # 익은 토마토가 있는 좌표를 큐에 삽입

BFS()  # BFS 수행

# 최대 일수 계산
result = 0
for box in graph:  # 토마토 한 박스에 대하여
    for tomato in box:  # 박스안의 토마토에 대하여
        # 아직 익지 않은 토마토가 있는지 조사
        if 0 in tomato:
            print(-1)
            exit(0)  # -1를 출력하고 프로그램 종료
        result = result if result > max(tomato) else max(tomato)
        # =>result = max(result,max(tomato))

print(result-1)
