# https://www.acmicpc.net/problem/17779
'''
1. 경계선 나누기 작업 수행
2. 나눠진 경계선을 기준으로 각 선거구역의 인구 파악
3. 모든 경우에 대해서 반복

nxn 크기의 영역
'''
INT_MAX = float('inf')
n = int(input())

grid = [[0]*(n+1)]
for _ in range(n):
    grid.append([0] + list(map(int,input().split())))

total_pop = sum(sum(r) for r in grid)

min_diff = float('inf') # 가장 많은 선거구 - 가장 적은 선거구 -> 최소값

def in_ragne(x,y):
    return 0<=x<n and 0<=y<n

def simulation(x,y,d1,d2):
    dxs = [1,1,-1,-1]
    dys = [-1,1,1,-1]
    ds = [d1,d2,d1,d2] # 증가량 설정
    # 현재 설정한 영역으로 올바르게 선거구역을 나눌수있는지 확인
    check = [[0]*(n+1) for _ in range(n+1)]
    for dx,dy,d in zip(dxs,dys,ds):
        for _ in range(d):
            nx = x + dx
            ny = y + dy
            if not in_ragne(nx,ny):
                return INT_MAX
            check[nx][ny] = 5 # 5번 구역으로 모두 표시
            x,y = nx,ny
    
    # 내부 채우기
    for r in range(n):
        left, right = -1, -1 
        for c in range(n):
            if check[r][c] == 5:
                if left == -1:
                    left = c 
                else:
                    right = c
        # 좌우 경계선 사이를 5로 채우기
        if left != -1 and right != -1:
            for c in range(left, right + 1):
                check[r][c] = 5
    
    pop = [0,0,0,0,0]
    
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if check[r][c] == 5:
                pop[4] += grid[r][c] #5번 선거구
            elif r < x + d1 and c <= y:  
                pop[0] += grid[r][c] #1번 선거구 
            elif r <= x + d2 and y < c:
                pop[1] += grid[r][c] #2번 선거구 
            elif x + d1 <= r and c < y - d1 + d2:
                pop[2] += grid[r][c] #3번 선거구 
            elif x + d2 < r and y - d1 + d2 <= c:
                pop[3] += grid[r][c] #4번 선거구 
    
    return max(pop) - min(pop) # 최대값 최소값 차이 리턴


# 기준점 (x, y)와 경계의 길이 d1, d2를 정한다. 
# (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
for x in range(1,n+1):
    for y in range(1,n+1):
        # 경계 길이 정하기
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                min_diff = min(min_diff, simulation(x,y,d1,d2))

print(min_diff)
