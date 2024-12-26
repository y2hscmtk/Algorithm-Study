'''
dp[i][j]: (i,j)번째에 위치해있을때 현재까지 거쳐간 경로들의 숫자들 중 최소값
'''
UNUSED =  float('inf')
n = int(input())
numbers = [list(map(int,input().split())) for _ in range(n)]
memo = [[UNUSED]*n for _ in range(n)] # 최소값 기록
# 오른쪽, 밑으로만 이동
dxs = [0,1]; dys = [1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

result = 0
def dfs(x,y):
    global result
    if memo[x][y] != UNUSED:
        return memo[x][y]
    # 목적지 도달시
    if (x,y) == (n-1,n-1):
        return numbers[x][y]
    min_result = 0
    for dx,dy in zip(dxs,dys):
        nx = x + dx; ny = y + dy
        # 2가지 방향중 최소값으로
        if in_range(nx,ny):
            # 두 경우 어떤 경로로 갔을때 최소값중 최대값인지 알고 싶음
            min_result = max(min_result, min(dfs(nx,ny),numbers[x][y]))
    memo[x][y] = min_result
    return memo[x][y]
        
result = dfs(0,0)
print(result)