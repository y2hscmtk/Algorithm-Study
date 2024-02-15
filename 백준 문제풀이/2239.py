# https://www.acmicpc.net/problem/2239
'''
0인 칸에 대해서 1~9까지의 수 중에서 가능한 수 탐색
수를 넣는게 가능하다면 표 복사후 백 트래킹
'''
import sys
# 해당 수를 넣어도 되는지 안되는지
def can_put(number,x,y):
    # 행과 열의 영역에 따라서 어떤 영역을 3x3 영역으로 삼을지 계산해야함
    if 0<=x<3:
        start = 0
    elif 3<=x<6:
        start = 3
    elif 6<=x<9:
        start = 6
    if 0<=y<3:
        end = 0
    elif 3<=y<6:
        end = 3
    elif 6<=y<9:
        end = 6
    for i in range(start,start+3):
        for j in range(end,end+3):
            # 넣으려고 하는 수가 이미 존재하는지 확인
            if sudoku[i][j] == number:
                return False # 이미 존재한다면 넣을 수 없는 수임
            
    # 가로, 세로 살피기
    for i in range(9): # 가로 살피기
        if sudoku[x][i] == number:
            return False
    for j in range(9): # 세로 살피기
        if sudoku[j][y] == number:
            return False
    # 모두 통과했다면 넣을 수 있음
    return True


def put_number(depth):
    # 모든 빈 공간에 수를 다 넣었다면
    if depth == len(position):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j],end='')
            print("")
        sys.exit(0)
    # 1~9까지 수 중에 넣을 수 있는 수 탐색
    x,y = position[depth]
    for num in range(1,10):
        if can_put(num,x,y):
            sudoku[x][y] = num
            put_number(depth+1)
            # 백트래킹
            sudoku[x][y] = 0 
sudoku = []
position = []

for x in range(9):
    sudoku.append(list(map(int,input().rstrip())))
    for y in range(9):
        if sudoku[x][y] == 0: # 탐색을 수행할 빈 공간 배열에 삽입
            position.append([x,y])
put_number(0)