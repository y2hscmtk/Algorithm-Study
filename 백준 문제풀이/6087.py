# https://www.acmicpc.net/problem/6087
'''
첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)
둘째 줄부터 H개의 줄에 지도가 주어진다. 지도의 각 문자가 의미하는 것은 다음과 같다.
.: 빈 칸
*: 벽
C: 레이저로 연결해야 하는 칸
'C'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.
거울(/, \)을 활용하여 레이저의 방향을 90도 회전 시킬 수 있다.
설치해야하는 거울의 최소값 구하기
<아이디어>
1. C에서 출발한 레이저는 방향을 바꾸기 전까지 일자로만 이동
1.1. 왔던 곳으로 되돌아 가는 방법은 없으며, 진행방향을 그대로 이동하거나, 방향을 바꾸거나 둘 중 하나임
1.2. 방향을 바꿨다는 것은 거울을 활용하여 진행방향을 꺾었다는것을 의미하므로 거울 사용횟수를 큐에 저장한다.
'''
from collections import deque
import sys
input = sys.stdin.readline
W,H = map(int,input().split())
# 상하좌우 방향에 대한 거울 최소 횟수 초기 저장
visited = [[[sys.maxsize]*4 for _ in range(W)] for _ in range(H)]
graph,laser = [],[]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
result = sys.maxsize
# 지도 정보 및 레이저 시작위치 끝 위치 저장
for i in range(H):
    data = input()
    for j in range(W):
        if data[j] == 'C':
            laser.append((i,j))
    graph.append(data)
# 레이저 탐색 시작 위치, 종료 위치 저장
sx,sy = laser[0]; ex,ey = laser[1]

# 레이저 통신
def bfs():
    global visited,result
    queue = deque()
    # 탐색 시작 위치, 현재까지 설치한 거울의 수, 진행방향
    # 처음 탐색시 4방향으로 모두 레이저 발사
    for i in range(4):
        nx = sx + dx[i]; ny = sy + dy[i]
        if 0<=nx<H and 0<=ny<W and graph[nx][ny] != '*': # 벽이 아닌 경우에만 정보 삽입
            visited[nx][ny][i] = 0 # 현재까지 설치된 거울의 수 저장
            queue.append((nx,ny,0,i)) 
    while queue:
        x,y,count,d = queue.popleft()
        # 목적지에 도달하였는지 확인
        if (x,y) == (ex,ey):
            result = min(result,count) # 더 적게 설치된 경우로 업데이트
            continue
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<H and 0<=ny<W and graph[nx][ny] != '*':
                if 0<=nx<H and 0<=ny<W and graph[nx][ny] != '*':
                    # 진행방향과 달라질 경우 count + 1 (레이저 꺾기)
                    n_count = count + (0 if i == d else 1)
                    # i방향을 기준으로 이동하는 경우에 대해 거울 수 단축 가능하다면
                    if n_count < visited[nx][ny][i]:
                        visited[nx][ny][i] = n_count
                        queue.append((nx,ny,n_count,i))

bfs()
print(result)