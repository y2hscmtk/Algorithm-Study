# https://www.acmicpc.net/problem/17143
'''
[낚시왕]
칸에는 상어가 최대 한 마리 들어있을 수 있다. 상어는 크기와 속도를 가지고 있다.

낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다. 다음은 1초 동안 일어나는 일이며, 
아래 적힌 순서대로 일어난다. 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

1. 낚시왕이 오른쪽으로 한 칸 이동한다. // 낚시왕의 열 위치를 변수로 표시
2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다. // 포인트 누적
3. 상어가 이동한다. // 상어 이동 알고리즘 수행

상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 
이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다. // 크기 순으로 정렬하고, 가장 큰 상어만 남기고 죽인다.

낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구해보자
r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다. 
(r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다.
1,2,3,4 => 상하우좌
'''
import sys
input = sys.stdin.readline
R,C,M = map(int,input().split())
graph = [[[0,0,0] for _ in range(C)] for _ in range(R)]
# 1,2,3,4 상하우좌
dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]
fisherman = 0 # 시작 위치 => 끝에 도달하면 종료
result = 0 # 낚시왕이 잡은 물고기 크기의 합

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    graph[r-1][c-1] = [s,d,z] # 속력, 방향, 크기

# 방향 바꾸기
def change_direction(r,c):
    global graph
    if graph[r][c][1] == 1:
        graph[r][c][1] = 2
    elif graph[r][c][1] == 2:
        graph[r][c][1] = 1
    elif graph[r][c][1] == 3:
        graph[r][c][1] = 4
    elif graph[r][c][1] == 4:
        graph[r][c][1] = 3
        
# 이동거리 최적화
def optimization_distance(speed, direction):
    if direction in [1, 2]: # 상하 이동
        cycle = 2 * (R - 1)
    else: # 좌우 이동
        cycle = 2 * (C - 1)
    return speed % cycle

# 낚시왕의 열에 있는 상어 중에 땅과 제일 가까운 상어를 잡는다.
def fishing():
    global result
    for r in range(R):
        # 속력 방향 크기
        if graph[r][fisherman][1] != 0: # 물고기라면 방향이 존재함
            result += graph[r][fisherman][2]
            graph[r][fisherman] = [0,0,0] # 물고기를 잡았으므로 모든 정보 제거
            break

# 상어가 이동한다.
def shark_move():
    global graph
    dict = {}
    # 상어가 이동하려는 칸이 격자판의 경게를 넘는 경우 방향을 바꿔서 속력을 유지한채로 이동한다.
    for i in range(R):
        for j in range(C):
            # 속력,방향,크기
            if graph[i][j][1] == 0: # 물고기가 존재한다면 방향 정보를 갖고 있을테니까
                continue # 빈 공간은 생략
            speed,direction,_ = graph[i][j] # 속력,방향,크기
            remain_distance = optimization_distance(speed,direction)
            x,y = i,j
            # 남은 거리가 0이 될때까지 이동
            for _ in range(remain_distance):
                nx = x + dx[graph[i][j][1]]
                ny = y + dy[graph[i][j][1]]
                # 경계에 닿지 않고 이동가능하다면
                if 0<=nx<R and 0<=ny<C:
                    x = nx; y = ny
                else: # 경계에 도달하였다면
                    change_direction(i,j) # 방향 바꾸기
                    nx = x + dx[graph[i][j][1]]
                    ny = y + dy[graph[i][j][1]]
                    x = nx; y = ny
            
            # 바로 이동시키지 않고, 이동 결과의 목적지를 '키'로 설정하여 dict에 저장
            key = f'{x},{y}'
            if key not in dict:
                dict[key] = [graph[i][j]]
            else:
                dict[key].append(graph[i][j])
            # 현재 위치에서 이동 처리 된것이므로, 현재 위치에 대한 정보는 우선 초기화 [0,0,0]
            graph[i][j] = [0,0,0]
    
    # 이동 결과 한 칸에 여러마리의 상어가 있다면 큰 상어만 남기고 작은 상어는 없앤다.(큰 상어가 잡아먹음)
    # dict의 모든 키를 돌면서, 키에 포함된 배열을 상어의 크기를 기준으로 내림차순 정렬후 큰 상어만 배열에 정보 삽입
    for key in dict:
        dict[key].sort(key=lambda x:-x[2]) # 속력,방향,크기 -> 크기 순으로 내림차순 정렬
        x,y = map(int,key.split(','))
        # 가장 큰 상어 정보를 삽입(0번째 상어가 제일 큰 상어)
        graph[x][y] = dict[key][0] # 속력,방향,크기

while fisherman != C:
    # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    fishing()
    # 3. 상어가 이동한다.
    shark_move()
    # 1. 낚시왕이 오른쪽으로 한 칸 이동한다. 
    fisherman += 1

print(result)