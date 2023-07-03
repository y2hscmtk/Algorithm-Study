# https://www.acmicpc.net/problem/19237
'''
NxN 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 
맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 
그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 
냄새는 상어가 k번 이동하고 나면 사라진다.

[상어 이동 알고리즘]
각 상어가 이동 방향을 결정할 때
1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 
2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 
3. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 
우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 
상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

이 과정을 반복할 때, 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성하시오.
'''
n,m,k = map(int,input().split())
# n x n 크기의 맵 => 상어의 현재 위치 기록
# m은 상어의 개수
# k는 냄새가 사라지는데 걸리는 시간

# 현재 격자의 상태 입력받기
# 0은 빈 공간을 의미, 숫자는 각 상어의 번호를 의미
box = [list(map(int,input().split())) for _ in range(n)]

# 각 상어들의 현재 방향정보
sharck_direction = list(map(int,input().split()))

# 각 상어들의 우선순위 입력받기 
# 3차원 배열 필요(각 상어별, 방향별, 우선순위)
# 상 하 좌 우 (1,2,3,4)
priority = [[list(map(int,input().split())) for _ in range(4)] for _ in range(m)]

# 현재 냄새와 냄새가 사라지는데 남은 시간 정보
# 3차원 배열 필요
# 첫번째 인자는 냄새를 남긴 상어의 번호, 두번째 인자는 냄새가 사라지기까지 남은 시간 => 이동후 업데이트 필요
smell = [[[0,0] for _ in range(n)] for _ in range(n)]


# 방향벡터 설정
# 상,하,좌,우를 기준으로 접근할수 있도록
# dx[direction-1],dy[direction-1] // direction = 1일때, (-1,0)씩 각 좌표에 더해져 위쪽으로 이동됨 
dx = [-1,1,0,0]
dy = [0,0,-1,1]


# 1번상어만 남아있는지 확인
def isAlone():
    for i in range(n):
        for j in range(n):
            # 0과 1이외의 숫자가 발견된다 => 다른 상어가 존재한다
            if box[i][j] != 0 and box[i][j] != 1:
                return False
    return True # 문제없이 통과했다 => 1번 상어만 남아있다.

                
# 다음에 이동할 위치를 결정하는 함수
# 탐색중인 상어의 번호, 상어의 위치좌표
def define_next_position(shark_num,x,y):
    global sharck_direction
    # 현재 상어의 이동 방향
    d = sharck_direction[shark_num-1]-1
    # 조건을 만족하는 값이 여러개가 있다면 
    # 방향별 우선순위를 기준으로 다음 방향을 결정한다.
    # 1. 상하좌우 중 아무 냄새가 없는 칸을 방향으로 잡는다.
    # 조건을 만족하는 값들을 배열에 넣고,배열의 값이 하나라면 해당 값을 반환한다.
    # 그렇지 않다면 우선순위별 이동방향을 결정한다.
    next_direction = 0
    array = []
    found = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 배열을 벗어나지 않는지 확인
        if 0<=nx<n and 0<=ny<n:
            # 아무 냄새도 없는 칸인지 확인
            if smell[nx][ny][0] == 0:
                array.append([nx,ny])
                next_direction = (i+1)
                found = True
    # 좌표를 반환하지 못했다 => 상하좌우 다 냄새가 있다.
    #아무 냄새도 없는 칸을 찾지 못했다면 자신의 냄새가 있는 칸 찾기
    if not found:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 배열을 벗어나지 않는지 확인
            if 0<=nx<n and 0<=ny<n:
                # 자신의 냄새가 있는 칸인지 확인
                if smell[nx][ny][0] == shark_num:
                    array.append([nx,ny])
    # 값을 결정했다면 이동하는 방향이 상어의 이동 방향이됨
    # 해당 상어의 이동방향 설정 필요
    # 조건을 만족하는 값이 여러개라면 방향별 우선순위로 반환
    # 우선순위 높은 값 검사
    # 우선순위 배열로부터 좌표 생성
    # num-1번의 상어의 현재 방향에서의 우선순위
    curr_p = priority[shark_num-1][d]
    for i in range(len(curr_p)):
        p_dir = curr_p[i]-1
        nx = x + dx[p_dir]
        ny = y + dy[p_dir]
        
        # array에서
        # 일치하는 좌표가 있는지 확인
        # 가장 먼저 발견되는 좌표로 이동 => 우선순위가 제일 높은 좌표임
        for j in range(len(array)):
            if array[j][0] == nx and array[j][1] == ny:
                # 해당 상어의 이동방향 변경후 값 반환
                sharck_direction[shark_num-1] = p_dir+1
                return nx,ny

