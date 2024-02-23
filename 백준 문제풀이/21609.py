# https://www.acmicpc.net/problem/21609
'''
블록 그룹은 연결된 블록의 집합
그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다. 
검은색 블록은 그룹에 포함하면 안된다. 무지개 블록은 얼마나 들어있든 상관없다.
그룹에 포함된 블록의 개수는 2개 이상이어야 한다.
블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 여러개라면 열의 번호가 가장 작은 블록이다.
'''
from collections import deque
dx = [0,0,-1,1]; dy = [-1,1,0,0]
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
point = 0 # 획득한 포인트

# 2. 중력 알고리즘
# - 격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다. 
# - 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.
def gravity():
    global board
    # 0번째 열부터 반복
    # -1을 만나거나 인덱스가 0이 될 때까지 스택에 삽입하면서 내려가기
    # -1을 만날경우, -1의 위로 현재까지 쌓은 스택 빌때까지 뽑아서 쌓고 다음 칸으로 내려가서 반복
    # 인덱스가 0이 되면, 마찬가지로 여태까지 쌓은 값 쌓고 다음 열로 이동
    new_board = [[-2]*N for _ in range(N)]
    for c in range(N):
        stack = []
        for r in range(N):
            # 빈 공간은 무시
            if board[r][c] == -2:
                continue
            # -1을 만나기 전까지 삽입
            if board[r][c] != -1:
                stack.append(board[r][c])
            else: # -1을 만났다면
                new_board[r][c] = -1 # 검은 블록 그대로 남겨두고
                # 현재 칸 위로 스택 올리기
                x = 0
                while stack:
                    new_board[r-1-x][c] = stack.pop()
                    x+=1
                stack = [] # 스택 비우기
        # 스택 아직 남아있다면
        x = 0
        while stack:
            new_board[N-1-x][c] = stack.pop()
            x+=1
    board = new_board

# 3. 점수 채점 알고리즘
# - 블록 그룹에 해당하는 좌표들 모두 비우고, 
def get_point(selected_group):
    global point,board
    point += (selected_group[0]**2)
    position = selected_group[-1]
    for x,y in position:
        # 빈 공간은 -2로 표시
        board[x][y] = -2

# 4. 90도 회전 알고리즘
# - N x N 크기의 배열이므로 새로운 배열 생성후 갈아끼우는 방식으로
def rotate():
    global board
    new_board = [[-2]*N for _ in range(N)]
    for i in range(N):
        k = i
        for j in range(N):
            new_board[N-j-1][k] = board[i][j]
    board = new_board


def debug():
    print()
    for b in board:
        print(*b)

def bfs(s,e):
    global visited, group
    queue = deque()
    queue.append([s,e])
    visited[s][e] = True # 방문 처리
    position = []
    position.append((s,e))
    rainbow = 0 # 무지개 블록의 개수 카운팅
    # 자신의 색과 같은 블록만 넣을 수 있음
    sx,sy = s,e
    color = board[s][e]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] == color or board[nx][ny] == 0: # 무지개 블록 또는 같은 색이라면
                    if (nx,ny) not in position:
                        position.append((nx,ny))
                        visited[nx][ny] = True
                        queue.append([nx,ny])
                        if board[nx][ny] == 0: # 무지개 블록인 경우 카운팅
                            rainbow+=1
                        else: # 무지개 블록이 아닌 경우 기준좌표 업데이트
                            if nx<sx: # 행의 번호가 가장 작은 블록
                                sx,sy = nx,ny
                            elif nx==sx: # 그러한 블록이 여러개면 열의 번호가 가장 작은 블록
                                if ny<sy:
                                    sy = ny
    # 그룹에 속한 블록의 크기는 2 이상이어야 함
    if len(position) >= 2:
        # 그룹의 크기, 무지개 블록의 수, 기준블록 행, 기준블록 열
        group.append([len(position),rainbow,sx,sy,position])


# 검은색 블록(-1) 무지개 블록(0) 일반 블록(1)
# 이상의 자연수
while True:
    # 0. 블록 그룹을 탐색한다.
    # - 기존 그룹 저장소 비우고 찾기 시작
    group = []
    # - 방문 배열 확인후 방문하지 않은 장소라면
    # - 탐색 시작
    # - 결과물 확인후 배열에 그룹이 존재하지 않는다면 종료
    # - set 배열을 만들고 좌표를 기록하자.(무지개 블록 때문에 => 다른 그룹에도 속할 수 있음)
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] >= 1:
                # 방문하지 않았으며, 일반 블록인 경우에만 탐색
                bfs(i,j)
    if len(group) == 0: # 판별 결과 그룹이 존재하지 않으면 프로그램 종료
        print(point)
        break

    # 1. 블록 그룹 판별
    # 우선순위
    # - 블록 그룹의 크기
    # - 무지개 블록의 수
    # - 기준 블록의 행이 가장 큰 값
    # - 그 것도 여러개이면 열이 가장 큰 것
    group.sort(key = lambda x : (-x[0],-x[1],-x[2],-x[3]))
    # 2. 블록을 제거하고 포인트를 획득한다.
    get_point(group[0])
    # 3. 중력 작용
    gravity()
    # 4. 격자가 90도 반시계 방향으로 회전한다.
    rotate()
    # 5. 다시 중력 작용
    gravity()
