# https://www.acmicpc.net/problem/12100
'''
상,하,좌,우 로 이동할때에 대한 함수를 각각 구현해놓고
백트래킹과 브루트포스를 이용하여 모든 경우의 수에 대해 탐색하고 최대 점수를 업데이트한다.
'''
N = int(input())  # 보드의 크기
# 현재 보드 상태
board = [list(map(int, input().split())) for i in range(N)]
result = 0  # 정답 출력용


# 각 방향에 대한 함수 작성
# 위로 움직일때
def up():
    global board
    # 각 세로 줄에 대해서 판별 시작
    # 0 1 2 3 번 줄로 명명
    for i in range(N):
        # board[j][i] # i고정 시키고, j값 바꾸면서
        last_num, index = board[0][i], 0
        for j in range(1, N):
            # 각 세로줄을 살피면서 숫자 압축
            # 빈 공간을 만나면 건너뛰기
            if board[j][i] == 0:
                continue
            # 숫자를 만날경우
            # 이전 숫자와 같은 숫자인지 확인하고 같은 숫자라면 숫자 합치고, 현재 숫자는 0으로 기록
            elif board[j][i] > 0:
                if last_num == board[j][i]:
                    board[index][i] = board[index][i] + last_num  # 숫자 합치기
                    board[j][i] = 0  # 합쳤으니까 빈공간으로 처리
                    last_num, index = 0, 0  # 이전 숫자는 다시 0으로 기록
                else:  # 같지 않다면
                    # 이전숫자와, 인덱스를 현재 숫자로 변경
                    last_num, index = board[j][i], j
    # 돌면서 리스트에 삽입
    numbers = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[j][i] > 0:
                numbers[i].append(board[j][j])
    # 한쪽으로 몰아 넣기
    for i in range(N):
        for k in range(len(numbers[i])):
            board[k][i] = numbers[i][k]
        # 숫자 아닌부분 0으로 채우기
        for j in range(len(numbers[i]), N):
            board[j][i] = 0


def down():
    global board
    # 각 세로 줄에 대해서 판별 시작
    # 0 1 2 3 번 줄로 명명
    for i in range(N):
        # board[j][i] # i고정 시키고, j값 바꾸면서
        last_num, index = board[N-1][i], N-1
        for j in range(N-2, -1, -1):
            # 각 세로줄을 살피면서 숫자 압축
            # 빈 공간을 만나면 건너뛰기
            if board[j][i] == 0:
                continue
            # 숫자를 만날경우
            # 이전 숫자와 같은 숫자인지 확인하고 같은 숫자라면 숫자 합치고, 현재 숫자는 0으로 기록
            elif board[j][i] > 0:
                if last_num == board[j][i]:
                    board[index][i] = board[index][i] + last_num  # 숫자 합치기
                    board[j][i] = 0  # 합쳤으니까 빈공간으로 처리
                    last_num, index = 0, 0  # 이전 숫자는 다시 0으로 기록
                else:  # 같지 않다면
                    # 이전숫자와, 인덱스를 현재 숫자로 변경
                    last_num, index = board[j][i], j
    # 돌면서 리스트에 삽입
    numbers = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N-1, -1, -1):
            if board[j][i] > 0:
                numbers[i].append(board[j][j])
    # 한쪽으로 몰아 넣기
    for i in range(N):
        for k in range(len(numbers[i])):
            board[N-k-1][i] = numbers[i][k]
        # 숫자 아닌부분 0으로 채우기
        for j in range(len(numbers[i]), N):
            board[N-j-1][i] = 0


