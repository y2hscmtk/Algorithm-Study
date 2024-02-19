# https://www.acmicpc.net/problem/16946
'''
각 칸에 대해서 bfs를 수행한다면 시간초과 발생
초기에 빈칸에 대해서 bfs를 수행하여 몇칸을 이동할수있는지 사전에 기록해두고
이후에 벽(1)에 대해서 bfs를 수행하여 상하좌우에 존재하는 숫자를 더해서 출력하면 된다.
'''
from collections import deque
n,m = map(int,input().split())
# 그래프 입력받기
graph = [list(map(int, input())) for i in range(n)]
group_count = 0 # 그룹끼리 서로 구별하기 위함

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 이동할 수 있는 칸에 대한 정보를 표현하기 위한 표
move_able = [[0]*m for _ in range(n)]
group = [[0]*m for _ in range(n)] # 그룹 식별용
visited = [[False]*m for _ in range(n)]

def count_empty(s,e):
    global group_count
    group_count += 1 # 그룹 식별자
    queue = deque()
    queue.append([s,e])
    temp = [[s,e]]
    visited[s][e] = True # 방문처리
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] == 0: # 방문하지 않은 빈 영역에 대해서
                    count += 1
                    visited[nx][ny] = True
                    temp.append([nx,ny])
                    queue.append([nx,ny])
    for x,y in temp:
        move_able[x][y] = count # 몇 칸의 공백이 이어져있는지
        group[x][y] = group_count # 그룹 식별용


for i in range(n):
    for j in range(m):
        # 아직 탐색하지 않은 빈칸 발견시
        if not visited[i][j] and graph[i][j] == 0:
            count_empty(i,j) # 빈 영역 탐색 시작


# bfs 정의
def print_info(x,y):
    # 상하좌우를 기준으로 move_able에서 0이 아닌 좌표 발견시 더해서 출력
    count = 1
    visited_group = [] # 방문한 그룹의 번호 기록
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어나지 않는지 확인
        if 0<=nx<n and 0<=ny<m:
            # 아직 방문한적 없는 그룹인지 확인
            if group[nx][ny] not in visited_group: # 방문한적 없는 그룹이라면
                count = (count + move_able[nx][ny])%10 # 값 더하기
                visited_group.append(group[nx][ny]) # 그룹 방문 처리
    return count%10 # 10으로 나눈 나머지 리턴

# graph에서 벽(1)에 대하여 벽을 부수고 이동했을때의 결과 출력
# => 인접한 칸의 상하좌우를 move_able을 기준으로 검사, 0이 아니라면 더하기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: # 원래 빈칸인 곳은 0을 출력한다.
            print(0,end='')
        else: #벽인 곳은 이동할수 있는 칸을 10으로 나눈 나머지를 출력한다.
            print(print_info(i,j),end='')
    print("")