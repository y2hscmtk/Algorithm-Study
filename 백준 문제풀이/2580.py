# https://www.acmicpc.net/problem/2580
'''
입력이 0으로 주어진 영역에 대해서 1~9까지 수를 달리하며 조건을 만족하는지 백트래킹
'''
import sys
input = sys.stdin.readline
sudoku = []
position = []
for i in range(9):
    row = list(map(int,input().split()))
    for j in range(9):
        if row[j] == 0:
            position.append([i,j])
    sudoku.append(row)

# 사각형 영역에 대해서 검사
def squareCheck(x,y,target):
    # 3으로 나누면 몫은 0,1,2 => *3 => 0,3,6
    # x,y를 포함하고 있는 사각형 영역을 기준으로 검사
    for i in range(x//3*3, x//3*3+3):
        for j in range(y//3*3, y//3*3+3):
            if target == sudoku[i][j]:
                return False
    return True
                    
def rowCheck(x,target):
    for num in sudoku[x]: # x행의 모든 수들에 대해서
        if target == num: # 사용하고 싶은 수가 이미 사용중이라면
            return False
    return True

def colCheck(y,target):
    for i in range(9):
        num = sudoku[i][y] # 열 고정, 행 변환
        if target == num: # 사용하고 싶은 수가 이미 사용중이라면
            return False
    return True

# 숫자 채우기, 0의 개수만큼 숫자 채우기 작업 가능
def dfs(i):
    global sudoku
    # 모든 0에 숫자를 채웠다면
    if i == len(position):
        # 정답 출력
        for row in sudoku:
            print(*row)
        sys.exit()

    # 아직 숫자를 다 채우지 못했다면
    x,y = position[i] # 숫자를 채울 곳의 좌표
    for num in range(1,10):
        # 숫자를 넣기 전 행,열,사각형 영역 검사
        if rowCheck(x,num) and colCheck(y,num) and squareCheck(x,y,num):
            # num을 x,y 위치에 배치 가능하다면
            sudoku[x][y] = num
            dfs(i+1)
            sudoku[x][y] = 0 # 백트래킹
dfs(0)