def left():
    global board
    # 각 가로 줄에 대해서 판별 시작
    # 0 1 2 3 번 줄로 명명
    for i in range(N):  # 가로 줄 고정
        # board[i][j] # i고정 시키고, j값 바꾸면서
        last_num, index = board[i][0], 0
        for j in range(1, N):
            # 각 가로줄 살피면서 숫자 압축
            # 빈 공간을 만나면 건너뛰기
            if board[i][j] == 0:
                continue
            # 숫자를 만날경우
            # 이전 숫자와 같은 숫자인지 확인하고 같은 숫자라면 숫자 합치고, 현재 숫자는 0으로 기록
            elif board[i][j] > 0:
                if last_num == board[i][j]:
                    board[i][index] = board[i][index] + last_num  # 숫자 합치기
                    board[i][j] = 0  # 합쳤으니까 빈공간으로 처리
                    last_num, index = 0, 0  # 이전 숫자는 다시 0으로 기록
                else:  # 같지 않다면
                    # 이전숫자와, 인덱스를 현재 숫자로 변경
                    last_num, index = board[i][j], j
    # 돌면서 리스트에 삽입
    numbers = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                numbers[i].append(board[i][j])
    # 한쪽으로 몰아 넣기
    for i in range(N):
        for k in range(len(numbers[i])):
            board[i][k] = numbers[i][k]
        # 숫자 아닌부분 0으로 채우기
        for j in range(len(numbers[i]), N):
            board[i][j] = 0


def right():
    global board
    # 각 가로 줄에 대해서 판별 시작
    # 0 1 2 3 번 줄로 명명
    for i in range(N):  # 가로 줄 고정
        # board[i][j] # i고정 시키고, j값 바꾸면서
        last_num, index = board[i][N-1], N-1
        for j in range(N-2, -1, -1):
            # 각 가로줄 살피면서 숫자 압축
            # 빈 공간을 만나면 건너뛰기
            if board[i][j] == 0:
                continue
            # 숫자를 만날경우
            # 이전 숫자와 같은 숫자인지 확인하고 같은 숫자라면 숫자 합치고, 현재 숫자는 0으로 기록
            elif board[i][j] > 0:
                if last_num == board[i][j]:
                    board[i][index] = board[i][index] + last_num  # 숫자 합치기
                    board[i][j] = 0  # 합쳤으니까 빈공간으로 처리
                    last_num, index = 0, 0  # 이전 숫자는 다시 0으로 기록
                else:  # 같지 않다면
                    # 이전숫자와, 인덱스를 현재 숫자로 변경
                    last_num, index = board[i][j], j
    # 돌면서 리스트에 삽입
    numbers = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N-1, -1, -1):
            if board[i][j] > 0:
                numbers[i].append(board[i][j])
    # 한쪽으로 몰아 넣기
    for i in range(N):
        for k in range(len(numbers[i])):
            board[i][N-k-1] = numbers[i][k]
        # 숫자 아닌부분 0으로 채우기
        for j in range(len(numbers[i]), N):
            board[i][N-j-1] = 0


# 설정된 방향으로 게임 수행
def start_game(direction):
    global result
    for d in direction:
        if d == 0:  # up
            up()
        elif d == 1:  # down
            down()
        elif d == 2:  # left
            left()
        elif d == 3:  # right
            right()
    # 설정한 방향으로 게임을 마친 후 점수 갱신
    update()


# 현재 보드판에서의 블록의 최고 점수 갱신
def update():
    global result
    for scores in board:
        result = max(result, max(scores))


# 백트래킹을 통해 최대값 갱신 시작
def set_game(count, direction):
    global board
    # 방향 5개가 모두 결정되었다면 게임 시작
    if count == 5:
        # 현재 상태를 기록해두고
        backup = [b[:] for b in board]
        start_game(direction)  # 게임을 실행하여 값 갱신한 후
        # 원래 상태로 되돌아오기
        board = [b[:] for b in backup]
        return

    # 상 상 상 상 상
    # 상 상 상 상 하
    # .... 모든 방향에 대해서 수행
    # 0 : 상, 1 : 하, 2 : 좌, 3 : 우
    for i in range(4):
        direction.append(i)
        set_game(count+1, direction)
        direction.pop()


# 모든 경우의 수에 대해 게임 수행
set_game(0, [])
# 결과 출력
print(result)
