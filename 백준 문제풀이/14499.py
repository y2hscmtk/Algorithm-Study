'''
각 숫자들에 대한 참조로 주사위 인위로 조정
주사위를 굴렸을 때 각 숫자의 인덱스가 어떻게 변화하는지 계산해야함
이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
초기 상태 : [1,2,3,4,5,6]
1. 동쪽으로 돌릴 때 : [4,2,1,6,5,3]
2. 서쪽으로 돌릴 때 : [3,2,6,1,5,4]
3. 북쪽으로 돌릴 때 : [5,1,3,4,6,2]
4. 남쪽으로 돌릴 때 : [2,6,3,4,1,5]
'''
N,M,x,y,k = map(int,input().split())
dice = [0,0,0,0,0,0]
def turn_1(): # 동쪽으로 굴리기
    global dice
    # [1,2,3,4,5,6] -> [4,2,1,6,5,3]
    new_dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    dice = new_dice
def turn_2(): # 서쪽으로 굴리기
    global dice
    # [1,2,3,4,5,6] -> [3,2,6,1,5,4]
    new_dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    dice = new_dice
def turn_3(): # 북쪽으로 굴리기
    global dice
    # [1,2,3,4,5,6] -> [5,1,3,4,6,2]
    new_dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    dice = new_dice
def turn_4(): # 남쪽으로 굴리기
    global dice
    # [1,2,3,4,5,6] -> [2,6,3,4,1,5]
    new_dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    dice = new_dice

turn = [turn_1,turn_2,turn_3,turn_4]
board = [list(map(int,input().split())) for _ in range(N)]
commands = list(map(int,input().split())) # 명령들
dx = [0,0,-1,1]; dy = [1,-1,0,0] # 동서북남 1,2,3,4
for command in commands:
    command-=1
    nx = x + dx[command]; ny = y + dy[command]
    if 0<=nx<N and 0<=ny<M: # 이동 가능하다면
        turn[command]() # 회전하기
        # 해당 칸으로 이동
        x = nx; y = ny
        # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면
        if board[x][y] == 0:
            board[x][y] = dice[5] # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. (바닥면은 5번째 인덱스)
        else: # 0이 아닌 경우에는 칸에 쓰여있는 수가 바닥면으로 복사된다.
            dice[5] = board[x][y]
            board[x][y] = 0 # 칸에 쓰여있는 수는 0이 된다.
        # 주사위가 이동했을 때 마다 상단에 쓰여있는 값을 구한다.
        print(dice[0]) # 상단은 0번