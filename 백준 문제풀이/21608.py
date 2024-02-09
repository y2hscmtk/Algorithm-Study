'''
(r, c)는 r행 c열을 의미한다. 교실의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다.
|r1 - r2| + |c1 - c2| = 1(상하좌우)을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.
학생은 N^2명이 존재

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

#0. 모든 칸을 순위하며 해당 학생이 앉을 자리 찾기
#1. 인접한 칸 중 해당 학생이 좋아하는 학생의 수와, 빈 칸의 수를 배열에 각각 기록
#1.1. 배열에 기록할 값 => (좋아하는 학생의 수, 빈 칸의 수, 행의 번호, 열의 번호)
#2. 배열을 조건1~3에 맞춰 정렬한 후, 조건을 만족하는 자리에 배치
#3. 모든 학생들을 배치한 후, 배열을 돌면서 전체 만족도 계산
'''
N = int(input())
seat = [[0]*N for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# n번째 학생이 앉을 자리 계산
def select_seat():
    global seat
    # 각 좌석에 대한 정보를 기록하기 위한 배열 생성
    seat_info = []
    for x in range(N):
        for y in range(N):
            if seat[x][y] != 0:
                continue
            like_count,empty_count = 0,0 # 좋아하는 학생수, 빈좌석수
            # 앉을 수 있는 자리에 대해서 상하좌우 검사
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if seat[nx][ny] in like: # 좋아하는 학생이라면
                        like_count+=1
                    elif seat[nx][ny] == 0: # 빈 좌석이라면
                        empty_count+=1
            # 현재 좌석에 대한 정보 배열에 기록
            seat_info.append([like_count,empty_count,x,y])
    
    # 최적의 자리 계산하여 배치
    # 1. 좋아하는 사람이 가장 많은 자리로
    # 2. 그 중에서 주변에 빈칸이 많은 자리로
    # 3. 그 중에서 행의 번호가 가장 작고, 그 다음으로 열의 번호가 가장 작은 순으로
    # 내림차순,내림차순,오름차순,오름차순
    seat_info.sort(key = lambda x: (-x[0],-x[1],x[2],x[3])) 
    
    # 정렬 이후 가장 왼쪽에 위치한 값의 x,y좌표
    x = seat_info[0][2]
    y = seat_info[0][3]
    
    # 그 좌표에 사람 배치
    seat[x][y] = n


# 전체 만족도 계산
def calc_satisfication():
    result = 0 # 만족도 총합
    for x in range(N):
        for y in range(N):
            p = seat[x][y] # 그 칸에 있는 사람의 번호
            like = people[p] # 그 사람이 좋아하는 사람들
            like_count = 0 # 좋아하는 사람의 수
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if seat[nx][ny] in like:
                        like_count += 1
            if like_count == 1:
                result += 1
            elif like_count == 2:
                result += 10
            elif like_count == 3:
                result += 100
            elif like_count == 4:
                result += 1000
    return result

people = [[] for _ in range(N*N+1)] # N번 사람이 각각 누구를 좋아하는지 기록 => 호감도 계산에 사용
for _ in range(N*N):
    data = list(map(int,input().split()))
    n,like = data[0],data[1:]
    people[n] = like
    select_seat()

print(calc_satisfication())




