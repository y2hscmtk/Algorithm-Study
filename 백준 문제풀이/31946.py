# https://www.acmicpc.net/problem/31946
'''
1행 1열에서 시작해서 N행 M열에 도달
현재 밟고 있는 색과 같은 색으로만 이동 가능
맨해튼 거리가 X 이하인 곳으로만 이동 가능
각 정점에 대해서 방문한적 없다면, 맨해튼 거리가 x이하인 곳으로 이동
'''
from collections import deque

N = int(input())
M = int(input())
visited = [[False for _ in range(M)] for _ in range(N)]

graph = [list(map(int,input().split())) for _ in range(N)]

jump = int(input())

color = graph[0][0] # 시작좌표의 색, 같은 색의 블록만 밟을 수 있다.

def bfs():
    global visited
    queue = deque()
    queue.append((0,0)) # 탐색을 시작할 정점

    while queue:
        (x,y) = queue.popleft()
        # 목적지에 도달하였다면 함수 종료
        if (x,y) == (N-1,M-1):
            return "ALIVE"
        # 영역상의 모든 정점에 대해서
        for i in range(N):
            for j in range(M):
                # 아직 해당 정점을 방문하지 않았고, 같은 색의 블록이라면
                if not visited[i][j] and graph[i][j] == color:
                    # 맨해튼 거리가 x이하인지 확인
                    if abs(x-i) + abs(y-j) <= jump:
                        visited[i][j] = True # 방문 처리
                        queue.append((i,j))
    return "DEAD"

print(bfs())
