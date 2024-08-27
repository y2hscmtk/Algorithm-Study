# https://www.acmicpc.net/problem/21938
'''
경계값 T보다 크거나 같다면 255, 작으면 0으로 바꿔서 영상처리
새로 만들어진 화면에서 255는 물체로 인식되며 상하좌우 인접한 픽셀들은 같은 물체로 인식된다.
물체가 몇개인지 구하기
'''
from collections import deque
import sys
input = sys.stdin.readline
dx = [0,0,-1,1]; dy = [-1,1,0,0]
N,M = map(int,input().split())
# 영상 정보를 위한 배열
data = [list(map(int,input().split())) for _ in range(N)]
T = int(input()) # 임계값 T
result = 0 # 측정된 물체의 개수
graph = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
# 영상 압축
for j in range(N):
    for i in range(0,M*3,3):
        # 평균값 계산 및 데이터 압축
        avg = sum(data[j][i:i+3])/3
        if avg >= T:
            graph[j][int(i/3)] = 255
        else:
            graph[j][int(i/3)] = 0

# bfs 작성(물체 개수 측정용)
def bfs(x,y):
    global visited
    visited[x][y] = True # 시작 좌표 방문처리
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                # 연결되어있는 물체인지 판정
                if graph[nx][ny] == 255:
                    visited[nx][ny] = True
                    queue.append([nx,ny])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 255 and not visited[i][j]:
            result+=1
            bfs(i,j)

print(result)