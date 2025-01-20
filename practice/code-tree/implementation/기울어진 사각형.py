'''
대각선 이동 원리 유형
대각선으로 이동하여 기울어진 직사각형을 이루며 이동하며 적힌 숫자들의 합이 최대가 되는 경우 반환
이동하는 도중 격자 밖으로 벗어나면 안된다.

1. 최대로 가능한 대각선의 길이 계산 - 최대 n까지 가능 - 가장 긴 대각선 (n*n)
2. 탐색 시작할 위치 정하기 (n*n)
3<=n<=20

O(n^5)

'''
n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

# 영역 검사
def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 탐색
# 탐색 과정중 영역을 벗어나는 경우는 고려 x
def search(x,y,k,l):
    # 1번 경로로 이동시 - x-1,y+1 # 2번 경로로 이동시 - x-1,y-1
    # 3번 경로로 이동시 - x+1,y-1 # 4번 경로로 이동시 - x+1,y+1
    dxs = [-1,-1,1,1]
    dys = [1,-1,-1,1]
    move_num = [k,l,k,l]
    temp_sum = 0
    # k,l은 각 대각선의 방향에서 이동해야할 칸의 개수
    for dx,dy,num in zip(dxs,dys,move_num):
        for _ in range(num): # 현재 방향에서의 num만큼 이동
            nx,ny = x + dx, y + dy
            if not in_range(nx,ny):
                return 0 # 현재 수행에서 실패하는 경우
            temp_sum += grid[nx][ny]
            x,y = nx,ny
    return temp_sum

max_sum = 0 # 최대 숫자들의 합
# 탐색 시작 위치 지정
for i in range(n):
    for j in range(n):
        # 각 대각선에서 이동할 길이 설정
        for k in range(1,n):
            for l in range(1,n):
                max_sum = max(max_sum, search(i,j,k,l))
                
print(max_sum)
