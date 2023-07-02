# https://www.acmicpc.net/problem/2931
# 이동할수 있는 타일을 미리 제작 => 방향 벡터로 이용
'''
       [-1,0]
[0,-1] [0,0] [0,1]
       [1,0]
'''
from collections import deque
import sys
# 각 블록별로 인덱스로 매핑
# 블록 '|'	블록 '-'	블록 '+'	블록 '1'	블록 '2'	블록 '3'	블록 '4'
block_list = ['|','-','+','1','2','3','4']
change = {'|':0,'-':1,'+':2,'1':3,'2':4,'3':5,'4':6}
# 타일 배열의 각 인덱스에서 
# 첫번째 배열 => dx, 두번째 배열 => dy
# 0번 블록(위,아래) |
num0 = [[-1,1],[0,0]]
# 1번 블록(왼쪽,오른쪽) ─
num1 = [[0,0],[-1,1]]
# 2번 블록(상하좌우) ┼
num2 = [[-1,1,0,0],[0,0,-1,1]]
# 3번 블록(아래,오른쪽) ┌
num3 = [[1,0],[0,1]] 
# 4번 블록(위,오른쪽) └
num4 = [[-1,0],[0,1]]
# 5번 블록(왼쪽,위) ┘
num5 = [[0,-1],[-1,0]]
# 6번 블록(왼쪽,아래) ┐
num6 = [[0,1],[-1,0]]

block = [num0,num1,num2,num3,num4,num5,num6]

top = [0,2,3,6]
bottom = [0,2,4,5]
left = [1,2,3,4]
right = [1,2,5,6]

# 0번 타일 [위,아래] |
can0 = [top,bottom]
# 1번 블록(왼쪽,오른쪽) ─
can1 = [left,right]
# 2번 블록(상하좌우) ┼
can2 = [top,bottom,left,right]
# 3번 블록(아래,오른쪽) ┌
can3 = [bottom,right]
# 4번 블록(위,오른쪽) └
can4 = [top,right]
# 5번 블록(왼쪽,위) ┘
can5 = [left,top]
# 6번 블록(왼쪽,아래) ┐
can6 = [left,bottom]

pipe_candidate = [can0,can1,can2,can3,can4,can5,can6]


'''
# 블록 하나가 제거되어 가스가 목적지까지 흐를 수 없는 상황이다.

# 1. 제거된 블록의 위치를 알아야한다
# 1.1. bfs를 통해 목적지에 도달하지 못한채로 '.'을 만나면 해당칸이 지워진 칸이다.

# 2. 원래 존재했던 블록이 어떤것인지 알아야한다.
# 2.2. 올바른 블록을 채워넣으면 모든 가스관에 가스가 흘러야한다 
# => 방문하지 않은채로 남아있는 가스관이 있다면 가스관을 다른 번호로 변경해서 bfs를 다시 수행한다
# 위 과정은 모든 가스관을 방문할때까지 반복한다.
'''
def find_block(s,e):
    global t_x,t_y
    queue = deque()
    queue.append([s,e])
    visited = [[False]*c for _ in range(r)]
    visited[s][e] = True # 방문처리
    visited[m_x][m_y] = True # M의 좌표 방문처리
    
    while queue:
        x, y = queue.popleft()
        # 해당 좌표에 놓인 파이프가 어떤 파이프인지 알아야함
        pipe = graph[x][y]
        # Z인 경우 목적지에 도달하였음을 의미
        if pipe == 'Z':
            return True
        else: # Z가 아닌 경우 방향벡터 재확립
            # M은 될 수 없음 => M과 인접한 좌표에서 탐색을 시작하므로
            block_num = change[pipe] # 블록 번호로 변경
            dx = block[block_num][0]
            dy = block[block_num][1]
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                pipe = graph[nx][ny]
                # 다음으로 이동할 좌표가 '.'인지 확인
                if pipe == '.':
                    # 다음으로 이동해야할 좌표가 영역안에 존재하는데, '.'이라는 것은
                    # 해당 좌표가 타일이 사라진 좌표임을 의미한다.
                    return nx,ny
                # '.'이 아니라면 다음에 이동할 블록이 이동 가능한 블록인지 확인하고 이동하는 작업 수행
                # 이 단계에서는, 길이 있다면 이동할수있는 타일임이 보장되어 있으므로 그냥 큐에 삽입
                else:
                    visited[nx][ny] = True # 방문처리
                    queue.append([nx,ny])


