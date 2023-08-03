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
def up():
    global board
    # 각 세로줄을 고정시켜놓고 생각
    for j in range(N):
        index = 0  # 시작 인덱스
        for i in range(1, N):
            if board[i][j] != 0:  # 0인 경우는 무시
                # 숫자인 경우
                temp = board[i][j]  # 현재 숫자 저장
                board[i][j] = 0  # 댕겨올거니까 비우기

                if board[index][j] == 0:  # 0이 연속될 수 있으므로
                    board[index][j] = temp
                # 이전 숫자와 같은 숫자인지 확인
                elif temp == board[index][j]:  # 같다면
                    board[index][j] *= 2  # 2배 처리
                    index += 1  # 이전 index는 채워졌으니, 다음 위치 고려
                else:  # 같지 않다면
                    # 현재 인덱스의 옆칸에 값을 위치시켜야함
                    index += 1
                    board[index][j] = temp  # 숫자 당겨오기


def down():
    global board
    # 각 세로줄을 고정시켜놓고 생각
    for j in range(N):
        index = N-1  # 시작 인덱스
        # 두번째 아래에서 부터 확인
        for i in range(N-2, -1, -1):
            # 0인 경우는 무시
            if board[i][j] != 0:
                # 숫자인 경우
                temp = board[i][j]  # 현재 숫자 저장
                board[i][j] = 0  # 댕겨올거니까 비우기
                if board[index][j] == 0:  # 0이 연속될 수 있으므로
                    board[index][j] = temp
                # 이전 숫자와 같은 숫자인지 확인
                elif temp == board[index][j]:  # 같다면
                    board[index][j] *= 2  # 2배 처리
                    index -= 1  # 이전 index는 채워졌으니, 다음 위치 고려
                else:  # 같지 않다면
                    # 현재 인덱스의 옆칸에 값을 위치시켜야함
                    index -= 1
                    board[index][j] = temp  # 숫자 당겨오기


def left():
    global board
    # 가로줄은 고정, 세로줄을 달리하면서
    # board[i][ ] i 고정
    for i in range(N):
        # 시작 인덱스
        index = 0  # 0부터 차례로 채울것임
        for j in range(1, N):
            if board[i][j] != 0:
                # 0이 아닌경우
                temp = board[i][j]  # 값 저장
                board[i][j] = 0  # 댕겨올거니까 비우기

                if board[i][index] == 0:  # 0이 연속될 수 있으므로
                    board[i][index] = temp  # 이전 값이 0으로 비워져있다면 당겨오기
                # 이전 숫자와 같은 숫자인지 확인
                elif temp == board[i][index]:  # 같다면
                    board[i][index] *= 2  # 2배 처리
                    index += 1  # 이전 index는 채워졌으니, 다음 위치 고려
                else:  # 같지 않다면
                    # 현재 인덱스의 옆칸에 값을 위치시켜야함
                    index += 1
                    board[i][index] = temp  # 숫자 당겨오기


def right():
    global board
    # 가로줄은 고정, 세로줄을 달리하면서
    # board[i][ ] i 고정
    for i in range(N):
        # 시작 인덱스
        index = N-1  # 끝에서 부터 채울것임
        for j in range(N-2, -1, -1):
            if board[i][j] == 0:  # 0인경우 무시
                continue
            # 0이 아닌경우
            temp = board[i][j]  # 값 저장
            board[i][j] = 0  # 댕겨올거니까 비우기

            if board[i][index] == 0:  # 0이 연속될 수 있으므로
                board[i][index] = temp  # 이전 값이 0으로 비워져있다면 당겨오기
            # 이전 숫자와 같은 숫자인지 확인
            elif temp == board[i][index]:  # 같다면
                board[i][index] *= 2  # 2배 처리
                index -= 1  # 이전 index는 채워졌으니, 다음 위치 고려
            else:  # 같지 않다면
                # 현재 인덱스의 옆칸에 값을 위치시켜야함
                index -= 1
                board[i][index] = temp  # 숫자 당겨오기


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
