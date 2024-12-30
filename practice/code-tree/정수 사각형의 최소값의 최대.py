# 격자 안에서 한 칸씩 전진하는 DP / 정수 사각형 최댓값의 최소
'''
N×N 행렬이 주어졌을 때, (1,1)에서 시작하여 오른쪽 혹은 밑으로만 이동하여 (N,N)으로 간다고 했을 때 
거쳐간 위치에 적혀있는 숫자들 중 최댓값을 최소로 하는 프로그램을 작성해보세요.
'''
UNUSED = -1
n = int(input())
numbers = [list(map(int,input().split())) for _ in range(n)]
memo = [[UNUSED]*n for _ in range(n)]
result = 1000001

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find_max_min(x,y):
    global result
    if memo[x][y] != UNUSED:
        return memo[x][y]
    
    # 목적지 도달시 - (n-1,n-1)
    if (x,y) == (n-1,n-1):
        return numbers[x][y]
    
    # 오른쪽, 밑으로만 이동 가능
    dxs,dys = [0,1],[1,0]

    temp_min = float('inf')
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx,y+dy
        if in_range(nx,ny):
            # 현재값 vs 이동하여 얻은 경로들 중 최대값
            # 오른쪽, 밑 두개의 경로 중 얻은 최대값
            # 두 경우 어떤 경로로 갔을때 최대값중 최소값인지 알고 싶음
            temp_min = min(temp_min,max(numbers[x][y],find_max_min(nx,ny)))

    memo[x][y] = temp_min
    return memo[x][y]

find_max_min(0,0)

print(find_max_min(0,0))