# 끼워넣은 블록이 올바른지 확인하는 함수
def bfs(s,e):
    queue = deque()
    queue.append([s,e])
    visited = [[False]*c for _ in range(r)]
    visited[s][e] = True # 방문처리
    visited[m_x][m_y] = True # M 좌표 방문처리
    
    while queue:
        x, y = queue.popleft()
        # 해당 좌표에 놓인 파이프가 어떤 파이프인지 알아야함
        pipe = graph[x][y]
        # Z인 경우 목적지에 도달하였음을 의미
        if pipe == 'Z':
            return True
        else: # Z가 아닌 경우 방향벡터 재확립
            # M은 불가능
            block_num = change[pipe] # 블록 번호로 변경
            dx = block[block_num][0]
            dy = block[block_num][1]
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c:
                pipe = graph[nx][ny]
                # 다음으로 이동할 좌표가 '.'인지 확인
                if pipe == '.':
                    # '.'좌표로 이동하게 되었다 => 블록이 잘못 놓여졌다.
                    return False
                # '.'이 아니라면 다음에 이동할 블록이 이동 가능한 블록인지 확인하고 이동하는 작업 수행
                # 이 단계에서는, 길이 있다면 이동할수있는 타일임이 보장되어 있으므로 그냥 큐에 삽입
                # 다음에 이동할 좌표가 Z인지 확인하고 Z인 경우는 큐에 삽입
                elif pipe == 'Z':
                    queue.append([nx,ny])
                else:
                    if pipe =='M':
                        continue
                    # 현재 타일의 번호 확인
                    curr_num = change[graph[x][y]]
                    # 다음에 이동가능한 타일 목록 불러오기
                    can = pipe_candidate[curr_num][i]
                    # 다음에 이동할 타일의 번호 확인
                    next_num = change[graph[nx][ny]]
                    if next_num in can: # 이동 가능한 번호 목록에 있다면,아직 방문한적 없다면 이동
                        if not visited[nx][ny]:
                            visited[nx][ny] = True # 이동
                            queue.append([nx,ny]) # 값 삽입
                    else: # 이동가능한 번호 목록에 없다 => 파이프를 잘못설정했다
                        return False
            else: # 영역을 벗어나는 경우도 올바른 파이프라 할 수 없다.
                return False
    return False # 목적지까지 도달하지 못하였다.


r,c = map(int,input().split())

graph = [list(input()) for _ in range(r)]

# 먼저 M좌표를 찾아야함
find = False
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'M':
            m_x,m_y = i,j
            find = True
            break
    if find:
        break
    
# M(s,e)에서 바로 탐색을 시작하면 안됨
# M의 상하좌우 좌표에서 M과 이어져있는 좌표를 찾아서 그 좌표로 탐색해야함
dx = [-1,1,0,0]
dy = [0,0,-1,1]
candidate = [top,bottom,left,right]
for i in range(4):
    nx = m_x + dx[i]
    ny = m_y + dy[i]
    if 0<=nx<r and 0<=ny<c and graph[nx][ny] != '.':
        if graph[nx][ny] == 'Z':
            continue
        
        can = candidate[i]
        # 인접한 파이프가 M과 이어졌는지 확인
        pipe = change[graph[nx][ny]]
        if pipe in can:
            f_s,f_e = nx,ny
            break

# 문제가 있는 블록의 위치 찾기
t_x,t_y = find_block(f_s,f_e)

# 발견한 블록의 위치에 파이프들을 넣어보면서
# 모든 파이프를 방문하면서 목적지에 도달하는지 확인
for i in range(7):
    pipe = block_list[i]
    graph[t_x][t_y] = pipe # 해당 파이프로 설정하고
    # bfs 수행 => 모든 파이프를 다 방문하면서 목적지에 올바르게 도달했는지 검사
    if bfs(f_s,f_e): 
        # 지워진 블록의 행과 열 위치를 출력하고, 어떤 블록이었는지를 출력한다.
        print(t_x+1,t_y+1,pipe)
        sys.exit(0)
    graph[t_x][t_y] = '.'

