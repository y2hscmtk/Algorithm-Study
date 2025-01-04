# https://www.acmicpc.net/problem/14503
'''
n,m 크기의 방안 
처음에 빈 칸은 전부 청소되지 않은 상태이다. -> 청소 여부 확인을 위한 배열 필요
북 동 남 서 
'''
DIRTY = 0
BLOCK = 1
CLEAN = 2 # 청소 완료된 칸
n,m = map(int,input().split())
x,y,d = map(int,input().split()) # 청소기 초기 위치, 초기 방향 

grid = [list(map(int,input().split())) for _ in range(n)]

# 방향 벡터 : 북 동 남 서
dx = [-1,0,1,0]; dy = [0,1,0,-1]

# 총 몇칸이 청소되었는지 판단하는 함수
def get_clean_area():
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == CLEAN:
                count += 1
    return count

# 영역 검사
def in_range(x,y):
    return 0<=x<n and 0<=y<m

# 현재 칸 기준 상하좌우 4칸 중 청소되지 않은 칸이 있는지 판단한다
def is_dirty(x,y): 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 청소되지 않은 영역이 존재한다면
        if in_range(nx,ny) and grid[nx][ny] == DIRTY: 
            return True # 청소되지 않은 영역이 존재한다.
    return False # 모든 방향 청소를 완료했다.

# 현재 방향의 반대 방향을 얻는다.
def get_reverse_dir(d):
    return (d+2)%4

# 현재 위치에서 반시계 방향으로 회전할때의 방향
def get_next_dir(d):
    d-=1
    if d == -1:
        d = 3
    return d

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if grid[x][y] == DIRTY:
        grid[x][y] = CLEAN # 청소
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우 - 모두 청소된 경우
    if not is_dirty(x,y):
        next_d = get_reverse_dir(d)
        nx = x + dx[next_d]
        ny = y + dy[next_d]
        # 후진 가능하다면 한칸 후진하고, 1번으로 돌아간다.
        if in_range(nx,ny) and grid[nx][ny] != BLOCK:
            x = nx
            y = ny
        else: # 벽이라 후진할 수 없다면 작동을 중지한다.
            break
    else: # 3. 청소되지 않은 빈 칸이 있는 경우 - 현재 칸을 기준으로 반시계방향으로 회전하며 청소되지 않은 영역으로 이동
        for _ in range(4):
            d = get_next_dir(d)
            nx = x + dx[d]
            ny = y + dy[d]
            if in_range(nx,ny) and grid[nx][ny] == DIRTY:
                x = nx
                y = ny
                break

print(get_clean_area())