# https://www.acmicpc.net/problem/9663
'''
반복문을 돌면서 해당 위치에 퀸을 놓았을때 서로 공격할수 없는지 확인
N개를 놓는데 성공했다면 카운트+1
'''
N = int(input())
# 아무것도 없는 보드 생성
# 각
board = [0]*N

result = 0  # 퀸을 놓을 수 있는 방법의 수

# 왼쪽 위, 위, 오른쪽 위
dx = [-1, -1, -1]
dy = [-1, 0, 1]


# 이전 행들의 양 대각선과 위를 비교하면 됨
# 이후의 행들에 대해선 아직 퀸이 놓여지지 않은 상태이므로, 고려 대상이 아님
def able(row):
    # 현재 퀸의 위치
    # board[row] = col, (row,col)
    # 1. row이전의 행들을 돌면서 col과 같은 값이 있는지 확인
    # => col인 값이 있다면, 같은 열에 값이 있다는 의미니까
    col = board[row]
    for r in range(row):
        # 위 쪽               왼쪽 대각선                  오른쪽 대각선
        if board[r] == col or board[r] == col-(row-r) or board[r] == col+(row-r):
            return False
    return True


# 모든 좌표에 대해서 재귀적으로 퀸 N개 설치하기
def put_queen(row):
    global result, board
    # N개를 설치하였다면 정답 +1 하고 탈출
    # row번째 열까지 다 돌았다면~
    if row == N:
        result += 1
        return

    # 설치작업 수행
    # 같은 행에 여러개를 설치 할수 없음 => 각 행별로 한개씩 놓으면 됨
    # board = [0,2,3,1] => [0,0],[1,2],[2,3],[3,1]에 퀸이 있다는 의미
    for col in range(N):
        board[row] = col  # 퀸을 board[row][cow]에 놓는다.
        # row행 cow열에 퀸을 놓을 수 있는지 확인
        # row행 이전의 행들에 대해 확인
        if able(row):  # 가능하다면
            put_queen(row+1)  # 다음 열로 이동


# 퀸 놓기 시작
put_queen(0)
# 정답 출력
print(result)
