# https://www.acmicpc.net/problem/14442
from collections import deque
'''
도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면

벽을 K개 까지 부수고 이동하여도 된다.
'''
n,m,k = map(int,input().split())  # 벽은 k개까지 부술수 있다.
# 전체 맵 입력받기
graph = [list(map(int,input())) for _ in range(n)]
# 벽을 k개까지 부술 수 있으므로, k차원의 visited배열이 필요하다.
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
# 방향 벡터 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]



# bfs정의
def bfs():
    queue = deque()
    queue.append([0,0,0]) # x좌표,y좌표, 지금까지 부순 벽의 개수
    visited[0][0][0] = 1 # 탐색 시작 좌표 방문처리
    # bfs시작
    while queue:
        x,y,count = queue.popleft()
        # 만약 목적지에 도달하였다면
        if x==n-1 and y==m-1:
            return visited[x][y][count]
        
        # 4가지 방향에 대해서 판단
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않는다면
            if 0<=nx<n and 0<=ny<m and visited[nx][ny][count] == 0:
                # 만약 빈공간을 만났고, 아직 방문한적 없다면
                if graph[nx][ny]==0:
                    visited[nx][ny][count] = visited[x][y][count] +1 # 거리 누적
                    queue.append([nx,ny,count]) # 큐에 근접좌표 삽입
                # 만약 벽(1)을 만났고, 아직 벽을 부술수 있다면
                # k개만큼 벽을 부술 수 있으므로
                # 이미 부수고 온 벽에 대한 탐색을 더 진행하지 않아야함
                elif graph[nx][ny]==1 and count<k:
                    visited[nx][ny][count+1] = visited[x][y][count] + 1
                    # 거리를 누적시키고, 벽을 1개 추가로 부쉈다는 의미인 배열에 삽입
                    queue.append([nx,ny,count+1]) # 벽을 하나 부쉈다는 의미를 함께 넣어줌
    return -1 # 탐색 실패

print(bfs())
            