# https://www.acmicpc.net/problem/17836
'''
두번째 시도

검을 획득시 벽을 무제한으로 부술 수 있다 -> 검을 획득할 때까지 이동하는 거리 + 검이 있는 위치에서 공주가 있는 곳까지의 최단거리

하지만 굳이 검을 획득하지 않고 최단거리(BFS)로 이동 하는 것이 최단 거리 일 수 있음

2가지 경우를 고려하여 둘 중 더 짧은 값을 정답으로 채택
'''
from collections import deque
import sys
input = sys.stdin.readline

# T는 시간 제한
N,M,T = map(int,input().split())

graph = []
sx,sy = 0,0
for i in range(N):
    row = list(map(int,input().split()))
    for j in range(len(row)):
        if row[j] == 2:
            sx,sy = i,j # 검의 위치 저장
    graph.append(row)

# 검 찾기 최단 거리
def find_sword():
    queue = deque()
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 0 # 시작 위치 방문 처리
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        if (x,y) == (sx,sy):
            return visited[x][y]
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            # 영역 검사
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
                if graph[nx][ny] != 1: # 벽이 아닌 경우에 한해
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return sys.maxsize # 검에 도달 할 수 없을 경우

def bfs(): # 탐색 시작 좌표, 검의 보유 여부
    queue = deque()
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 0 # 시작 위치 방문 처리
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        if (x,y) == (N-1,M-1):
            return visited[x][y]
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
                if graph[nx][ny] != 1: # 벽이 아닌 경우에 한해
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return sys.maxsize # 목적지에 도달할 수 없을 경우

solve1 = bfs() # 검을 사용하지 않는 경우
# 검을 찾으려 이동하는 최단 거리 + 검에서 목적지까지의 최단 거리
solve2 = find_sword() + abs(sx-(N-1)) + abs(sy-(M-1)) 

result = min(solve1,solve2)
print(result) if result <= T else print("Fail") # 주어진 시간 안에 찾을 수 없다면 -1을 출력한다.