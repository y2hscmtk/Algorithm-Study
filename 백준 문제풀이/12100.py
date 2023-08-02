# https://www.acmicpc.net/problem/12100
'''
상,하,좌,우 로 이동할때에 대한 함수를 각각 구현해놓고
백트래킹과 브루트포스를 이용하여 모든 경우의 수에 대해 탐색하고 최대 점수를 업데이트한다.
'''
N = int(input()) # 보드의 크기
# 현재 보드 상태
board = [list(map(int,input().split())) for i in range(N)] 
result = 0 # 정답 출력용
# 각 방향에 대한 함수 작성
# 위로 움직일때
def up():
    global board
    print("up",end=' ')

def down():
    global board
    print("down",end=' ')

def left():
    global board
    print("left",end=' ')

def right():
    global board
    print("right",end=' ')

# 설정된 방향으로 게임 수행
def start_game(direction):
    global result
    for d in direction:
        if d == 0: # up
            up()
        elif d == 1: # down
            down()
        elif d == 2: # left
            left()
        elif d == 3: # right
            right()
    result += 1
    print("")


# 현재 보드판에서의 블록의 최고 점수 갱신
def update():
    global result
    for scores in board:
        result = max(result,max(scores))


# 백트래킹을 통해 최대값 갱신 시작
def set_game(count,direction):
    global board
    # 방향 5개가 모두 결정되었다면 게임 시작
    if count == 5:
        # 현재 상태를 기록해두고
        backup = [b[:] for b in board]
        start_game(direction) # 게임을 실행하여 값 갱신한 후
        # 원래 상태로 되돌아오기
        board = [b[:] for b in backup]
        return

    # 상 상 상 상 상
    # 상 상 상 상 하
    # .... 모든 방향에 대해서 수행
    # 0 : 상, 1 : 하, 2 : 좌, 3 : 우
    for i in range(4):
        direction.append(i)
        set_game(count+1,direction)
        direction.pop()

# 모든 경우의 수에 대해 게임 수행
set_game(0,[])
# 결과 출력
print(result)

