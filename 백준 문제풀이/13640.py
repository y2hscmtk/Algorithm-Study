# https://www.acmicpc.net/problem/13460
'''
bfs 응용
4가지 방향으로 이동 가능 => bfs의 4가지 방향으로 이동
탐색이 종료되는 기준은 '벽'을 만나거나 '구멍'을 만나는 경우
파란 구슬이 '구멍'을 만나게 되는 경우 실패로 간주한다.
빨간공의 위치와 파란공의 위치를 그룹으로 묶어서 visited배열로 관리
빨간공과 파란공을 이동 시킨후
이동결과 두 좌표가 서로 같은 곳에 위치한다면 -> 더 많은 거리를 이동한 공을 더 뒤에 배치한다.
'''
import sys
from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
N,M = map(int,input().split())
graph = []
for i in range(N):
    data = list(input())
    for j in range(M):
        if data[j] == 'R':
            rx,ry = i,j
        elif data[j] == 'B':
            bx,by = i,j
    graph.append(data)

def bfs():
    global rx,ry,bx,by
    queue = deque([(rx,ry,bx,by,0)])
    visited = [(rx,ry,bx,by)]
    while queue:
        rx,ry,bx,by,count = queue.popleft()
        # 10번 이상의 이동이 발생했는지 확인
        if count>10:
            return -1
        # 빨간구슬이 '구멍'에 도달하였는지 확인
        if graph[rx][ry] == 'O':
            return count
        for i in range(4):
            # 빨간 구슬 이동
            nrx,nry = rx,ry
            while True: # 벽,또는 구멍을 만날때까지 반복해서 이동
                nrx += dx[i]; nry += dy[i]
                # 다음에 이동하려는 좌표가 '벽' 또는 '구멍'인지 확인
                if graph[nrx][nry] == '#': # 벽이라면
                    nrx-=dx[i]; nry-=dy[i] # 한 칸 이전 좌표에 위치
                    break
                elif graph[nrx][nry] == 'O': # 구멍에 빠진다면
                    break # 그대로
            # 파란 구슬 이동
            nbx,nby = bx,by
            while True:
                nbx += dx[i]
                nby += dy[i]
                # 다음에 이동하려는 좌표가 '벽' 또는 '구멍'인지 확인
                if graph[nbx][nby] == '#': # 벽이라면
                    nbx-=dx[i]; nby-=dy[i] # 한 칸 이전 좌표에 위치
                    break
                elif graph[nbx][nby] == 'O': # 구멍에 빠진다면
                    break
            # 이동 결과 파란 구슬이 구멍에 빠졌는지 확인
            if graph[nbx][nby] == 'O':
                continue # 어떠한 경우에도 파란구슬은 빠지면 안됨(다른 방향으로 시도)
            # 이동 결과 두 구슬이 같은 위치에 존재 하는지 확인
            if (nrx,nry) == (nbx,nby): # 같은 위치에 존재한다면
                # 더 많이 이동한 구슬을 이전 위치에 붙인다.
                if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
                    # 빨간 구슬이 더 많이 이동했다면
                    nrx -= dx[i]; nry -= dy[i] # 현재위치보다 한칸 이전의 위치에 저장
                else: # 파란 구슬이 더 많이 이동했다면
                    nbx -= dx[i]; nby -= dy[i] # 파란구슬을 현재 위치보다 한 칸 이전의 위치에 저장
            # 방문한적이 있는지 확인
            if (nrx,nry,nbx,nby) not in visited:
                visited.append((nrx,nry,nbx,nby))
                queue.append((nrx,nry,nbx,nby,count+1))
    return -1 # 10번에 도달하기도 전에 실패하는 경우

print(bfs())