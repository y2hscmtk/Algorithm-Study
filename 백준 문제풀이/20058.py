# https://www.acmicpc.net/problem/20058
'''
단계 L에 맞춰서 2^L * 2^L 크기의 부분 격자로 나눈뒤, 격자를 90도 회전시킨다.
이후 얼음이 있는 칸 3개 또는 그 이상과 인접해 있지 않은 칸(주변에 얼음이 1,2인 칸)은 얼음의 양이 1 줄어든다.

파이어스톰은 총 Q번 시전된다.
1. 남아있는 얼음 A[r][c]의 합 구하기
2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 구하기 -> 가장 큰 섬

** 얼음을 감소시킬 때 0이하로 떨어지지 않도록 처리 -> 남아있는 얼음의 합을 위해

시작 : 2024/10/08/18:12 
종료 :
'''
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]; dy = [-1,1,0,0]
N, Q = map(int,input().split())
R = 2**N # 보드판의 영역
A = [list(map(int,input().split())) for _ in  range(R)]
# 마법사 상어가 시전한 단계 L1,L2, .. LQ
L = list(map(int,input().split()))

# 1. 남아있는 얼음 A[r][c]의 합 구하기
def calc_sum_ice():
    ice_size = 0
    for row in A:
        ice_size += sum(row)
    return ice_size

# 2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 구하기
def find_max_ice(i,j): # bfs
    global max_ice_size,visited
    
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True # 탐색 시작 위치 방문 처리
    size = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            # 영역을 벗어나지 않으면서 현재 얼음덩어리의 집합의 일부이며 처음 방문한 얼음
            if 0<=nx<R and 0<=ny<R and A[nx][ny] > 0: # 얼음인지 확인
                if not visited[nx][ny]:
                    visited[nx][ny] = True # 방문 처리
                    queue.append((nx,ny))
                    size+=1
    max_ice_size = max(max_ice_size,size) # 현재 얼음 덩어리가 더 크다면 정답 갱신

# 배열 회전시키키
def turn_array(x,y,l):
    global A
    temp_A = [a[:] for a in A]
    X,Y = x,y
    for nx,ny in [(X,Y+l),(X+l,Y+l),(X+l,Y),(X,Y)]:
        # 1. 현재 칸을 포함하여 가로세로 l칸을 선택하여 배열형태로 복사
        copy_array = [[0 for _ in range(l)] for _ in range(l)]
        for i in range(x,x+l):
            for j in range(y,y+l):
                copy_array[i-x][j-y] = A[i][j]
        
        # 다음 위치로 이동 후 붙여넣기
        for i in range(nx,nx+l):
            for j in range(ny,ny+l):
                temp_A[i][j] = copy_array[i-nx][j-ny]
        
        x,y = nx,ny
    A = temp_A

# 깊이가 2^L이 될 때 까지 재귀 호출
def storm(l):
    global A
    temp_A = [[0]*R for _ in range(R)]
    L = 2**l
    for ii in range(0, R, L):
        for jj in range(0, R, L):
            for i in range(L):
                for j in range(L):
                    temp_A[ii + i][jj + j] = A[ii + (L-j-1)][jj + i]
    A = temp_A


# 얼음 녹이기
def fire():
    global A
    temp_a = [a[:] for a in A] # 원본 복사
    for i in range(R):
        for j in range(R):
            ice_count = 0
            # 현재 칸이 얼음인지 파악
            if A[i][j] == 0: # 얼음이 아니라면 
                continue
            # 영역 검사 및 주변에 얼음있는지 검사
            for k in range(4):
                ni = i + dx[k]; nj = j + dy[k]
                if 0<=ni<R and 0<=nj<R:
                    if A[ni][nj] > 0: # 얼음이 존재한다면
                        ice_count += 1
            # 현재 칸에 존재하는 얼음이 2개 이하라면 -> 얼음을 녹인다.
            if ice_count <= 2:
                temp_a[i][j] -= 1
    A = temp_a

# 0. 마법사 상어의 각 단계 반복
for l in L:
    storm(l)
    fire() # 얼음 녹이기

# 2. 가장 큰 얼음 덩어리 구하기
visited = [[False for _ in range(R)] for _ in range(R)]
max_ice_size = 0 # 가장 큰 얼음 덩어리 크기
for i in range(R):
    for j in range(R):
        # 아직 크기 측정이 되지 않은 얼음 덩어리라면, 탐색 수행
        if A[i][j] > 0 and not visited[i][j]:
            find_max_ice(i,j)
            
print(calc_sum_ice()) # 1. 남아있는 얼음의 합 출력
print(max_ice_size) # 가장 큰 얼음의 크기 출력