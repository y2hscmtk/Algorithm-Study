# https://www.acmicpc.net/problem/23290
'''
4 4 크기의 격자
왼쪽 위 좌표는 (1,1), 오른쪽 아래 좌표는 (4,4)
물고기 M마리 존재, 각 물고기는 8가지 이동방향을 가지고 있다.
둘 이상의 물고기가 같은 칸에 존재할 수 있으며, 마법사 상어도 격자에 존재에 위치한다.

상어의 연습 1번은 아래 작업이 순차적으로 진행된다.
1. 상어가 모든 물고기에게 복제 마법을 시전한다.
복제 마법은 시간이 조금 걸리기 때문에, 아래 5번에서 물고기가 복제되어 칸에 나타난다.

2. 모든 물고기가 한 칸 이동한다. 
상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다. 
각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 
만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. 
물고기의 냄새는 아래 3에서 설명한다.

3. 상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다. 
연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다. 
연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 그 칸에 있는 모든 물고기는 격자에서 제외되며,
제외되는 모든 물고기는 물고기 냄새를 남긴다. 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 
그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다. 사전 순에 대한 문제의 하단 노트에 있다.

4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다. - 냄새 제거 함수 작성

5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.

격자에 있는 물고기의 위치, 방향 정보와 상어의 위치, 그리고 연습 횟수 S가 주어진다. 
S번 연습을 모두 마쳤을때, 격자에 있는 물고기의 수를 구해보자.

시뮬레이션, 구현
'''
BLANK,SHARK = 0,100
N = 4
M,S = map(int,input().split())
# 상어의 위치, 냄새 정보 저장용
status = [[BLANK]*N for _ in range(N)]
# 물고기의 위치 표시용
board = [[[] for _ in range(N)] for _ in range(N)]
next_board = [[[] for _ in range(N)] for _ in range(N)]

def in_range(x,y): # 영역 검사
    return 0<=x<N and 0<=y<N

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0,-1,-1, -1,0,1,1, 1]
dy = [-1,-1,0,  1,1,1,0,-1]
s_dx = [-1,0,1,0]
s_dy = [0,-1,0,1]

for _ in range(M):
    x,y,d = map(int,input().split())
    board[x-1][y-1].append([d-1,True]) # 해당 물고기가 살아있는지 여부

sx,sy = map(int,input().split())
sx,sy = sx-1,sy-1

shark_dir = []

# 최종적으로 남아있는 물고기 수 카운팅
def count_fish():
    count = 0
    for i in range(N):
        for j in range(N):
            for _,is_alive in board[i][j]:
                if is_alive:
                    count += 1
    return count

# 두번 전 연습에서의 냄새를 제거해야함
def delete_smell(target):
    for i in range(N):
        for j in range(N):
            if status[i][j] == target:
                status[i][j] = 0

# 특정 칸에 물고기가 몇마리인지 확인
def get_fish_count(x,y):
    count = 0
    for d,is_alive in next_board[x][y]:
        if is_alive:
            count += 1
    return count

def dfs(x,y,fish_count):
    global next_board
    if len(dir) == 3: # 이동할 방향 3곳을 모두 정한 경우
        shark_dir.append((fish_count,dir[:]))
        return
    
    for i in range(4):
        nx,ny = x + s_dx[i], y + s_dy[i]
        # 이동하려는 칸은 격자를 벗어나면 안된다.
        if not in_range(nx,ny):
            continue
        # 상어는 영역만 벗어나지 않으면 어떤 칸이든 이동 가능
        dir.append(i)
        # 임시로 물고기 사망 처리
        count = 0
        find = False
        for k in range(len(next_board[nx][ny])):
            d,is_alive = next_board[nx][ny][k]
            if is_alive:
                count += 1
                find = True
                next_board[nx][ny][k] = [d,False]
        dfs(nx,ny,fish_count+count)
        # 백트래킹
        if find:
            for k in range(len(next_board[nx][ny])):
                next_board[nx][ny][k][1] = True # 모두 생존 상태로 변경
        dir.pop()

