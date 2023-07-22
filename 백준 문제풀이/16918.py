# https://www.acmicpc.net/problem/16918
from collections import deque

R, C, N = map(int, input().split())

# 현재 격자판의 상태
# 빈 칸은 '.'로, 폭탄은 'O'로 주어진다.
board = [list(input()) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


bomb_queue = deque()


# 격자판의 상태 변경
def change():
    global board
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 0  # 빈 공간
            if board[i][j] == 'O':
                board[i][j] = 1


# 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
# 폭탄에만 시간 더하기
def add_time():
    global board, time
    time += 1  # 전체시간 +1초
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:
                board[i][j] += 1


# 폭탄 설치 => 폭탄이 없는곳에 폭탄 설치
def put_bomb():
    global board, time
    time += 1  # 전체시간 +1초
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                board[i][j] = 1


# 격자판의 상태 출력 함수
def print_board():
    # -1은 '.'으로, 양수는 'O'으로 바꿔서 출력
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                print('.', end='')
            elif board[i][j] >= 1:
                print('O', end='')
        print()


# 곧 터질 폭탄을 찾는다 2인 폭탄
def find_bomb():
    global bomb_queue
    for i in range(R):
        for j in range(C):
            if board[i][j] == 3:
                bomb_queue.append([i, j])


# 폭탄 터뜨리기
def destroy():
    global bomb_queue, board, time
    while bomb_queue:
        x, y = bomb_queue.popleft()
        board[x][y] = 0  # 현재 위치 폭탄 터뜨리기
        # 네방향 폭탄 터뜨리기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                # 폭탄인 경우에만 처리
                # 폭탄이 터지면 빈 공간이 되므로, 이미 빈 공간인 경우는 처리할 필요 없음
                if board[nx][ny] != 0:
                    board[nx][ny] = 0


time = 0
# N이 1초면 그냥 정답 출력
# 1. 처음엔 아무것도 안한다.
if N == 1:
    for b in board:
        print(''.join(b))
else:  # 2초 이상인 경우
    change()

    # 2. 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
    add_time()  # 아무것도 하지 않으므로 폭탄에만 시간이 더해진다.
    # 3번과 4번 반복
    while time != N:
        # 3. 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다.
        put_bomb()
        # 시간이 1초가 흘렀으므로 확인한다.
        if time == N:
            break
        # 4. 1초가 지난후에
        add_time()
        # 3초전에 설치된 모든 폭탄이 폭발한다.
        # 3초인 것들을 찾아 큐에 넣고
        find_bomb()
        # 큐에 있는 폭탄을 터뜨린다. # 1초 소요
        destroy()

    print_board()
