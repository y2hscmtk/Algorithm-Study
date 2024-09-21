# https://www.acmicpc.net/problem/16197
'''
13시 21분 시작
N x M 크기의 보드와 4개의 버튼으로 이루어진 게임
각각의 칸은 비어있거나 벽으로 구성되어있음
두개의 빈 칸에는 동전이 하나씩 놓여 있고 두 동전의 위치는 다르다.
버튼은 상하좌우 4가지가 있음
버튼을 누르면 두 동전이 버튼에 쓰여있는 방향으로 동시에 이동함 => 큐에 두 동전의 위치를 동시에 넣어주면 될듯
동전이 이동하려는 칸이 벽이라면 동전은 이동하지 않는다.
(*동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.)
그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다. 이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
(*두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야 하는지) 구하는 프로그램 작성
o 동전 . 빈칸 # 벽
동전의 개수는 항상 2개이다.

* 첫째 줄에 두 동전 중 하나만 보드에서 떨어뜨리기 위해 눌러야 하는 버튼의 최소 횟수를 출력한다. 
* 만약, 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면, -1을 출력한다.
예상 알고리즘 : 브루트포스, 백트래킹
13시 25분 문제 풀이 시작
14시 10분 시간초과
'''
import sys
N,M = map(int,input().split()) # 세로의 크기 N, 가로의 크기 M (1<=N,M<=20)
dx = [-1,0,1,0]; dy = [0,1,0,-1] # 방향벡터
result = sys.maxsize # 정답(최소 이동 횟수)
find = False
board = []
coin_position = []
# 보드판 정보 입력받기
for i in range(N):
    data = list(input())
    for j in range(M):
        if data[j] == 'o': # 동전 위치 발견시
            coin_position.append([i,j]) # 동전 위치 저장
    board.append(data)

def dfs(depth,count):
    global result,coin_position,board
    if depth > 10:
        return 
    if count == 1: # 동전이 하나만 떨어진 경우
        result = min(result,depth)
        return

    # 버튼을 누르면 두 동전이 버튼에 쓰여있는 방향으로 동시에 이동함
    # => 방향을 먼저 고른 다음 동전을 이동시켜야 됨
    for i in range(4): # 네가지 방향 버튼 중에서 한 방향 선택
        
        drop_count = 0 # 떨어진 동전의 수
        # 현재 코인 위치 저장
        copy_coin_position = [c[:] for c in coin_position]
        # 각각의 동전에 대해서
        for j in range(2): 
            x,y = coin_position[j]
            nx = x + dx[i]; ny = y + dy[i]
            # 동전이 떨어지지 않는다면 이동
            if 0<=nx<N and 0<=ny<M:
                # 이동한 곳에 벽이 있다면 이동 불가능
                if board[nx][ny] == '#':
                    continue
                
                # 동전 이동
                board[x][y] = '.' # 이전에 있었던 위치는 빈칸으로 바꾸고
                board[nx][ny] = '0' # 동전으로 바꾸기
                coin_position[j] = [nx,ny] # 코인 위치 변경
                        
            else: # 동전이 떨어졌다면
                drop_count += 1
        dfs(depth+1,drop_count)
        # 동전 위치 되돌리기
        for p in range(2):
            # 이전에 코인이 있었던 위치
            lcx,lcy = copy_coin_position[p]
            # 현재 코인이 놓여져 있는 위치
            ccx,ccy = coin_position[p]
            # 동전 되돌리기
            board[lcx][lcy] = '0'
            board[ccx][ccy] = '.'
        coin_position = [c[:] for c in copy_coin_position]

dfs(0,0)

print(-1) if result == sys.maxsize else print(result)