# 상어의 위치를 결정하는 함수
# 같은 위치에 여러마리 상어가 있는지 검사하고, 생존할 상어를 결정
def define_final_positon():
    global box,shark_position
    
    # 각 상어별로 같은 위치에 존재하는 상어가 있는지 확인
    for i in range(m):
        x,y = shark_position[i]
        if x==-1: # 쫓겨난 성어는 무시
            continue
        array = [i] # 상어번호 삽입(x,y좌표에 존재하는 상어)
        overlap = False # 겹치지 않았다는 의미
        for j in range(m):
            if i==j:
                continue # 같은 상어에 대해서는 무시
            # 이미 쫓겨난 상어도 무시
            if shark_position[j][0] == -1:
                continue
            # 만약 같은 위치에 상어가 존재한다면
            # 두마리 뿐 아니라, 여러마리 존재 가능함
            if shark_position[j][0] == x and shark_position[j][1] == y:
                array.append(j)
                overlap = True # 겹쳤다는 의미
        # 만약 겹치지 않았다면 해당 좌표로 상어 이동
        if overlap == False:
            box[x][y] = (i+1)
        else: # 겹쳤다면
            # 가장 숫자가 작은 상어만 남기고 나머지 상어 내쫓기
            save = min(array)
            x,y = shark_position[save]
            box[x][y] = (save+1)
            for shark in array:
                if shark!=save:
                    shark_position[shark] = [-1,-1]



# 현재 자신의 위치에 냄새를 뿌리는 함수
def spread_smell():
    global smell
    for i in range(m):
        x,y = shark_position[i]
        # 해당 번호의 상어가 아직 격자안에 존재한다면
        # 냄새를 뿌린다.
        if x!=-1 and y!=-1:
            smell[x][y] = [i+1,k]
    # for i in range(n):
    #     for j in range(n):
    #         shark = box[i][j]
    #         if shark != 0:
    #             smell[i][j] = shark,k


# 냄새정보 업데이트
def update():
    global smell
    for i in range(n):
        for j in range(n):
            # 0보다 큰 경우에 한해서 업데이트(k값은 0보다 작아질수없음)
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                # 카운트가 0이 되었다면, 해당 좌표의 냄새를 지운다
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0



# 각 상어별 현재 위치
# 각 상어의 다음 이동 위치가 결정되면 이 배열을 비교하여, box의 값을 초기화한다.
shark_position = [[] for _ in range(m)] # 상어 수만큼 배열을 만들어 2차원 배열로 관리
for i in range(n):
    for j in range(n):
        shark = box[i][j]
        if shark != 0:
            shark_position[shark-1] = [i,j]
# 1번 상어의 위치 x,y = shark_position[0] 로 접근

time = 0 # 걸린 총 시간 => 정답
# 1번 상어만 격자에 남을때까지 반복
while True:
    # 1번 상어만 남았다면 반복문 종료
    if isAlone():
        print(time)
        break
    # 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다
    if time>=1000:
        print(-1)
        break
    
    
    # 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
    spread_smell()
    
    # 각 상어별로 이동할 위치 설정
    # 배열을 돌면서 상어 위치 발견시 => define_next_positon()호출
    for i in range(n):
        for j in range(n):
            shark = box[i][j]
            if shark != 0:
                # 해당 상어의 다음 이동 위치 결정
                nx,ny = define_next_position(shark,i,j)
                shark_position[shark-1] = [nx,ny]
                # 다음 이동 위치가 결정되면, 일단 현재 값을 0으로 변경
                box[i][j] = 0 # 상어 이동
                
    # 모든 상어의 다음 이동 위치가 결정되면
    # 같은 위치에 상어가 있는지 검사하고, 상어별 서열에 따라 상어 제거
    define_final_positon()
    
    # 상어가 이동한 뒤에, 냄새정보 업데이트
    update()
    time+=1