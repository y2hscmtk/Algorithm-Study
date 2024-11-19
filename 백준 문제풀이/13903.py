# https://www.acmicpc.net/problem/13903
from collections import deque
import sys
input = sys.stdin.readline
R,C = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(R)]
dx = []; dy = []
for _ in range(int(input().strip())):
    r,c = map(int,input().split())
    dx.append(r); dy.append(c)
'''
1. 1인 칸만 이동 가능
2. 주어진 규칙에 따라 이동 가능 +r, +c
첫번째 줄의 1인 아무 칸에서 탐색 시작 가능, 마지막 줄에 도달하면 성공
마지막 줄에 도달할 수 없다면 -1 출력
'''
def bfs():
    queue = deque()
    visited = [[-1]*C for _ in range(R)]
    # 첫번째 줄의 1인 칸 미리 큐에 삽입
    for j in range(C):
        if graph[0][j] == 1:
            queue.append((0,j))
            visited[0][j] = 0
    while queue:
        x,y = queue.popleft()
        # 마지막 줄 도달시 성공
        if x == R-1:
            return visited[x][y]
        for i in range(len(dx)):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C and visited[nx][ny] == -1:
                if graph[nx][ny] == 1: # 1인 칸으로만 이동 가능
                    visited[nx][ny] = visited[x][y] + 1 # 방문 처리
                    queue.append((nx,ny))
    return -1 # 출근 실패

print(bfs())
