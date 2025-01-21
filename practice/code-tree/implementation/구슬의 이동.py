'''
방향을 바꾸는데는 시간 소요가 없다.
동일한 위치에 존재하는 구슬이 k개 이하라면 문제없이 다음 과정을 진행한다.
k개가 넘는 구슬이 존재한다면 우선순위가 높은 구슬 k개만 살아남고 나머지는 사라진다.
구슬의 속도가 빠를 수록 우선순위가 높으며, 구슬의 속도가 일치할 경우, 구슬의 번호가 더 큰 구슬이 우선순위가 높다.
'''
# 격자크기, 구슬 개수, 시간, 최대 구슬 수
n, m, t, k = map(int, input().split())

board = [[[] for _ in range(n)] for _ in range(n)]

# U,L,D,R 
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 이동방향 매핑
mapper = {'U':0, 'L':1, 'D':2, 'R':3}

balls = [[]]
alive = [True]*(m+1) # 해당 구슬이 현재 살아있는지 여부
# 각 구슬에 대한 정보
for i in range(1,m+1):
    # (r,c)에서 d방향으로 속도 v로 이동중
    r,c,d,v = input().split()
    balls.append([int(r)-1,int(c)-1,mapper[d],int(v)])

# 벽에 부딪히는지 검사
def in_range(x,y):
    return 0<=x<n and 0<=y<n

# num번째 구슬 이동
def move(num):
    # 방향을 바꾸는데는 시간이 소요되지 않는다.
    # 벽에 부딪히는지 여부를 확인하여 방향을 바꿀것인지 결정 필요
    x,y,d,v = balls[num]
    
    # v칸만큼 d방향으로 이동
    # 이동하는 과정에서 영역을 벗어나면 방향을 바꾼뒤 이동
    for _ in range(v):
        nx,ny = x + dx[d], y + dy[d]
        if not in_range(nx,ny): # 영역을 벗어나는 경우
            d = (d+2)%4 # 반대방향으로 변경
            nx,ny = x + dx[d], y + dy[d]
        x,y = nx,ny # 다음 위치로 이동
                
    balls[num] = [x,y,d,v]
    return (x,y)

# k개 이상이 존재하는 구슬 제거 
def remove_balls(i,j):
    numbers = board[i][j] # 해당 좌표에 존재하는 구슬의 번호들
    temp = []
    for num in numbers:
        r,c,d,v = balls[num] # 해당 공의 정보들
        temp.append((v,num)) # 속도가 더 클수록, 번호가 더 클수록 우선순위가 높다.
    
    temp.sort()
    size = len(numbers)
    for i in range(size-k):
        v,b_n = temp[i]
        alive[b_n] = False # 공 삭제 처리
         

# 시뮬레이션
def simulation():
    global board
    # 보드판 초기화
    board = [[[] for _ in range(n)] for _ in range(n)]

    # 공 이동
    # 살아있는 구슬에 한해 이동
    for num in range(1,m+1):
        if alive[num]:
            nx,ny = move(num) # 구슬이 이동하고 난 위치
            board[nx][ny].append(num)
    
    # 모든 구슬의 이동이 끝난 이후 k개 초과로 구슬이 존재하는 칸 발견시 처리
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > k:
                remove_balls(i,j) # 구슬 제거 작업 수행
    

# t초 동안 시뮬레이션 진행
for _ in range(t):
    simulation()

# 남아있는 구슬의 수를 출력
ans = 0
for i in range(1,len(alive)):
    if alive[i]:
        ans += 1

print(ans)

    
