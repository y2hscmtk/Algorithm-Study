# https://www.acmicpc.net/problem/3197
'''
예상 알고리즘 : 시뮬레이션, 구현, BFS
'.'은 물, 'x'는 얼음, 'L'은 백조
1. 만날 수 있는지 확인한다. (bfs)
2. 만날 수 없었다면 얼음을 지운다. (bfs)
3. 1으로 돌아간다.
물,백조인 지역을 모두 큐에 넣고 시작한다. visited배열을 만들어서 물,백조 인 지역을 모두 방문처리하고 시작한다.
큐에서 하나씩 뽑으면서 상하좌우를 검사하고, 얼음(x)을 만난다면 녹이고(.) 방문처리 후 큐에 다시 삽입한다.( 다른 물의 상후좌우 검사에서 걸리지 않도록)
=> 이로인해 반복되는 시뮬레이션에서 이전에 방문한 물에 대해서는 방문하지 않아도 된다. 
=> 가장 최신화 된 물에서부터 녹이기 작업을 이어서 할 수 있다.(큐에 남아있는)
'''
import sys
input = sys.stdin.readline
from collections import deque
R,C = map(int,input().split())
visited = [[False]*C for _ in range(R)] # 백조 방문한 지역들
dx = [0,0,-1,1]; dy = [-1,1,0,0]
day = 0 # 날짜는 0일차부터 시작함
graph = []
water = deque() # 물 큐
swan = deque() # 백조 큐
for i in range(R):
    row = list(input())
    for j in range(C):
        if row[j] == 'X':
            continue
        if row[j] == 'L':
            sx,sy = i,j # 백조의 위치 저장 => 둘이 만날 수 있는지 탐색할때 사용
        # 백조와 물의 좌표 저장(백조의 밑에도 물이 있으므로 백조 근처의 얼음도 녹는다.)
        water.appendleft((i,j))
    graph.append(row)
swan.appendleft((sx,sy))
visited[sx][sy] = True

def isMeet():
    global swan
    # sx,sy에서 탐색 시작
    new_swan = deque()
    while swan:
        x,y = swan.pop()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
                if graph[nx][ny] == 'X': # 얼음을 만나서 더이상 현재 방향으로 탐색이 불가하다면
                    new_swan.appendleft((x,y)) # 현재 위치 삽입
                    visited[nx][ny] # 중복해서 넣을 수 없도록
                elif graph[nx][ny] == '.':
                    swan.appendleft((nx,ny))
                    visited[nx][ny] = True # 방문처리
                else: # 'L', 즉 백조를 만났다면
                    return True
    # 현재 시도에서 만나지 못할경우
    swan = new_swan # 다음 시도로 넘기기(new_swan에 들어있는 좌표들은 모두 시작 위치에서 방문 가능한 위치들임)
    return False

def meltIce():
    global water
    new_water = deque() # 새로 생길 물들의 좌표
    # 아직 큐에 남아있는 모든 얼음들에 대해(큐에 남아있다는 것은 아직 탐색을 하지 않았다는 의미임)
    while water:
        x,y = water.pop()
        # 현재 물의 상하좌우 좌표에 대해 벽인지 아닌지 검사
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C:
                if graph[nx][ny] == 'X': # 얼음이라면(물과 닿아있는)
                    graph[nx][ny] = '.' # 물로 녹이기 처리
                    new_water.appendleft((nx,ny)) # 큐에 새로운 물 삽입(현재시점에서는 탐색x)
    water = new_water # 다음 날로 녹이기 좌표들 넘기기

while True:
    if isMeet():
        break
    # 만나지 못하였다면 얼음 지우기(이전 기록을 그대로 가져간다)
    day += 1
    meltIce()
print(day)