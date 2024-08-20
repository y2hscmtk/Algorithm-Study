# https://www.acmicpc.net/problem/26169
'''
5 x 5 칸
사과(1), 장애물(-1), 빈칸(0)
상 하 좌 우 이동 가능, 사과로 이동시 사과 1개 섭취
학생이 지나간 칸은 장애물 칸으로 변함(재방문 불가능)
세 번 이하의 이동으로 사과를 2개 이상 먹을 수 있다면 1, 불가능 하면 0을 출력
=> 백트래킹
'''
dx = [0,0,-1,1]; dy = [-1,1,0,0]
isSuccess = False # 성공 여부
def dfs(x,y,apple,count):
    global board, isSuccess
    if isSuccess: # 이미 성공했다면 탐색을 이어서 수행할 필요 없다
        return
    if count > 3:
        return # 3번 초과시 불가능한 케이스
    if apple >= 2: # 3번 이하 이동, 사과 2개 이상 섭취
        isSuccess = True # 성공 처리
        return
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i] 
        if 0<=nx<5 and 0<=ny<5 and board[nx][ny] != -1:
            a = board[nx][ny] # 사과 유무
            board[nx][ny] = -1 # 방문 처리
            dfs(nx,ny,apple+a,count+1)
            board[nx][ny] = a # 백트래킹(이전 상태로 복원)

board = [list(map(int,input().split())) for _ in range(5)]
r,c = map(int,input().split())
apple = 0
# 현재 위치 방문 처리, 사과 있는 위치에서 시작시 사과 섭취
if board[r][c] == 1:
    apple += 1
board[r][c] = -1 
dfs(r,c,apple,0)
print(1) if isSuccess else print(0)