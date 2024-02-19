# https://www.acmicpc.net/problem/19236
'''
1. 상어 이동한 뒤 물고기를 먹는다. 
    1.1. 상어의 현재 방향에서 이동가능한 칸을 찾는다.
    1.2. 이동가능한 칸이 여러개라면 백트래킹하여 시뮬레이션 수행
    1.3. 이동가능한 칸이 없다면 해당 시점에서의 시뮬레이션 종료 => 현재까지 먹은 물고기 번호 합 최대합으로 갱신
2. 물고기가 이동한다. 다시 1번으로 이동한다.

상어가 먹을 수 있는 물고기들의 번호의 최대 합 구하기
상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다.

방향은 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다
'''
# 1번째 인덱스부터 문제에서 주어진 방향대로
# %8을 통해 8번 인덱스를 넘어서는 경우 다시 1이 될 수 있도록
dx = [0,-1,-1,0,+1,+1,+1,0,-1]
dy = [0,0,-1,-1,-1,0,+1,+1,1]
graph = []
direction = [] # 물고기의 현재 방향을 표시

# 상태정보 매핑
for _ in range(4):
    a1,d1,a2,d2,a3,d3,a4,d4 = map(int,input().split())
    graph.append([a1,a2,a3,a4])
    direction.append([d1,d2,d3,d4])

result = graph[0][0] # 0,0 위치의 물고기는 무조건 먹고 시작함
graph[0][0] = -1 # 상어는 -1로 표시
shark_direction = direction[0][0] # 0,0 위치의 물고기의 방향 정보를 갖고 시작
shark_x,shark_y = 0,0 # 상어의 위치

# 물고기 이동
def fish_move(c_graph,c_direction):
    # 물고기는 낮은 번호부터 이동하기 시작함
    for t in range(1,17): # 16마리로 고정되어있음
        x,y = -1,-1
        for i in range(4):
            for j in range(4):
                if c_graph[i][j] == t:
                    x,y = i,j
                    break
            if (x,y) != (-1,-1): # 찾았다면
                break
        if (x,y) == (-1,-1): # 못찾았다면 -> 사망
            continue # 다음 물고기부터 진행
        # 해당 물고기가 살아있다면 물고기 위치 찾기
        # 해당 번호의 물고기의 방향
        x,y = i,j
        d = c_direction[x][y]
        # 이동할 수 있는 방향인지 확인하고 이동할 수 없다면 방향 업데이트 필요함
        # 현재 방향에서부터 한바퀴 돌면서 이동가능한 방향인지 확인하는 과정
        find_d = False # 올바른 방향을 찾았는지 -> 현재 물고기가 이동할 수 있는지
        for i in range(8):
            if i!=0:
                d+=1
                if d>8:
                    d%=8
            nx = x + dx[d]
            ny = y + dy[d]
            # 이동 가능하면 break
            # 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸
            if 0<=nx<4 and 0<=ny<4:
                if c_graph[nx][ny] != -1: # 상어가 없는 칸이어야함
                    # 상어가 없는 칸을 발견했다면 해당 방향이 올바른 방향임
                    find_d = True    
                    break
        # 만약 이동할 수 있는 칸이 없으면 이동하지 않는다.
        if find_d: # 찾은 경우에만 이동
            c_graph[x][y],c_graph[nx][ny] = c_graph[nx][ny],c_graph[x][y] # 위치 변경
            c_direction[x][y] = c_direction[nx][ny]
            c_direction[nx][ny] = d  # 방향 정보 변경(바뀐 방향 정보로 바꿔줘야함)

# 상어의 움직임
def shark_move(c_graph,c_direction,shark_direction,eat_count):
    global shark_x,shark_y
    # 먼저 이동할 좌표를 고른다.
    # 이동 가능한 좌표가 없다면 해당 시뮬레이션 종료
    for i in range(1,4): # *1,*2,*3(최대)
        nx = shark_x + dx[shark_direction]*i
        ny = shark_y + dy[shark_direction]*i
        if 0<=nx<4 and 0<=ny<4:
            # 상어는 물고기가 있는 칸으로만 이동 가능
            if c_graph[nx][ny] > 0: # 0은 죽어서 없는 빈칸, 그 이상은 물고기
                # 배열 복사
                save_graph = [c[:] for c in c_graph] 
                save_direction = [c[:]for c in c_direction]
                s_x,s_y = shark_x,shark_y
                c_d = shark_direction
                # 물고기 섭취
                eat_count += c_graph[nx][ny]
                # 좌표에서 물고기 제거처리(graph)
                c_graph[shark_x][shark_y],c_graph[nx][ny] = c_graph[nx][ny],c_graph[shark_x][shark_y]
                c_graph[shark_x][shark_y] = 0 # 상어 이동완료
                shark_direction = c_direction[nx][ny]
                shark_x,shark_y = nx,ny # 상어의 다음 위치
                # 먹었으니까 다음 수행으로
                move(c_graph,c_direction,shark_direction,eat_count)
                # 백트래킹 - 원상복구
                c_graph = save_graph 
                c_direction = save_direction
                eat_count -= c_graph[nx][ny]
                shark_x,shark_y = s_x,s_y
                shark_direction = c_d
    return False # 상어가 이동할 곳이 없으면 멈춘다.


def move(c_graph,c_direction,shark_direction,eat_count):
    global result
    while True:
        # 물고기가 이동한다.
        fish_move(c_graph,c_direction)
        # 상어가 이동한다.
        # 상어가 이동할 수 없으면 break
        if not shark_move(c_graph,c_direction,shark_direction,eat_count):
            result = max(result,eat_count) # 최대값 갱신 후 탈출
            break

# 초기에는 원본을 넘김 -> 이후 상어의 움직임이 백트래킹에 따라 결정됨에 따라 배열을 복사해서 move 호출
move(graph,direction,shark_direction,result) # 마지막 인자는 현 시점에서의 최대값
print(result)

