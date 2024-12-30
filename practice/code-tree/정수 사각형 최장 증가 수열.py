# 격자 안에서 한 칸씩 전진하는 DP / 정수 사각형 최장 증가 수열
'''
n×n 크기의 격자 정보가 주어졌을 때, 시작점을 적절하게 잡아 상하좌우로 인접한 칸으로 
계속 칸에 적혀있는 정수값이 커지도록 이동한다고 했을 때 밟고 지나갈 수 있는 최대 칸의 수를 구하는 프로그램을 작성해보세요.

1 ≤ n ≤ 500
1 ≤ 주어지는 숫자 ≤ 10^9

memo[x][y] : (x,y) 칸에서 상하좌우로 이동하여 지나갈 수 있는 최대 칸의 수
'''
import sys
sys.setrecursionlimit(500*500)
UNUSED = -1
n = int(input())
numbers = [list(map(int,input().split())) for _ in range(n)]
memo = [[UNUSED]*n for _ in range(n)]
dxs = [0,0,-1,1]; dys = [-1,1,0,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find_max_value(x,y):
    # 이미 기록된 칸이라면 반환 
    if memo[x][y] != UNUSED:
        return memo[x][y]
        
    # 네 방향 이동 - 현재 칸보다 큰 값이 존재하는 경우로만 이동 가능
    temp_max = 1 # 최소한 현재 칸은 이동 가능
    curr = numbers[x][y] # 현재 수
    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy
        if in_range(nx,ny) and curr < numbers[nx][ny]:
            # 기존에 기록된 값 vs 현재 위치에서 탐색을 통해 얻은 최대값
            # 네 방향 중에 가장 많이 이동 가능한 경우로 현재 값 갱신
            temp_max = max(temp_max, find_max_value(nx,ny)+1)
    memo[x][y] = temp_max
    return memo[x][y]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result,find_max_value(i,j))

print(result)