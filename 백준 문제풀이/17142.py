# https://www.acmicpc.net/problem/17142
'''
바이러스는 활성 상태와 비활성 상태가 있다.
가장 처음 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 인접한 모든 빈칸으로 동시에 복제되며 1초가 걸린다.
승원이는 연구실의 바이러스 M개를 활성 상태로 변경하려고 한다.
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
=> 활성화 바이러스가 비활성화 바이러스를 만나면 그대로 통과한다는 의미
=> 초기에 비활성화 상태인 바이러스가 활성화가 된다고 해서 퍼져나갈수는 없다. 
연구실의 크기는 N x N 크기, 연구소는 빈 칸, 벽, 바이러스로 이루어져 있다.
0은 빈칸 1은 벽 2는 바이러스의 위치이다.

연구소의 상태가 주어질 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.

브루트포스, 깊이 우선 탐색, 백트래킹

<아이디어>
바이러스(2)들 중 M개를 뽑아 활성화 상태로 만들고 최단 시간을 측정한다.
연구소의 크기는 최대 50x50 => 2500칸, 활성화 시킬 수 있는 바이러스의 수는 최대 10개
'''
from collections import deque
import sys
input = sys.stdin.readline
lab,virus,selected = [],[],[] # 연구실, 바이러스를 놓을 수 있는 위치, 바이러스를 놓기로 선택한 좌표
result = sys.maxsize # 바이러스를 확산시키는데 걸린 최소 시간
N,M = map(int,input().split())
dx = [0,0,-1,1]; dy = [-1,1,0,0] # 바이러스는 상하좌우로 확산한다.
for i in range(N):
    row = list(map(int,input().split()))
    # 바이러스의 위치 저장
    for j in range(N):
        if row[j] == 2: # 바이러스를 놓을 수 있는 위치라면
            virus.append((i,j))
    lab.append(row) # 행 정보 입력
    
# 바이러스 확산 실시
def bfs():
    global able
    visited = [[-1]*N for _ in range(N)]
    # 바이러스가 놓인 좌표들은 우선 0초로 설정
    for x,y in selected:
        visited[x][y] = 0
    # 바이러스 확산 실시
    time = 0 # 확산하는데 걸린 시간 갱신용
    queue = deque(selected)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            # 바이러스는 벽이 아닌 곳(비활성 바이러스가 있거나, 방문하지 않은 좌표)으로 확산한다.
            if 0<=nx<N and 0<=ny<N:
                # 아직 방문하지 않은 좌표이면서 벽이 아닌 좌표(비활성화 바이러스 좌표 혹은 빈칸)
                if visited[nx][ny] == -1 and lab[nx][ny] != 1:
                    # 만약 바이러스가 활성화 상태라면 
                    if lab[nx][ny] == 2: # 비활성화 바이러스가 활성화 될 경우
                        visited[nx][ny] = visited[x][y] + 1 # 이동하는데 걸린시간은 존재하기 때문에 +1
                        # 비활성화 바이러스가 확산된 경우 갱신은 실시하지 않는다.
                    else:
                        visited[nx][ny] = visited[x][y] + 1 # 확산에 걸린 시간
                        time = max(time,visited[nx][ny])
                    queue.append((nx,ny))
    for i in range(N):
        for j in range(N):
            # 빈칸중에 아직 바이러스 확산이 안된 칸이 있다면(비활성화 바이러스는 바이러스가 존재하는 것으로 간주)
            if visited[i][j] == -1 and lab[i][j] == 0:
                return -1 # -1을 리턴
    return time # 모든 칸이 확산되는데 걸린 시간 반환
            
# 바이러스를 놓을 좌표 M곳 선정
def select_virus(start):
    global result
    if len(selected) == M:
        # M개를 놓았으면, 바이러스 확산을 시뮬레이션하고 최소 시간을 갱신한다.
        time = bfs()
        if time != -1: # -1이 아니라면 정답 갱신
            result = min(result,time)
        return
    # 아직 M개의 바이러스를 선택하지 않았다면 바이러스를 선택한다.
    for i in range(start, len(virus)):
        selected.append(virus[i])
        select_virus(i+1)
        selected.pop()
    
select_virus(0) # 바이러스를 선택하고 바이러스 확산을 실시한다.
# 여전히 result가 sys.maxsize에 머물러 있다 => 모든 경우의 수에 대해서도 바이러스 확산에 실패함
print(-1 if result == sys.maxsize else result)