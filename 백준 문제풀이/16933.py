# https://www.acmicpc.net/problem/14442
from collections import deque
'''
이동하지 않고 같은 칸에 머물러있는 경우도 가능하다. 
이 경우도 방문한 칸의 개수가 하나 늘어나는 것으로 생각해야 한다.

낮과 밤이 번갈아가면서 등장한다. 가장 처음에 이동할 때는 낮이고, 한 번 이동할 때마다 낮과 밤이 바뀌게 된다
이동하지 않고 같은 칸에 머무르는 경우에도 낮과 밤이 바뀌게 된다.

도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면
벽을 K개 까지 부수고 이동하여도 된다. 단, 벽은 낮에만 부술 수 있다.
'''
from sys import stdin
input = stdin.readline
n,m,k = map(int,input().split())  # 벽은 k개까지 부술수 있다.
# 전체 맵 입력받기
graph = [list(map(int,input().strip())) for _ in range(n)]
# 벽을 k개까지 부술 수 있으므로, k차원의 visited배열이 필요하다.
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
# 방향 벡터 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]



# bfs정의
def bfs():
    queue = deque()
    queue.append([0,0,0,1,0]) # x좌표,y좌표, 지금까지 부순 벽의 개수, 현재 시간정보 1은 낮, 0은 밤,wait
    visited[0][0][0] = 1 # 탐색 시작 좌표 방문처리
    # bfs시작
    while queue:
        x,y,count,time,wait = queue.popleft()
        # 만약 목적지에 도달하였다면
        if x==n-1 and y==m-1:
            return visited[x][y][count]
        
        # 4가지 방향에 대해서 판단
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않는다면
            if 0<=nx<n and 0<=ny<m:
                # 만약 빈공간을 만났고, 아직 방문한적 없다면
                if graph[nx][ny]==0 and visited[nx][ny][count] == 0:
                    visited[nx][ny][count] = visited[x][y][count] +1 # 거리 누적
                    # 시간 변경 // 한 번 이동할 때마다 낮과 밤이 바뀌게 된다
                    queue.append([nx,ny,count,(time+1)%2,0]) # 큐에 근접좌표 삽입
                    
                # 만약 벽(1)을 만났고, 아직 벽을 부술수 있다면
                # k개만큼 벽을 부술 수 있으므로
                elif graph[nx][ny]==1 and count<k and visited[nx][ny][count+1] == 0:
                    # 시간 확인
                    if time == 0: # 밤이라면
                    # 이동하지 않고 같은 칸에 머물러있는 경우도 가능하다. 
                    # 이 경우도 방문한 칸의 개수가 하나 늘어나는 것으로 생각해야 한다. 
                    # 시간이 흐리길 기다린다
                        queue.append([x,y,count,(time+1)%2,1]) # 큐에 근접좌표 삽입, wait정보 추가
                    else: # 낮이라면
                        # 그 자리에서 대기하여 시간이 추가로 흘렀는지 확인
                        if wait:
                            visited[nx][ny][count+1] = visited[x][y][count] + 2
                            # 거리를 누적시키고, 벽을 1개 추가로 부쉈다는 의미인 배열에 삽입
                            queue.append([nx,ny,count+1,(time+1)%2,0]) # 벽을 하나 부쉈다는 의미를 함께 넣어줌
                        else:
                            visited[nx][ny][count+1] = visited[x][y][count] + 1
                            # 거리를 누적시키고, 벽을 1개 추가로 부쉈다는 의미인 배열에 삽입
                            queue.append([nx,ny,count+1,(time+1)%2,0]) # 벽을 하나 부쉈다는 의미를 함께 넣어줌
                            
    return -1 # 탐색 실패

print(bfs())
            