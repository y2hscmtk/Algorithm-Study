# https://www.acmicpc.net/problem/17837
'''
말이 이동할때 올려져 있는 말도 함께 이동
0은 흰색, 1은 빨간색, 2는 파란색이다.
'''
WHITE,RED,BLUE = 0,1,2
cnt = 0 # 턴 번호

n, k = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

number_pos = [[[] for _ in range(n)] for _ in range(n)]

#  →, ←, ↑, ↓
dx = [0,0,-1,1]; dy = [1,-1,0,0]

# 말의 초기 위치 입력
for i in range(1,k+1):
    x,y,d = map(int,input().split())
    number_pos[x-1][y-1].append([i,d-1]) # 말 번호, 이동 방향

def reverse_dir(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

# 해당 칸에 말이 4개 이상 존재하는지 확인
def check(x,y):
    if len(number_pos[x][y]) >= 4:
        return True
    return False

# 영역 검사
def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 1. 이동할 말의 현재 좌표 찾기
def find_pos(num):
    for i in range(n):
        for j in range(n):
            for idx,number in enumerate(number_pos[i][j]):
                if number[0] == num:
                    return (i,j,idx)

# x,y 좌표에 있는 말(num) 이동
def move(x,y,idx):
    num,d = number_pos[x][y][idx]
    nx,ny = x + dx[d], y + dy[d] # 다음에 이동할 위치
    # 이동하려는 칸이
    # 3. 파란색이거나 영역을 벗어나는 경우 - 현재 말의 이동방향을 반대로 설정하고, 그 방향으로 한 칸 이동
    if not in_range(nx,ny) or grid[nx][ny] == BLUE:
        d = reverse_dir(d)
        number_pos[x][y][idx] = [num,d]
        nx,ny = x + dx[d], y + dy[d] # 반대 방향 위치 갱신
    # 이후 이동하려는 칸이 파란색이거나 영역을 벗어나는 경우, 이동하지 않고 가만히 있는다.
    if not in_range(nx,ny) or grid[nx][ny] == BLUE:
        return (x,y)
    # 이동하려는 칸이 흰색, 빨간색인 경우 아래 조건에 따라 이동한다.
    # 1. 흰색인 경우 그 칸으로 이동 - 해당 칸에 말이 이미 존재하는 경우, 가장 위에 말을 위치 시킨다.
     # 현재 말의 인덱스에서부터 가장 마지막 말 까지 순차적으로 이동
    if grid[nx][ny] == WHITE:
        # 현재 칸에서 해당 말과 그 위의 말 제거
        for i in range(idx,len(number_pos[x][y])):
            num, d = number_pos[x][y][i]
            number_pos[nx][ny].append([num,d])
        for i in range(idx,len(number_pos[x][y])):
            number_pos[x][y].pop()
    # 2. 빨간색인 경우 그 칸으로 이동 - 거꾸로 말을 쌓는다.
    elif grid[nx][ny] == RED:
        for i in range(idx,len(number_pos[x][y])):
            num,d = number_pos[x][y].pop()
            number_pos[nx][ny].append([num,d])
    return (nx,ny)

while True:
    # 한 턴은 1번말부터 k번째 말까지 이동
    cnt += 1
    isContinue = True # 진행 가능 여부 확인
    for num in range(1,k+1):
        x,y,idx = find_pos(num) 
        nx,ny = move(x,y,idx) # 해당 말 이동 - 이동 결과 반환
        # 해당 칸에 말이 4개 위치하게 되었는지 확인
        if check(nx,ny):
            isContinue = False # 진행 불가
            break
    if cnt > 1000: # 1000보다 큰 경우 종료
        print(-1)
        break
    if not isContinue: # 말이 4개 이상 위치하게 되는 경우 종료
        print(cnt)
        break