# https://www.acmicpc.net/problem/20057
'''
토네이도는 이동하면서 모래를 이동시킨다. 
모래는 격자의 밖으로 이동할 수도 있다.
토네이도가 소멸되었을 때, 격자 밖으로 나간 모래의 양을 구하라
'''
N = int(input())
send = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [0,1,0,-1] # 방향 벡터
dy = [-1,0,1,0]
d = 0 # 토네이도의 현재 이동방향을 의미
result = 0
# 2. 토네이도는 이동하면서 모래를 이동시킨다.
def move_send(x,y): # (x,y)는 Y의 좌표, Y좌표의 모든 모래가 이동한다.
    # 현재 이동 방향을 기준으로 모래 이동시키기
    # 그 과정에서 격자 밖으로 나가는 모래 파악
    global send, result
    amount = send[x][y]
    # 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다.
    # 7퍼센트 비율의 좌표(d-1방향, d+1방향으로 1칸씩)
    # 위 7퍼센트
    nx = x + dx[(d+3)%4]; ny = y + dy[(d+3)%4]
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += int(amount * 0.07)
    else: # 영역을 벗어난다면
        result += int(amount * 0.07)
        
    # 위 2퍼센트
    nx = x + 2*dx[(d+3)%4]; ny = y + 2*dy[(d+3)%4]
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += int(amount * 0.02)
    else: # 영역을 벗어난다면
        result += int(amount * 0.02)

    # 아래 7퍼센트
    nx = x + dx[(d+1)%4]; ny = y + dy[(d+1)%4]
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += int(amount * 0.07)
    else: # 영역을 벗어난다면
        result += int(amount * 0.07)
    
    # 아래 2퍼센트
    nx = x + 2*dx[(d+1)%4]; ny = y + 2*dy[(d+1)%4]
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += int(amount * 0.02)
    else: # 영역을 벗어난다면
        result += int(amount * 0.02)
    
    # 5퍼센트 비율의 좌표(d방향으로 2칸)
    nx = x + 2*dx[d]; ny = y + 2*dy[d]
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += int(amount * 0.05) # 소수점 이하는 무시
    else: # 영역을 벗어난다면
        result += int(amount * 0.05) # 소수점 이하는 무시
    
    # 10퍼센트 비율의 좌표(d방향으로 이동후, 위아래로 한칸)
    # 아래 10퍼센트
    nx = x + dx[d]; ny = y + dy[d]
    nx = nx + dx[(d+1)%4]; ny = ny + dy[(d+1)%4]; 
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += int(amount * 0.1) # 소수점 이하는 무시
    else: # 영역을 벗어난다면
        result += int(amount * 0.1) # 소수점 이하는 무시
    # 위 10퍼센트
    nx = x + dx[d]; ny = y + dy[d]
    nx = nx + dx[(d+3)%4]; ny = ny + dy[(d+3)%4]; 
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += int(amount * 0.1) # 소수점 이하는 무시
    else: # 영역을 벗어난다면
        result += int(amount * 0.1) # 소수점 이하는 무시
    
    # 1퍼센트 비율의 좌표(d+2방향으로 이동후, 위아래로 한칸)
    # 위 1퍼센트
    nx = x + dx[(d+2)%4]; ny = y + dy[(d+2)%4]
    nx = nx + dx[(d+3)%4]; ny = ny + dy[(d+3)%4]
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += int(amount * 0.01) # 소수점 이하는 무시
    else: # 영역을 벗어난다면
        result += int(amount * 0.01) # 소수점 이하는 무시
    
    # 아래 1퍼센트
    nx = x + dx[(d+2)%4]; ny = y + dy[(d+2)%4]
    nx = nx + dx[(d+1)%4]; ny = ny + dy[(d+1)%4]
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += int(amount * 0.01) # 소수점 이하는 무시
    else: # 영역을 벗어난다면
        result += int(amount * 0.01) # 소수점 이하는 무시
    
    # a 좌표(d 방향으로 한 칸 이동)
    nx = x + dx[d]; ny = y + dy[d]
    a = amount - 2*int(amount*0.02) - 2*int(amount*0.07) - 2*int(amount*0.1) - 2*int(amount*0.01) - int(amount*0.05)
    if 0<=nx<N and 0<=ny<N:
        send[nx][ny] += a
    else:
        result += a
    send[x][y] = 0 # 현재 칸의 모래가 이동한것이므로 현재 칸 모래 지우기

# 1. 토네이도가 이동한다. 처음에 이동하는 장소는 배열의 중간
x,y = N//2,N//2
# <토네이도 이동 알고리즘>
# 1 1 2 2 3 3 ... 2번 이동할때마다 이동하는 칸이 한 칸씩 늘어난다.
move = 1 # 초기에는 한 칸만 이동 가능
count = 0 # 이동 가능한 칸 늘리기 용도
while True:
    # 토네이도는 (1,1)까지 이동한 뒤 소멸한다.
    if (x,y) == (0,0):
        break
    if count == 2: # 두 번 이동 완료시 칸 층가
        move += 1
        count = 0 # 초기화
    # 한번 설정한 방향으로 이동 가능한 칸 만큼 먼저 이동
    for m in range(1,move+1):
        nx = x + dx[d]
        ny = y + dy[d]
        move_send(nx,ny) # 모래 이동 수행
        x,y = nx,ny # 모래 이동 
        if (x,y) == (0,0): # 토네이도는 (1,1)까지 이동한 뒤 소멸한다.
            break
    # 이동 가능한 만큼 이동이 끝나면 방향 꺾기
    d = (d+1)%4 # 상하좌우 이동 반복, 한번 이동하면 방향을 꺾는다
    count += 1

print(result)