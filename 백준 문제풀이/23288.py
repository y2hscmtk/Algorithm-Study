# https://www.acmicpc.net/problem/23288
'''
<주사위 굴리기2>
** 오른쪽 동쪽, 위쪽은 북쪽
좌표는 r,c로 나타내며 가장 왼쪽 위의 좌표는 ** (1,1) 

주사위는 윗면이 1이고 동쪽을 바라보는 방향이 3인 상태로 놓여져 있음, 놓여진 곳의 좌표는 (1,1)
지도의 각 칸에도 정수가 하나씩 존재, 가장 처음 주사위의 이동방향은 동쪽
'''
import sys
from collections import deque
input = sys.stdin.readline
# 가장 처음 이동하는 방향은 동쪽
# 90도 이동방향을 고려하여 동(0)->남(1)->서(2)->북(3) 방향으로 이동할 수 있도록 설계
dx = [0,1,0,-1]; dy = [1,0,-1,0]

N,M,K = map(int,input().split())
point = [[-1 for _ in range(M)] for _ in range(N)]

board = [list(map(int,input().split())) for _ in range(N)]

'''
칸 (x, y)에 대한 점수는 다음과 같이 구할 수 있다. 
(x, y)에 있는 정수를 B라고 했을때, (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다. 
이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다. 여기서 점수는 B와 C를 곱한 값이다.
'''
def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))
    # 점수 = count * 현재 칸에 적힌 수
    B = board[sx][sy]
    count = 1 # 연속한 숫자가 몇개 있는지 파악하기 위함
    point[sx][sy] = 0
    temp = [(sx,sy)]
    while queue:
        x,y = queue.popleft()
        for nx,ny in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
            # 영역 검사
            if 0<=nx<N and 0<=ny<M and point[nx][ny] == -1:
                # 조건 검사 : 같은 숫자인지 확인
                if board[nx][ny] == B:
                    point[nx][ny] = 0 # 방문 처리
                    count += 1 # 개수 증가
                    queue.append((nx,ny))
                    temp.append((nx,ny))
    
    # 포인트 계산
    result_point = B * count
    # 같은 숫자를 가진 모든 칸에 대해
    for x,y in temp:
        point[x][y] = result_point
        
# 아직 점수가 기록되지 않은 칸을 찾아서 기록해둔다.
for i in range(N):
    for j in range(M):
        if point[i][j] == -1:
            bfs(i,j)


'''
주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
'''
# 현재 주사위의 위치에서 탐색 시작
def dice_move(x,y):
    global dice_x,dice_y,bottom,dir,total_point
    # 이동방향이 바뀌는지 확인
    A = bottom # 현재 주사위 바닥에 있는 숫자
    top = 7-bottom # 주사위 위쪽에 있는 숫자
    B = board[x][y] # 게임판의 바닥에 적힌 숫자
    # A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    if A > B:
        dir = (dir+1)%4
    # A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    elif A < B:
        dir-=1
        if dir == -1:
            dir = 3
    # A = B인 경우 이동 방향에 변화 없음
    
    # 다음에 주사위가 이동하려고 하는 칸
    nx = x + dx[dir]; ny = y + dy[dir]
    # 주사위가 이동 방향으로 한 칸 굴러간다. 만약, ** 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    if nx<0 or nx>=N or nx<0 or ny>=M:
        if dir == 0:
            dir = 2
        elif dir == 2:
            dir = 0
        elif dir == 1:
            dir = 3
        elif dir == 3:
            dir = 1
        # 이동방향 정반대로 변경 후 한칸 굴러간다.
        nx = x + dx[dir]; ny = y + dy[dir]

    # 주사위 위치 변경
    dice_x = nx; dice_y = ny

    turn_dice[dir] # 주사위 이동
    bottom = 7 - dice[0]
    
    # 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    total_point += point[dice_x][dice_y]
    return

'''
초기 상태 : [1,5,6,2,4,3]
1. 동쪽으로 돌릴 때 : [4,5,3,2,6,1]
2. 서쪽으로 돌릴 때 : [3,5,4,2,1,6]
3. 북쪽으로 돌릴 때 : [5,6,2,1,4,3]
4. 남쪽으로 돌릴 때 : [2,1,5,6,4,3]
'''
dice = [1,5,6,2,4,3]
def turn_0(): # 동쪽으로 굴리기
    global dice
    new_dice = [dice[4],dice[1],dice[5],dice[3],dice[2],dice[0]]
    dice = new_dice
def turn_1(): # 남쪽으로 굴리기
    global dice
    new_dice = [dice[3],dice[0],dice[1],dice[2],dice[4],dice[5]]
    dice = new_dice
def turn_2(): # 서쪽으로 굴리기
    global dice
    new_dice = [dice[5],dice[1],dice[4],dice[3],dice[0],dice[2]]
    dice = new_dice
def turn_3(): # 북쪽으로 굴리기
    global dice
    # [1,5,6,2,4,3] -> [5,6,2,1,4,3]
    new_dice = [dice[1],dice[2],dice[3],dice[0],dice[4],dice[5]]
    dice = new_dice

turn_dice = [turn_0,turn_1,turn_2,turn_3]

# 첫번째 이동방향은 동쪽이고, 영향을 끼치지 않으므로 이미 이동했다고 가정한다.
dice_x,dice_y,bottom = 0,1,3
total_point = point[0][1] # 총 획득 가능 포인트
dir = 0 # 처음 이동 방향은 동쪽이다.
turn_dice[0] # 동쪽 이동
K -= 1
while K>0: # K만큼 수행
    dice_move(dice_x,dice_y)
    K -= 1 # 이동 가능 횟수를 1 줄인다.
print(total_point)


