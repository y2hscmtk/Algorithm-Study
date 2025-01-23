'''
n x n 칸
8개의 방향
각 칸은 중복 없는 숫자

특정 위치에서 시작, 현재 위치에 적혀있는 방향에 있는 숫자들 중, 
현재 숫자보다 더 큰 숫자가 있는 곳으로 이동 최대한 많이 반복하는 것이 목표
'''
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
direction = [list(map(int,input().split())) for _ in range(n)]

# 이동할 방향 정의
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

# 탐색 시작 위치
x, y = map(int,input().split())
max_move_count = 0 # 최대 이동 가능 횟수

def in_range(x,y):
    return 0<=x<n and 0<=y<n


def backtracking(x,y,move_count):
    global max_move_count
    # 이동 횟수는 매번 갱신
    max_move_count = max(max_move_count, move_count)

    curr_num = grid[x][y] # 현재 칸에 적힌 숫자
    d = direction[x][y] # 현재 칸에서의 이동 방향

    # 현재 칸에서 이동 가능한 영역 탐색
    while True:
        nx,ny = x + dx[d-1], y + dy[d-1]
        if not in_range(nx,ny):
            break
        # 현재 칸에서 이동가능한지 확인
        if curr_num <= grid[nx][ny]:
            backtracking(nx,ny,move_count+1)
        x,y = nx,ny
    

backtracking(x-1,y-1,0)

print(max_move_count)