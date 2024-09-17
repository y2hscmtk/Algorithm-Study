# https://www.acmicpc.net/problem/18232
'''
현재 위치가 점 X라면 X+1이나 X-1로 이동하거나 
X에 위치한 텔레포트와 연결된 지점으로 이동할 수 있으며 각 행동에는 1초가 소요된다.
점 S에서 점 E로 이동하는데 걸리는 최소 시간 구하기
'''
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
S, E = map(int,input().split()) # S -> E
visited = [-1 for _ in range(N+1)] # 방문정보 저장용
dict = {} # 텔레포트 정보 저장용 딕셔너리
for _ in range(M):
    # 텔레포트 정거장 정보
    x,y = map(int,input().split())
    if x not in dict:
        dict[x] = [y]
    else:
        dict[x].append(y)
    # 텔레포트는 양방향
    if y not in dict:
        dict[y] = [x]
    else:
        dict[y].append(x) 
# S에서 E까지 갈 수 있는 최단 거리
# +1, -1 혹은 텔레포트         
def bfs():
    global visited
    queue = deque()
    queue.append(S)
    visited[S] = 0 # 방문처리
    while queue:
        x = queue.popleft()
        # 목적지에 도달한 경우
        if x == E:
            return
        # 텔레포트 가능하다면 텔레포트
        if x in dict:
            # 텔레포트 가능한 모든 정류장에 대해서 bfs
            for nx in dict[x]:
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1 # 이동
                    queue.append(nx)
        # 그 이외의 경우
        for nx in [x+1,x-1]:
            # 영역을 벗어나지 않으면서 아직 방문하지 않은 경우
            if 0<=nx<=N and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

bfs()
print(visited[E])