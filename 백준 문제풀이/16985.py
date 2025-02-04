from collections import deque
from itertools import permutations
LENGTH = 5         # 판의 크기 (5×5)
VALID = 1          # 이동 가능한 칸의 값
MAX_INT = float('inf')
min_move_count = MAX_INT

def in_range(x, y, z):
    return 0 <= x < LENGTH and 0 <= y < LENGTH and 0 <= z < LENGTH

# 배열 회전
def rotate_arr(arr):
    new_arr = [[0]*LENGTH for _ in range(LENGTH)]
    for i in range(LENGTH):
        for j in range(LENGTH):
            new_arr[j][LENGTH-1-i] = arr[i][j]
    return new_arr
    
def bfs(maze):
    # 출발점과 도착점이 이동 가능한 칸인지 먼저 확인
    if maze[0][0][0] != VALID or maze[4][4][4] != VALID:
        return MAX_INT

    queue = deque()
    visited = [[[-1]*LENGTH for _ in range(LENGTH)] for _ in range(LENGTH)]
    sx, sy, sz = 0, 0, 0
    ex, ey, ez = 4, 4, 4
    visited[sx][sy][sz] = 0
    queue.append((sx, sy, sz))
    dxs = [-1, 1, 0, 0, 0, 0]
    dys = [0, 0, 1, -1, 0, 0]
    dzs = [0, 0, 0, 0, 1, -1]
    
    while queue:
        x, y, z = queue.popleft()
        if (x, y, z) == (ex, ey, ez):
            return visited[x][y][z]
        for dx, dy, dz in zip(dxs, dys, dzs):
            nx, ny, nz = x + dx, y + dy, z + dz
            if in_range(nx, ny, nz) and maze[nx][ny][nz] == VALID:
                if visited[nx][ny][nz] == -1:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    queue.append((nx, ny, nz))
    return MAX_INT  # 도달 불가능한 경우

def make_maze_and_move(new_board):
    global min_move_count
    for order in permutations(range(LENGTH), LENGTH):
        maze = [new_board[i] for i in order]
        min_move_count = min(min_move_count, bfs(maze))

def simulation():
    copy_board = [None] * LENGTH
    for i, rotate_count in enumerate(rotate):
        copy_board[i] = rotate_board[i][rotate_count]
    make_maze_and_move(copy_board)

# 각 판별 회전 횟수를 결정 (0: 회전 없음, 1: 90도, 2: 180도, 3: 270도)
rotate = [0] * LENGTH
def select_rotate(idx):
    if idx == LENGTH:
        simulation()
        return
    for i in range(4):
        rotate[idx] = i
        select_rotate(idx+1)
        rotate[idx] = 0
        # 조기 종료 조건 설정 - 12 이하로는 줄어들 수 없음
        if min_move_count == 12:
            return

board = [ [list(map(int, input().split())) for _ in range(LENGTH)] for _ in range(LENGTH) ]

# 원본 배열을 회전시켜놓은 결과 미리 저장
# rotate_board[i][k] => board[i]를 k번 회전시킨 결과 배열
rotate_board = [[] for _ in range(LENGTH)]
for i in range(LENGTH):
    # i번째 보드판에 대해서
    copy_arr = [b[:] for b in board[i]]
    rotate_board[i].append(copy_arr)
    for count in range(1,4):
        copy_arr = rotate_arr(copy_arr)
        rotate_board[i].append(copy_arr)

select_rotate(0)
print(-1 if min_move_count == MAX_INT else min_move_count)
