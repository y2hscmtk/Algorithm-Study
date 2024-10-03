# https://www.acmicpc.net/problem/14923
'''
3차원 배열 활용
벽을 부쉈을때에 대한 경우 / 벽을 부수지 않았을 때에 대한 경우
'''
from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
hx,hy = map(int,input().split()) # 초기 위치
ex,ey = map(int,input().split()) # 탈출 위치

def bfs(hx,hy,ex,ey):
    queue = deque()
    queue.append((hx,hy,False))

    # 0은 벽을 부수지 않았을 때, 1은 벽을 부쉈을 때
    visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]
    visited[hx][hy][0] = 0 # 시작 위치 방문 처리

    while queue:
        x,y,usePower = queue.popleft() # 현재 위치와 현재 시점에서 벽을 부쉈는지 여부
        
        # 목적지 도달시 리턴
        if (x,y) == (ex,ey):
            # 벽을 부수고 도달한 경우와, 부수지 않고 도달한 경우 둘 중 최소 반환
            return visited[x][y][usePower]

        for nx,ny in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
            # 영역 검사
            if 0<=nx<N and 0<=ny<M:
                # 조건 검사
                # 벽이라면 - 벽을 부술수 있는지 여부 판단
                if graph[nx][ny] == 1 and not usePower:
                    # 벽을 부순후(usePoser -> True), 벽을 부순 시점에서의 이동 수행
                    # 벽을 부수지 않았던 차원에서 부순 후의 차원으로 이동
                    # 방문 기록이 있는지 확인
                    if visited[nx][ny][1] == -1: # 방문 기록이 없는 경우에 한해서만 이동 수행
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        queue.append((nx,ny,True)) # 벽을 부순 기록을 함께 전달
                # 벽이 아니라면 이동 가능 - 벽을 부순 차원 / 부수지 않은 차원 선택 후 이동
                elif graph[nx][ny] == 0: # 벽이 없다면
                    # 이전에 벽을 부순적이 있다면 
                    d = 1 if usePower else 0
                    # 해당 위치를 이전에 방문 한적 있다면 방문x
                    if visited[nx][ny][d] == -1:
                        visited[nx][ny][d] = visited[x][y][d] + 1
                        queue.append((nx,ny,usePower)) # 이전 선택(벽을 부쉈는지)의 결과를 전달
    # 탈출 할수 없으면 -1
    return -1

graph = [list(map(int,input().split())) for _ in range(N)]

print(bfs(hx-1,hy-1,ex-1,ey-1))
