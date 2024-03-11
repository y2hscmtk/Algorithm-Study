from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]; dy = [0,0,-1,1]

def debug():
    for g in ground:
        print(*g)
        
def bfs(s,e):
    global visited
    queue = deque()
    queue.append([s,e])
    visited[s][e] = True
    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M: # 배열의 범위를 벗어나지 않는다면
                # 아직 방문하지 않은 '배추(1)'라면
                if not visited[nx][ny] and ground[nx][ny] == 1:
                    visited[nx][ny] = True # 방문하고
                    queue.appendleft([nx,ny])
        

for _ in range(int(input())):
    M,N,K = map(int,input().split())
    ground = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().split())
        ground[y][x] = 1
    group_count = 0 # 그룹의 개수를 알기 위함
    for i in range(N):
        for j in range(M):
            # 배추면서 아직 방문하지 않은 곳이라면 => 새로운 그룹 => 그룹 카운트 +1
            if ground[i][j] == 1 and not visited[i][j]:
                group_count+=1
                bfs(i,j)
    print(group_count)