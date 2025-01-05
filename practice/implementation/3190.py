# https://www.acmicpc.net/problem/3190
from collections import deque

APPLE = 1
BLANK = 0
dx = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dy = [0, 1, 0, -1]

# 보드 크기
N = int(input())
board = [[BLANK] * N for _ in range(N)]

# 사과 위치 입력
for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = APPLE

# 방향 전환 입력
L = int(input())
commands = deque()
for _ in range(L):
    X, C = input().split()
    commands.append((int(X), C))

def in_range(x,y):
    return 0<=x<N and 0<=y<N

# 방향 변경 함수
def change_dir(d, cmd):
    return (d - 1) % 4 if cmd == 'L' else (d + 1) % 4

# 뱀 초기 상태
snake = deque([(0, 0)])
direction = 1  # 초기 방향 (우측)
time = 0
# 게임 진행
while True:
    time += 1
    head_x, head_y = snake[-1]  # 뱀의 머리 위치
    nx, ny = head_x + dx[direction], head_y + dy[direction]

    # 벽이나 자기 자신과 충돌하면 종료
    if not in_range(nx,ny) or (nx, ny) in snake:
        break

    # 사과가 있는 경우
    if board[nx][ny] == APPLE:
        board[nx][ny] = BLANK  # 사과 제거
        snake.append((nx, ny))  # 머리 위치 추가
    else:
        snake.append((nx, ny))  # 머리 위치 추가
        snake.popleft()  # 꼬리 제거

    # 방향 전환 명령 처리
    if commands and commands[0][0] == time:
        _, cmd = commands.popleft()
        direction = change_dir(direction, cmd)

print(time)
