# https://www.acmicpc.net/problem/1799
'''
흰색과 흑색을 나눠서 생각
흰색칸의 경우 흑색 칸을 절대 공격할 수 없음
'''
import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
black_board = [b[:] for b in board] # 원본 배열 복사
white_board = [b[:] for b in board]

def make_board():
    global white_board,black_board    
    for i in range(N):
        for j in range(N):
            if (i+j)%2 == 0: # 같은 색 배열만 변경하기 위함
                black_board[i][j] = 0 # 흰색은 모두 비숍을 넣을 수 없는 위치로 생각
            else:
                white_board[i][j] = 0 # 검은색은 모두 비숍을 넣을 수 없는 위치로 생각
make_board() # 흰색, 검은색 배열 만들기

def can_put(x,y,vishops):
    for nx,ny in vishops: # 현재 비숍이 놓인 장소들을 대상으로 현재 위치에 비숍이 놓일 수 있는지 파악
        # 현재 칸에 비숍이 놓일 수 있는 조건은 왼쪽 위 대각선과 오른쪽 위 대각선에 비숍이 없을 것
        # 왼쪽 위 대각선의 경우 x-nx의 값과 y-ny의 값이 같으면 안됨
        if abs(x-nx) == abs(y-ny):
            return False # 놓을 수 없음
        # 오른쪽 위 대각선의 경우 (x+y)와 (nx+ny)가 같음
        if (x+y) == (nx+ny):
            return False
    return True # 그 밖의 경우는 가능함


def put_vishop(x, y, board, bishops):
    global results
    if x == N-1 and y == N:  # 끝까지 탐색을 마쳤다면 종료
        results.append(len(bishops))
        return
    if y == N: # 마지막 열까지 탐색을 마쳤다면 다음 행으로 이동
        put_vishop(x+1, 0, board, bishops)
        return
    # 현재 칸이 비숍을 놓을 수 있는지 탐색
    if board[x][y] == 1 and can_put(x, y, bishops): # 비숍을 놓을 수 있는지 현재까지 비숍이 놓인 곳을 대상으로 확인
        # 비숍을 놓을 수 있는 공간이라면
        # 1. 비숍을 놓지 않는다.
        put_vishop(x, y+1, board, bishops)
        # 2. 비숍을 놓는다.
        bishops.append((x, y))
        put_vishop(x, y+1, board, bishops)
        bishops.pop() # 백트래킹
    else: # 놓을 수 없다면 다음 칸으로 이동
        put_vishop(x, y+1, board, bishops)

results = []
put_vishop(0, 0, white_board, [])
white_count = max(results)

results = []
put_vishop(0, 0, black_board, [])
black_count = max(results)
print(white_count + black_count)