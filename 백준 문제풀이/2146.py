# https://www.acmicpc.net/problem/2146
'''
아이디어
1. 최초 bfs를 통해 섬이 몇개인지 파악 => 한번도 방문한 적 없는 섬이라면 새로운 섬
2. 섬의 끝(물과 맞닿아 있느 부분)을 모두 하나의 큐에 미리 넣어둔다.
3. 섬의 끝을 대상으로 각각 탐색을 수행하여 다른 섬에 도달았을때의 거리를 구하고(bfs) 최소 거리를 갱신한다.
'''
import sys
input = sys.stdin.readline
from collections import deque
dx = [0,0,-1,1]; dy = [-1,1,0,0]
end_point = deque() # 탐색을 시작할 섬의 끝 부분을 의미한다.
island_num,result = 0,sys.maxsize # 섬 번호, 지어진 다리의 최소길이
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
# 최초로 발견하는 섬에 대해서, end_point(섬의 끝단)을 찾아서 (좌표,섬 번호)형식으로 저장
def find_island(s,e):
    global end_point
    queue = deque()
    queue.append([s,e])
    visited[s][e] = True
    graph[s][e] = island_num
    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = True # 방문처리
                # 만약 아직 방문하지 않은 땅(1)이라면
                if graph[nx][ny] == 1:
                    graph[nx][ny] = island_num # 섬 번호로 땅 변환
                    queue.append([nx,ny])
                # 만약 현재 섬에서 상하좌우 중 한 곳이 물(0)이라면, 섬의 끝단을 의미
                elif graph[nx][ny] == 0:
                    end_point.append([x,y,island_num]) # 현재 땅이 섬의 끝단, 섬 정보도 남겨야함

def make_bridge():
    global result
    for x,y,num in end_point: # 각 섬의 끝단에서 각각 다리 짓기
        visited = [[-1]*N for _ in range(N)]
        visited[x][y] = 0
        queue = deque()
        queue.append([x,y])
        while queue:
            x,y = queue.popleft()
            # 만약 이동하게 된 좌표가 현재 섬의 번호와 다르다면 => 다리가 만들어졌다.
            if graph[x][y] != 0 and graph[x][y] != num:
                result = min(result,visited[x][y]-1) # 이전까지가 땅이므로 -1
                break
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1:
                    # 자기 땅이 아닌 경우에만 다리를 지을 수 있음
                    if graph[nx][ny] != num:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx,ny])

# 처음 방문하는 땅(1)에 대해서 섬 찾기 시작
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            continue
        if graph[i][j] == 1 and not visited[i][j]:
            island_num += 1 # 새로운 섬을 찾았으므로 +1
            find_island(i,j)

# 찾은 섬을 바탕으로 다리 짓기 시작 => 지은 다리의 길이를 보고 다리 길이 갱신
make_bridge()
print(result)