# *************
# 경우의 수는 최대 64개
# 모든 방향으로 이동 설정 후, 잡은 물고기 순으로 내림차순
def shark_move(t):
    global sx,sy,dir,next_board
    # 3. 상어는 상하좌우중 한 방향으로 3칸이동
    # 3.1. 이동과정 중에 격자를 넘어서게 된다면 그 방향으로는 이동 불가
    # 3.2. 이동 방향에 물고기가 있다면, 해당 물고기는 제거됨
    # 3.3. 가장 물고기를 많이 제거할 수 있는 방향을 선택
    dir = []
    
    dfs(sx,sy,0)
    
    # 물고기가 가장 많이 제거된 칸 선별
    shark_dir.sort(reverse=True, key=lambda x : x[0])
    _,dir = shark_dir[0]
    
    for nd in dir:
        nx,ny = sx + s_dx[nd], sy + s_dy[nd]
        # 해당 위치의 모든 물고기 제거
        find = False
        for i in range(len(next_board[nx][ny])):
            find = True
            next_board[nx][ny][i][1] = False # 제거 처리
        if find: # 해당 위치에 물고기가 있었다면
            status[nx][ny] = t # 냄새 처리
        sx,sy = nx,ny
    # 상어의 냄새를 기록하면, 물고기 냄새와 겹쳐지므로 별도로 기록할 필요없이 좌표로 관리

# 다음에 이동할 좌표, 이동할 방향 반환
def get_next_pos(x,y,d):
    # 현재 방향이 이동가능한 방향인지 확인
    # 상어가 없고, 냄새가 없고, 영역을 벗어나지 않는 빈칸으로 이동 가능
    nx,ny = x + dx[d], y + dy[d]
    if in_range(nx,ny) and status[nx][ny] == BLANK and (nx,ny) != (sx,sy):
        return (nx,ny,d)
    # 원하는 방향을 찾을 때 까지,반시계 방향으로 회전
    nd = d
    while True:
        nd = nd-1
        if nd == -1:
            nd = 7
        nx,ny = x + dx[nd], y + dy[nd]
        if in_range(nx,ny) and status[nx][ny] == BLANK and (nx,ny) != (sx,sy):
            return (nx,ny,nd)
        if d == nd: # 이동가능한 방향이 없는 경우
            return (x,y,d)

def practice(t,target):
    global shark_dir,board,next_board
    # 1. 복제 마법 시전 - 현재 물고기 정보 배열 복사해두기
    copy_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for d,is_alive in board[i][j]:
                copy_board[i][j].append([d,is_alive])
    
    # 2. 모든 물고기 이동 - next_board 배열 준비
    next_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for d,is_alive in board[i][j]:
                if not is_alive:
                    continue
                #   2.0. 올바른 이동방향 파악 - 이동 불가능 하다면 가만히 있기
                #   2.1. 비어있는 칸으로만 이동 가능(status)
                nx,ny,nd = get_next_pos(i,j,d)
                next_board[nx][ny].append([nd,is_alive])
    
    # 상어 움직임 수행
    shark_dir = [] # 상어 방향 배열 초기화
    shark_move(target)
    
    # 4. 두번 전 연습에서 생긴 물고기의 냄새가 사라진다
    delete_smell(t) # t로 표시된 냄새들 제거
    
    # 5. 물고기의 복제가 완료된다.
    # next_board의 물고기, copy_board의 물고기 정보 병합
    board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for d,is_alive in copy_board[i][j]:
                board[i][j].append([d,is_alive])
            for d,is_alive in next_board[i][j]:
                if is_alive:
                    board[i][j].append([d,is_alive])


# S번 연습 수행
for t in range(S):
    practice(t,t+2) # 현재 상태, 냄새 표시 상태

print(count_fish())